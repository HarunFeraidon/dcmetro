import unittest
from unittest.mock import patch
from main import app, constants


class TestCommands(unittest.TestCase):

    @patch('main.app.make_wmata_request')
    def test_command_when_base(self, mock_make_wmata_request):
        command = "when"
        location = ["McLean"]
        data = {
            'Trains': [{
                'Car': '6',
                'Destination': 'Ashburn',
                'DestinationCode': 'N12',
                'Min': 'BRD'
            }, {
                'Car': '8',
                'Destination': 'Largo',
                'DestinationCode': 'G05',
                'Min': '6'
            }, {
                'Car': '8',
                'Destination': 'Ashburn',
                'DestinationCode': 'N12',
                'Min': '15'
            }, {
                'Car': '8',
                'Destination': 'Largo',
                'DestinationCode': 'G05',
                'Min': '26'
            }, {
                'Car': '6',
                'Destination': 'Ashburn',
                'DestinationCode': 'N12',
                'Min': '32'
            }]
        }
        results = {'Largo': ['6', '26'], 'Ashburn': ['BRD', '15', '32']}
        mock_make_wmata_request.return_value = data
        self.assertEqual(app.handle_commands(command, location), results)

        location = ["NoMa-Gallaudet", "U"]
        data = {
            'Trains': [{
                'Car': '8',
                'Destination': 'Largo',
                'DestinationCode': 'G05',
                'Min': 'BRD'
            }, {
                'Car': '8',
                'Destination': 'Vienna',
                'DestinationCode': 'K08',
                'Min': 'BRD'
            }, {
                'Car': '8',
                'Destination': 'NewCrltn',
                'DestinationCode': 'D13',
                'Min': ''
            }, {
                'Car': '6',
                'Destination': 'NewCrltn',
                'DestinationCode': 'D13',
                'Min': ''
            }, {
                'Car': None,
                'Destination': 'ssenger',
                'DestinationCode': None,
                'Min': ''
            }]
        }
        results = {'Largo': ['BRD'], 'Vienna': ['BRD']}
        mock_make_wmata_request.return_value = data
        self.assertEqual(app.handle_commands(command, location), results)

    def test_command_not_found(self):
        command = "whn"
        result = f"command not found: {command}"
        self.assertEqual(app.handle_commands(command, "McLean"), result)

    def test_location_not_recognized(self):
        command = "when"
        location = ["disneyland"]
        result = "Location not recognized"
        self.assertEqual(app.handle_commands(command, location), result)

    @patch('main.app.make_wmata_request')
    def test_command_from_to_base(self, mock_make_wmata_request):
        command = "from"
        location = ["McLean", "to", "Ashburn"]
        data = {
            'StationToStationInfos': [{
                'RailTime': 36,
            }]
        }
        mock_make_wmata_request.return_value = data
        self.assertEqual(app.handle_commands(command, location), 36)

        location = [
            "Woodley", "Park-Zoo/Adams", "Morgan", "to", "Gallery",
            "Pl-Chinatown"
        ]
        data = {
            'StationToStationInfos': [{
                'RailTime': 8,
            }]
        }
        mock_make_wmata_request.return_value = data
        self.assertEqual(app.handle_commands(command, location), 8)

    def test_command_from_to_without_to(self):
        command = "from"
        location = ["McLean", "Ashburn"]  # "to" is a required input
        result = "Error: please follow a 'from' start 'to' end format"
        self.assertEqual(app.handle_commands(command, location), result)

    def test_command_from_to_location_not_recognized(self):
        command = "from"
        location = ["loot", "lake", "to", "Ashburn"]
        result = "'From' location not recognized"
        self.assertEqual(app.handle_commands(command, location), result)
        location = ["Bethesda", "to", "tilted", "towers"]
        result = "'To' location not recognized"
        print(app.handle_commands(command, location))
        self.assertEqual(app.handle_commands(command, location), result)

    def test_make_wmata_request(self):
        sample_endpoint = "/StationPrediction.svc/json/GetPrediction/N01?"
        bad_endpoint = "bad_endpoint"
        result = app.make_wmata_request(sample_endpoint)
        self.assertTrue(constants.ERROR_CONN not in result)
        result = app.make_wmata_request(bad_endpoint)
        self.assertTrue(constants.ERROR_CONN in result)


if __name__ == '__main__':
    unittest.main()