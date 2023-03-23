import http.client, urllib.request, urllib.parse, urllib.error, base64
import app
import json

headers = {
    # Request headers
    'api_key': app.API_KEY,
}


def get_station_codes():
    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/Rail.svc/json/jStations", "{body}", headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        data = json.loads(data)
        map_station_codes_to_name(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def map_station_codes_to_name(data):
    station_codes = {}
    stations_list = data["Stations"]
    for station in stations_list:
        station_codes[station['Name']] = station['Code']
        # print("Code: {}, Name: {}".format(station['Code'], station['Name']))
    print(station_codes)
    return station_codes


def get_stations_per_color():
    params = urllib.parse.urlencode({
        # Request parameters
        'LineCode': 'SV',
    })

    colors = ["RD", "YL", "GR", "BL", "OR", "SV"]

    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        for color in colors:
            conn.request("GET","/Rail.svc/json/jStations?LineCode=%s" % color, "{body}", headers)
            response = conn.getresponse()
            data = response.read().decode('utf-8')
            data = json.loads(data)
            print(color)
            map_station_codes_to_name(data)
            conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


if __name__ == '__main__':
    get_stations_per_color()
