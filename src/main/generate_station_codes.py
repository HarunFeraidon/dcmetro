import http.client, urllib.request, urllib.parse, urllib.error, base64
from . import commands
import json

headers = {
    # Request headers
    'api_key': commands.API_KEY,
}


def get_station_codes() -> None:
    endpoint = "/Rail.svc/json/jStations"
    data = commands.make_wmata_request(endpoint)
    map_station_codes_to_name(data)


def map_station_codes_to_name(data: dict) -> dict:
    station_codes = {}
    stations_list = data["Stations"]
    for station in stations_list:
        station_codes[station['Name'].lower()] = station['Code']
    return station_codes