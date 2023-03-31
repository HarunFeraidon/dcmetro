ERROR_CONN = "Error: connection is broken"
ERROR_FROM_TO = "Error: please follow a 'from' start 'to' end format"
ERROR_DUPLICATE_LOCATIONS = "Error: please do not enter duplicate locations"
ERROR_EMPTY_LOCATION = "Error: please enter a 'from' location and a 'to' location"

LINE_CODES = {
    'Red' : 'RD',
    'Yellow' : 'YL',
    'Green' : 'GR',
    'Blue' : 'BL',
    'Orange' : 'OR',
    'Silver' : 'SV',
}

STATION_CODES = {
    'Metro Center': 'C01',
    'Farragut North': 'A02',
    'Dupont Circle': 'A03',
    'Woodley Park-Zoo/Adams Morgan': 'A04',
    'Cleveland Park': 'A05',
    'Van Ness-UDC': 'A06',
    'Tenleytown-AU': 'A07',
    'Friendship Heights': 'A08',
    'Bethesda': 'A09',
    'Medical Center': 'A10',
    'Grosvenor-Strathmore': 'A11',
    'North Bethesda': 'A12',
    'Twinbrook': 'A13',
    'Rockville': 'A14',
    'Shady Grove': 'A15',
    'Gallery Pl-Chinatown': 'F01',
    'Judiciary Square': 'B02',
    'Union Station': 'B03',
    'Rhode Island Ave-Brentwood': 'B04',
    'Brookland-CUA': 'B05',
    'Fort Totten': 'E06',
    'Takoma': 'B07',
    'Silver Spring': 'B08',
    'Forest Glen': 'B09',
    'Wheaton': 'B10',
    'Glenmont': 'B11',
    'NoMa-Gallaudet U': 'B35',
    'McPherson Square': 'C02',
    'Farragut West': 'C03',
    'Foggy Bottom-GWU': 'C04',
    'Rosslyn': 'C05',
    'Arlington Cemetery': 'C06',
    'Pentagon': 'C07',
    'Pentagon City': 'C08',
    'Crystal City': 'C09',
    'Ronald Reagan Washington National Airport': 'C10',
    'Braddock Road': 'C12',
    'King St-Old Town': 'C13',
    'Eisenhower Avenue': 'C14',
    'Huntington': 'C15',
    'Federal Triangle': 'D01',
    'Smithsonian': 'D02',
    "L'Enfant Plaza": 'F03',
    'Federal Center SW': 'D04',
    'Capitol South': 'D05',
    'Eastern Market': 'D06',
    'Potomac Ave': 'D07',
    'Stadium-Armory': 'D08',
    'Minnesota Ave': 'D09',
    'Deanwood': 'D10',
    'Cheverly': 'D11',
    'Landover': 'D12',
    'New Carrollton': 'D13',
    'Mt Vernon Sq 7th St-Convention Center': 'E01',
    'Shaw-Howard U': 'E02',
    'U Street/African-Amer Civil War Memorial/Cardozo': 'E03',
    'Columbia Heights': 'E04',
    'Georgia Ave-Petworth': 'E05',
    'West Hyattsville': 'E07',
    'Hyattsville Crossing': 'E08',
    'College Park-U of Md': 'E09',
    'Greenbelt': 'E10',
    'Archives-Navy Memorial-Penn Quarter': 'F02',
    'Waterfront': 'F04',
    'Navy Yard-Ballpark': 'F05',
    'Anacostia': 'F06',
    'Congress Heights': 'F07',
    'Southern Avenue': 'F08',
    'Naylor Road': 'F09',
    'Suitland': 'F10',
    'Branch Ave': 'F11',
    'Benning Road': 'G01',
    'Capitol Heights': 'G02',
    'Addison Road-Seat Pleasant': 'G03',
    'Morgan Boulevard': 'G04',
    'Downtown Largo': 'G05',
    'Van Dorn Street': 'J02',
    'Franconia-Springfield': 'J03',
    'Court House': 'K01',
    'Clarendon': 'K02',
    'Virginia Square-GMU': 'K03',
    'Ballston-MU': 'K04',
    'East Falls Church': 'K05',
    'West Falls Church': 'K06',
    'Dunn Loring-Merrifield': 'K07',
    'Vienna/Fairfax-GMU': 'K08',
    'McLean': 'N01',
    'Tysons': 'N02',
    'Greensboro': 'N03',
    'Spring Hill': 'N04',
    'Wiehle-Reston East': 'N06',
    'Reston Town Center': 'N07',
    'Herndon': 'N08',
    'Innovation Center': 'N09',
    'Washington Dulles International Airport': 'N10',
    'Loudoun Gateway': 'N11',
    'Ashburn': 'N12'
}

