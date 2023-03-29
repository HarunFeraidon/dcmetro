from app import make_wmata_request, headers
import urllib.parse

colors = ["RD", "YL", "GR", "BL", "OR", "SV"]

def get_each_lines_start_and_end_stations():
    endpoint = "/Rail.svc/json/jLines"
    data = make_wmata_request(endpoint) 
    result = {}
    lines = data["Lines"]
    for line in lines:
        result.setdefault(line["LineCode"], (line["StartStationCode"], line["EndStationCode"]))
    # {'BL': ('J03', 'G05'), 'GR': ('F11', 'E10'), 'OR': ('K08', 'D13'),
    # 'RD': ('A15', 'B11'), 'SV': ('N12', 'G05'), 'YL': ('C15', 'E06')}
    generate_all_lines_path(result)
    return result

def generate_all_lines_path(lines):
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
            info.append({stop["StationCode"]: stop["DistanceToPrev"]})
        lines_with_stops.setdefault(line, info)
    print(lines_with_stops)
    return lines_with_stops


    

if __name__ == '__main__':
    get_each_lines_start_and_end_stations()
