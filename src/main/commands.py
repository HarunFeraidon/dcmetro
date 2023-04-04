import http.client, urllib.request, urllib.parse, urllib.error, base64
import os
from dotenv import load_dotenv, find_dotenv
from . import constants
from .dijkstra import dijkstra
from .build_graph import Graph, GraphNode
import json

load_dotenv(find_dotenv())
API_KEY = os.environ.get("API_KEY")
headers = {
    # Request headers
    'api_key': API_KEY,
}

def handle_commands(command: str, args: list) -> str:
    commands = {
        constants.query_when: command_when,
        constants.query_length: command_from_to,
        constants.query_path: command_path,
    }
    if command in commands:
        return commands[command](*args)
    else:
        error = f"command not found: {command}"
        return error


def command_when(*locations: list) -> str:
    location = " ".join(locations)
    error_message = constants.ERROR_LOCATION_NOT_RECOGNIZED
    station_code = get_station_code(location, error_message)
    if station_code == error_message:
        return error_message

    params = urllib.parse.urlencode({})
    endpoint = f"/StationPrediction.svc/json/GetPrediction/{station_code}?{params}"
    data = make_wmata_request(endpoint)
    if (connection_broken(data)):
        return constants.ERROR_CONN
    arrivals = organize_for_when(data)
    return arrivals


def organize_for_when(data: dict) -> str:
    arrivals = {}
    results = data["Trains"]
    for result in results:
        if (result["DestinationCode"] == None or result["Min"] == ''
                or result["Car"] == None):
            continue
        minute = result["Min"]
        destination = result["Destination"]
        arrivals.setdefault(destination, [])
        arrivals[destination].append(minute)
    arrivals_list = []
    for platform in arrivals:
        arrivals_list.append(
            f"For {platform}, the next arrivals are in {', '.join(arrivals[platform])} minutes"
        )
    return "\n".join(arrivals_list)


def process_multi_word_locations(*locations: list) -> list:
    before_to = []
    after_to = []
    found_to = False
    for loc in locations:
        loc = loc.strip()
        if loc.lower() == "to":
            found_to = True
        elif not found_to:
            before_to.append(loc)
        else:
            after_to.append(loc)
    if not found_to:
        return [constants.ERROR_FROM_TO]
    from_location = " ".join(before_to)
    to_location = " ".join(after_to)
    if (from_location == to_location):
        return [constants.ERROR_DUPLICATE_LOCATIONS]
    if (from_location == "" or to_location == ""):
        return [constants.ERROR_EMPTY_LOCATION]
    return [from_location, to_location]


def command_from_to(*locations: list) -> str:
    processed_locations = process_multi_word_locations(*locations)
    if (len(processed_locations) == 1):
        return processed_locations[0]
    else:
        from_location, to_location = processed_locations
    from_error = constants.ERROR_FROM_LOCATION
    to_error = constants.ERROR_TO_LOCATION
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
    if (connection_broken(data)):
        return constants.ERROR_CONN
    rail_time = organize_from_to(data, from_location, to_location)
    return rail_time


def organize_from_to(data: dict, from_location: str, to_location: str) -> str:
    info = data["StationToStationInfos"][0]
    rail_time = info["RailTime"]
    return f"The estimated rail time from '{from_location}' to '{to_location}' is {rail_time} minutes"


def command_path(*locations: list) -> str:
    processed_locations = process_multi_word_locations(*locations)
    if (len(processed_locations) == 1):
        return processed_locations[0]
    else:
        from_location, to_location = processed_locations
    from_error = constants.ERROR_FROM_LOCATION
    to_error = constants.ERROR_TO_LOCATION
    from_station_code = get_station_code(from_location, from_error)
    if (from_station_code == from_error):
        return from_error
    to_station_code = get_station_code(to_location, to_error)
    if (to_station_code == to_error):
        return to_error
    path = dijkstra(from_station_code, to_station_code)
    path_with_names = []
    for code in path:
        path_with_names.append(
            get_station_name(code)
        )  # error message not necessart since impossible at this point
    path = ' -> '.join(path_with_names)
    return path


def get_station_code(location: str, error_message: str) -> str:
    if (location.lower() in constants.STATION_CODES):
        return constants.STATION_CODES[location.lower()]
    else:
        return error_message


def get_station_name(station_code: str) -> str:
    # list out keys and values separately
    key_list = list(constants.STATION_CODES.keys())
    val_list = list(constants.STATION_CODES.values())

    position = val_list.index(station_code)
    return key_list[position]


def make_wmata_request(endpoint: str) -> dict:
    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", f"{endpoint}", "{body}", headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        data = json.loads(data)
        conn.close()
        return data
    except Exception as e:
        return {constants.ERROR_CONN: str(e)}


def connection_broken(data: dict) -> bool:
    if constants.ERROR_CONN in data:
        return True
    return False


def process_input() -> None:
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
    except KeyboardInterrupt:
        print("\nExecution interrupted by the user.")
    except Exception as e:
        print(e)


def process_message(message) -> str:
    inputs = message.split()
    if len(inputs) == 0:
        return ""
    command = inputs[0]
    args = inputs[1:]
    if len(args) == 0:
        return ""
    return handle_commands(command, args)
