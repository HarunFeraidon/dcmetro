from .commands import make_wmata_request, headers
import urllib.parse

colors = ["RD", "YL", "GR", "BL", "OR", "SV"]


def get_each_lines_start_and_end_stations() -> dict:
    endpoint = "/Rail.svc/json/jLines"
    data = make_wmata_request(endpoint)
    result = {}
    lines = data["Lines"]
    for line in lines:
        result.setdefault(line["LineCode"],
                          (line["StartStationCode"], line["EndStationCode"]))
    generate_all_lines_path(result)
    return result


def generate_all_lines_path(lines: dict) -> dict:
    lines_with_stops = {}
    for line in lines:
        params = urllib.parse.urlencode({
            # Request parameters
            'FromStationCode': lines[line][0],
            'ToStationCode': lines[line][1],
        })
        endpoint = "/Rail.svc/json/jPath?%s" % params
        data = make_wmata_request(endpoint)
        each_stop = data["Path"]
        info = []
        for stop in each_stop:
            info.append([stop["StationCode"], stop["DistanceToPrev"]])
        lines_with_stops.setdefault(line, info)
    return lines_with_stops
