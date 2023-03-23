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
    }
    if command in commands:
        commands[command](*args)
    else:
        print("command not recognized")


def command_when(location):
    print("You want to know when", location, "is.")
    if(location in constants.STATION_CODES):
        station_code = constants.STATION_CODES[location]
        # print("Location name: {} Code: {}".format(location, constants.STATION_CODES[location]))
    else:
        print("location not recognized")
        return

    params = urllib.parse.urlencode({})
    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request(
            "GET",
            f"/StationPrediction.svc/json/GetPrediction/{station_code}?{params}",
            "{body}", headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        data = json.loads(data)
        organize_for_when(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def organize_for_when(data):
    arrivals = {}
    results = data["Trains"]
    for result in results:
        minute = result["Min"]
        destination = result["Destination"]
        arrivals.setdefault(destination, [])
        arrivals[destination].append(minute)
    for platform in arrivals:
        print(f"For {platform}, the next arrivals are in {', '.join(arrivals[platform])} minutes")


def command_help(args):
    print("Asdf")


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