EACH_LINES_START_AND_END_STATION = {'BL': ('J03', 'G05'), 'GR': ('F11', 'E10'), 'OR': ('K08', 'D13'), 'RD': ('A15', 'B11'), 'SV': ('N12', 'G05'), 'YL': ('C15', 'E06')}

# swapped A01 -> C01 and B01 -> F01
# swapped B06 -> E06
# swapped D03 -> F03
EACH_LINES_DISTANCE_TO_PREVIOUS_STATION_LIST = {'BL': [['J03', 0], ['J02', 18695], ['C13', 20158], ['C12', 3453], ['C10', 8605], ['C09', 2939], ['C08', 4068], ['C07', 3216], ['C06', 7036], ['C05', 4936], ['C04', 6993], ['C03', 2783], ['C02', 2001], ['C01', 2359], ['D01', 1561], ['D02', 2016], ['F03', 2643], ['D04', 1757], ['D05', 3052], ['D06', 2703], ['D07', 3289], ['D08', 3750], ['G01', 12162], ['G02', 7779], ['G03', 5215], ['G04', 7960], ['G05', 7256]],
                                                'GR': [['F11', 0], ['F10', 9144], ['F09', 7658], ['F08', 6612], ['F07', 5508], ['F06', 6851], ['F05', 6254], ['F04', 3326], ['F03', 4158], ['F02', 2950], ['F01', 1879], ['E01', 2985], ['E02', 2527], ['E03', 2555], ['E04', 4715], ['E05', 4717], ['E06', 8348], ['E07', 10406], ['E08', 6670], ['E09', 10368], ['E10', 12981]],
                                                'OR': [['K08', 0], ['K07', 13165], ['K06', 12638], ['K05', 10918], ['K04', 13156], ['K03', 2980], ['K02', 2473], ['K01', 2687], ['C05', 5807], ['C04', 6993], ['C03', 2783], ['C02', 2001], ['C01', 2359], ['D01', 1561], ['D02', 2016], ['F03', 2643], ['D04', 1757], ['D05', 3052], ['D06', 2703], ['D07', 3289], ['D08', 3750], ['D09', 11080], ['D10', 4723], ['D11', 6149], ['D12', 9665], ['D13', 7655]],
                                                'RD': [['A15', 0], ['A14', 14151], ['A13', 10586], ['A12', 5895], ['A11', 7309], ['A10', 11821], ['A09', 5530], ['A08', 9095], ['A07', 4135], ['A06', 5841], ['A05', 3320], ['A04', 3740], ['A03', 6304], ['A02', 2487], ['C01', 4178], ['F01', 1505], ['B02', 1967], ['B03', 3446], ['B35', 3548], ['B04', 5771], ['B05', 4553], ['E06', 7378], ['B07', 10026], ['B08', 7484], ['B09', 8871], ['B10', 8484], ['B11', 9334]],
                                                'SV': [['N12', 0], ['N11', 10338], ['N10', 15145], ['N09', 10999], ['N08', 9095], ['N07', 7130], ['N06', 5961], ['N04', 30867], ['N03', 3634], ['N02', 3902], ['N01', 3440], ['K05', 24745], ['K04', 13156], ['K03', 2980], ['K02', 2473], ['K01', 2687], ['C05', 4936], ['C04', 6993], ['C03', 2783], ['C02', 2001], ['C01', 2359], ['D01', 1561], ['D02', 2016], ['F03', 2643], ['D04', 1757], ['D05', 3052], ['D06', 2703], ['D07', 3289], ['D08', 3750], ['G01', 12162], ['G02', 7779], ['G03', 5215], ['G04', 7960], ['G05', 7256]],
                                                'YL': [['C15', 0], ['C14', 2770], ['C13', 3734], ['C12', 3453], ['C10', 8605], ['C09', 2939], ['C08', 4068], ['C07', 3216], ['F03', 12524], ['F02', 2950], ['F01', 1879], ['E01', 2985], ['E02', 2527], ['E03', 2555], ['E04', 4715], ['E05', 4717], ['E06', 8348]]}

