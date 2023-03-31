import http.client, urllib.request, urllib.parse, urllib.error, base64
import os
from dotenv import load_dotenv, find_dotenv
# from main import constants
import constants
from dijkstra import dijkstra
from build_graph import Graph, GraphNode
import json

load_dotenv(find_dotenv())
API_KEY = os.environ.get("API_KEY")

headers = {
    # Request headers
    'api_key': API_KEY,
}


def handle_commands(command, args):
    commands = {
        'when': command_when,
        'from': command_from_to,
        'path': command_path,
    }
    if command in commands:
        return commands[command](*args)
    else:
        error = f"command not found: {command}"
        return error


def command_when(*locations):
    location = " ".join(locations)
    error_message = "Location not recognized"
    station_code = get_station_code(location, error_message)
    if station_code == error_message:
        return error_message

    params = urllib.parse.urlencode({})
    endpoint = f"/StationPrediction.svc/json/GetPrediction/{station_code}?{params}"
    data = make_wmata_request(endpoint)
    if(connection_broken(data)):
        return constants.ERROR_CONN
    arrivals = organize_for_when(data)
    return arrivals


def organize_for_when(data):
    arrivals = {}
    results = data["Trains"]
    for result in results:
        if(result["DestinationCode"] == None or result["Min"] == '' or result["Car"] == None):
            continue
        minute = result["Min"]
        destination = result["Destination"]
        arrivals.setdefault(destination, [])
        arrivals[destination].append(minute)
    for platform in arrivals:
        print(
            f"For {platform}, the next arrivals are in {', '.join(arrivals[platform])} minutes"
        )
    return arrivals

def process_multi_word_locations(*locations):
    before_to = []
    after_to = []
    found_to = False
    for loc in locations:
        if loc.lower() == "to":
            found_to = True
        elif not found_to:
            before_to.append(loc)
        else:
            after_to.append(loc)
    if not found_to:
        return "Error: please follow a 'from' start 'to' end format"
    from_location = " ".join(before_to)
    to_location = " ".join(after_to)
    return from_location, to_location

def command_from_to(*locations):
    from_location, to_location = process_multi_word_locations(*locations)
    from_error = "'From' location not recognized"
    to_error = "'To' location not recognized"
    from_station_code = get_station_code(from_location, from_error)
    if (from_station_code == from_error):
        return from_error
    to_station_code = get_station_code(to_location, to_error)
    if (to_station_code == to_error):
        return to_error
    params = urllib.parse.urlencode({
        # Request parameters
        'FromStationCode': from_station_code,
        'ToStationCode': to_station_code,
    })
    endpoint = f"/Rail.svc/json/jSrcStationToDstStationInfo?{params}"
    data = make_wmata_request(endpoint)
    if(connection_broken(data)):
        return constants.ERROR_CONN
    rail_time = organize_from_to(data, from_location, to_location)
    return rail_time


def organize_from_to(data, from_location, to_location):
    info = data["StationToStationInfos"][0]
    rail_time = info["RailTime"]
    print(
        f"The estimated rail time from {from_location} to {to_location} is {rail_time}"
    )
    return rail_time

def command_path(*locations):
    from_location, to_location = process_multi_word_locations(*locations)
    from_error = "'From' location not recognized"
    to_error = "'To' location not recognized"
    from_station_code = get_station_code(from_location, from_error)
    if (from_station_code == from_error):
        return from_error
    to_station_code = get_station_code(to_location, to_error)
    if (to_station_code == to_error):
        return to_error
    path = dijkstra(from_station_code, to_station_code)
    path_with_names = []
    for code in path:
        path_with_names.append(get_station_code(code, "")) # error message not necessart since impossible at this point
    path = ' -> '.join(path_with_names)
    print(path)
    return path
    

def get_station_code(location, error_message):
    if (location in constants.STATION_CODES):
        return constants.STATION_CODES[location]
        # print("Location name: {} Code: {}".format(location, constants.STATION_CODES[location]))
    else:
        return error_message
    
def make_wmata_request(endpoint):
    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", f"{endpoint}", "{body}", headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        data = json.loads(data)
        conn.close()
        # print(data)
        return data
    except Exception as e:
        # print({constants.ERROR_CONN, str(e)})
        return {constants.ERROR_CONN: str(e)}
        # print("[Errno {0}] {1}".format(e.errno, e.strerror))

def connection_broken(data):
    if constants.ERROR_CONN in data:
        return True
    return False
    


def process_input():
    try:
        while True:
            user_input = input("Enter a command: ")
            inputs = user_input.split()
            if len(inputs) == 0:
                continue
            command = inputs[0]
            args = inputs[1:]
            if len(args) == 0:
                continue
            handle_commands(command, args)
            # print(inputs[0])
            # print(inputs[1])
    except KeyboardInterrupt:
        print("\nExecution interrupted by the user.")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    process_input()