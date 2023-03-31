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
        self.assertEqual(app.handle_commands(command, location), "The estimated rail time from McLean to Ashburn is 36")

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
        self.assertEqual(app.handle_commands(command, location), "The estimated rail time from Woodley Park-Zoo/Adams Morgan to Gallery Pl-Chinatown is 8")

    def test_command_from_to_location_not_recognized(self):
        command = "from"
        location = ["loot", "lake", "to", "Ashburn"]
        result = "'From' location not recognized"
        self.assertEqual(app.handle_commands(command, location), result)
        location = ["Bethesda", "to", "tilted", "towers"]
        result = "'To' location not recognized"
        print(app.handle_commands(command, location))
        self.assertEqual(app.handle_commands(command, location), result)

    def test_command_from_to_error(self):
        command = "from"
        location = ["Ashburn", "to", "Ashburn"]
        result = constants.ERROR_DUPLICATE_LOCATIONS
        self.assertEqual(app.handle_commands(command, location), result)

    def test_make_wmata_request(self):
        sample_endpoint = "/StationPrediction.svc/json/GetPrediction/N01?"
        bad_endpoint = "bad_endpoint"
        result = app.make_wmata_request(sample_endpoint)
        self.assertTrue(constants.ERROR_CONN not in result)
        result = app.make_wmata_request(bad_endpoint)
        self.assertTrue(constants.ERROR_CONN in result)

    def test_command_path(self):
        command = "path"
        location = ["McLean", "to", "Court", "House"]
        expected_path = "McLean -> East Falls Church -> Ballston-MU -> Virginia Square-GMU -> Clarendon -> Court House"
        self.assertEqual(app.handle_commands(command, location), expected_path)

        command = "path"
        location = ["Waterfront", "to", "Arlington", "Cemetery"]
        expected_path = "Waterfront -> L'Enfant Plaza -> Pentagon -> Arlington Cemetery"
        self.assertEqual(app.handle_commands(command, location), expected_path)

        location = ["Smithsonian", "to", "Ronald", "Reagan", "Washington", "National", "Airport"]
        expected_path = "Smithsonian -> L'Enfant Plaza -> Pentagon -> Pentagon City -> Crystal City -> Ronald Reagan Washington National Airport"
        self.assertEqual(app.handle_commands(command, location), expected_path)

        location = ["Mt", "Vernon", "Sq", "7th", "St-Convention", "Center", "to", "Dupont", "Circle",]
        expected_path = "Mt Vernon Sq 7th St-Convention Center -> Gallery Pl-Chinatown -> Metro Center -> Farragut North -> Dupont Circle"
        self.assertEqual(app.handle_commands(command, location), expected_path)

    def test_command_path_error(self):
        command = "path"
        location = ["McLean", "to", "McLean"]
        expected_error = constants.ERROR_DUPLICATE_LOCATIONS
        self.assertEqual(app.handle_commands(command, location), expected_error)

    def test_process_multi_word_locations(self):
        locations = ["McLean", "to", "Court", "House"]
        expected = ["McLean", "Court House"]
        self.assertEqual(app.process_multi_word_locations(*locations), expected)
        locations = ["McLean", "Court", "House"]
        expected = [constants.ERROR_FROM_TO]
        self.assertEqual(app.process_multi_word_locations(*locations), expected)
        locations = [" ", "to", "Smithsonian"]
        expected = [constants.ERROR_EMPTY_LOCATION]
        self.assertEqual(app.process_multi_word_locations(*locations), expected)
        locations = ["Glenmont", "to"]
        expected = [constants.ERROR_EMPTY_LOCATION]
        self.assertEqual(app.process_multi_word_locations(*locations), expected)
        locations = ["Glenmont", "to", "Glenmont"]
        expected = [constants.ERROR_DUPLICATE_LOCATIONS]
        self.assertEqual(app.process_multi_word_locations(*locations), expected)

if __name__ == '__main__':
    unittest.main()