EACH_LINES_DISTANCE_TO_PREVIOUS_STATION_DICT = {'BL': [{'J03': 0}, {'J02': 18695}, {'C13': 20158}, {'C12': 3453}, {'C10': 8605}, {'C09': 2939}, {'C08': 4068}, {'C07': 3216}, {'C06': 7036}, {'C05': 4936}, {'C04': 6993}, {'C03': 2783}, {'C02': 2001}, {'C01': 2359}, {'D01': 1561}, {'D02': 2016}, {'F03': 2643}, {'D04': 1757}, {'D05': 3052}, {'D06': 2703}, {'D07': 3289}, {'D08': 3750}, {'G01': 12162}, {'G02': 7779}, {'G03': 5215}, {'G04': 7960}, {'G05': 7256}],
 'GR': [{'F11': 0}, {'F10': 9144}, {'F09': 7658}, {'F08': 6612}, {'F07': 5508}, {'F06': 6851}, {'F05': 6254}, {'F04': 3326}, {'F03': 4158}, {'F02': 2950}, {'F01': 1879}, {'E01': 2985}, {'E02': 2527}, {'E03': 2555}, {'E04': 4715}, {'E05': 4717}, {'E06': 8348}, {'E07': 10406}, {'E08': 6670}, {'E09': 10368}, {'E10': 12981}],
 'OR': [{'K08': 0}, {'K07': 13165}, {'K06': 12638}, {'K05': 10918}, {'K04': 13156}, {'K03': 2980}, {'K02': 2473}, {'K01': 2687}, {'C05': 5807}, {'C04': 6993}, {'C03': 2783}, {'C02': 2001}, {'C01': 2359}, {'D01': 1561}, {'D02': 2016}, {'F03': 2643}, {'D04': 1757}, {'D05': 3052}, {'D06': 2703}, {'D07': 3289}, {'D08': 3750}, {'D09': 11080}, {'D10': 4723}, {'D11': 6149}, {'D12': 9665}, {'D13': 7655}],
 'RD': [{'A15': 0}, {'A14': 14151}, {'A13': 10586}, {'A12': 5895}, {'A11': 7309}, {'A10': 11821}, {'A09': 5530}, {'A08': 9095}, {'A07': 4135}, {'A06': 5841}, {'A05': 3320}, {'A04': 3740}, {'A03': 6304}, {'A02': 2487}, {'C01': 4178}, {'F01': 1505}, {'B02': 1967}, {'B03': 3446}, {'B35': 3548}, {'B04': 5771}, {'B05': 4553}, {'E06': 7378}, {'B07': 10026}, {'B08': 7484}, {'B09': 8871}, {'B10': 8484}, {'B11': 9334}],
 'SV': [{'N12': 0}, {'N11': 10338}, {'N10': 15145}, {'N09': 10999}, {'N08': 9095}, {'N07': 7130}, {'N06': 5961}, {'N04': 30867}, {'N03': 3634}, {'N02': 3902}, {'N01': 3440}, {'K05': 24745}, {'K04': 13156}, {'K03': 2980}, {'K02': 2473}, {'K01': 2687}, {'C05': 4936}, {'C04': 6993}, {'C03': 2783}, {'C02': 2001}, {'C01': 2359}, {'D01': 1561}, {'D02': 2016}, {'F03': 2643}, {'D04': 1757}, {'D05': 3052}, {'D06': 2703}, {'D07': 3289}, {'D08': 3750}, {'G01': 12162}, {'G02': 7779}, {'G03': 5215}, {'G04': 7960}, {'G05': 7256}],
 'YL': [{'C15': 0}, {'C14': 2770}, {'C13': 3734}, {'C12': 3453}, {'C10': 8605}, {'C09': 2939}, {'C08': 4068}, {'C07': 3216}, {'F03': 12524}, {'F02': 2950}, {'F01': 1879}, {'E01': 2985}, {'E02': 2527}, {'E03': 2555}, {'E04': 4715}, {'E05': 4717}, {'E06': 8348}]}