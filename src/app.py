import http.client, urllib.request, urllib.parse, urllib.error, base64
import os
from dotenv import load_dotenv, find_dotenv
import constants
import json

load_dotenv(find_dotenv())
API_KEY = os.environ.get("API_KEY")
print(API_KEY)


def handle_commands(command, args):
    commands = {
        'when': command_when,
        'from': command_from_to,
    }
    if command in commands:
        commands[command](*args)
    else:
        print("command not recognized")


def command_when(*locations):
    location = " ".join(locations)
    print("You want to know when", location, "is.")
    station_code = get_station_code(location, "Location not recognized")

    params = urllib.parse.urlencode({})
    endpoint =  f"/StationPrediction.svc/json/GetPrediction/{station_code}?{params}"
    data = make_wmata_request(endpoint)
    organize_for_when(data)


def organize_for_when(data):
    arrivals = {}
    results = data["Trains"]
    for result in results:
        minute = result["Min"]
        destination = result["Destination"]
        arrivals.setdefault(destination, [])
        arrivals[destination].append(minute)
    for platform in arrivals:
        print(
            f"For {platform}, the next arrivals are in {', '.join(arrivals[platform])} minutes"
        )


def command_from_to(*locations):
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
        print("Error: please follow a 'from' start 'to' end format")
        return
    from_location = " ".join(before_to)
    to_location = " ".join(after_to)
    from_station_code = get_station_code(from_location,
                                         "'From' location not recognized")
    to_station_code = get_station_code(to_location,
                                       "'To' location not recognized")
    params = urllib.parse.urlencode({
        # Request parameters
        'FromStationCode': from_station_code,
        'ToStationCode': to_station_code,
    })
    endpoint = "/Rail.svc/json/jPath?%s" % params
    data = make_wmata_request(endpoint)
    print(data)


def get_station_code(location, error_message):
    if (location in constants.STATION_CODES):
        return constants.STATION_CODES[location]
        # print("Location name: {} Code: {}".format(location, constants.STATION_CODES[location]))
    else:
        print(error_message)
        return


def make_wmata_request(endpoint):
    params = urllib.parse.urlencode({})
    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", f"{endpoint}", "{body}", headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        data = json.loads(data)
        conn.close()
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def process_input():
    try:
        while True:
            user_input = input("Enter a command: ")
            inputs = user_input.split()
            if len(inputs) == 0:
                continue
            command = inputs[0]
            args = inputs[1:]
            handle_commands(command, args)
            # print(inputs[0])
            # print(inputs[1])
    except:
        print("\nExecution interrupted by the user.")


headers = {
    # Request headers
    'api_key': API_KEY,
}

params = urllib.parse.urlencode({})


def station_prediction():
    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request(
            "GET",
            "/StationPrediction.svc/json/GetPrediction/{StationCodes}?%s" %
            params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


if __name__ == '__main__':
    process_input()