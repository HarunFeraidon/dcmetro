ERROR_CONN = "Error: connection is broken"
ERROR_FROM_TO = "Error: please follow a 'from' start 'to' end format"
ERROR_DUPLICATE_LOCATIONS = "Error: please do not enter duplicate locations"
ERROR_EMPTY_LOCATION = "Error: please enter a 'from' location and a 'to' location"
ERROR_FROM_LOCATION = "'From' location not recognized"
ERROR_TO_LOCATION = "'To' location not recognized"
ERROR_LOCATION_NOT_RECOGNIZED = "Location not recognized"

query_when = "when"
query_length = "length"
query_path = "path"

LINE_CODES = {
    'Red': 'RD',
    'Yellow': 'YL',
    'Green': 'GR',
    'Blue': 'BL',
    'Orange': 'OR',
    'Silver': 'SV',
}

STATION_CODES = {
    'metro center': 'C01',
    'farragut north': 'A02',
    'dupont circle': 'A03',
    'woodley park-zoo/adams morgan': 'A04',
    'cleveland park': 'A05',
    'van ness-udc': 'A06',
    'tenleytown-au': 'A07',
    'friendship heights': 'A08',
    'bethesda': 'A09',
    'medical center': 'A10',
    'grosvenor-strathmore': 'A11',
    'north bethesda': 'A12',
    'twinbrook': 'A13',
    'rockville': 'A14',
    'shady grove': 'A15',
    'gallery pl-chinatown': 'F01',
    'judiciary square': 'B02',
    'union station': 'B03',
    'rhode island ave-brentwood': 'B04',
    'brookland-cua': 'B05',
    'fort totten': 'E06',
    'takoma': 'B07',
    'silver spring': 'B08',
    'forest glen': 'B09',
    'wheaton': 'B10',
    'glenmont': 'B11',
    'noma-gallaudet u': 'B35',
    'mcpherson square': 'C02',
    'farragut west': 'C03',
    'foggy bottom-gwu': 'C04',
    'rosslyn': 'C05',
    'arlington cemetery': 'C06',
    'pentagon': 'C07',
    'pentagon city': 'C08',
    'crystal city': 'C09',
    'ronald reagan washington national airport': 'C10',
    'braddock road': 'C12',
    'king st-old town': 'C13',
    'eisenhower avenue': 'C14',
    'huntington': 'C15',
    'federal triangle': 'D01',
    'smithsonian': 'D02',
    "l'enfant plaza": 'F03',
    'federal center sw': 'D04',
    'capitol south': 'D05',
    'eastern market': 'D06',
    'potomac ave': 'D07',
    'stadium-armory': 'D08',
    'minnesota ave': 'D09',
    'deanwood': 'D10',
    'cheverly': 'D11',
    'landover': 'D12',
    'new carrollton': 'D13',
    'mt vernon sq 7th st-convention center': 'E01',
    'shaw-howard u': 'E02',
    'u street/african-amer civil war memorial/cardozo': 'E03',
    'columbia heights': 'E04',
    'georgia ave-petworth': 'E05',
    'west hyattsville': 'E07',
    'hyattsville crossing': 'E08',
    'college park-u of md': 'E09',
    'greenbelt': 'E10',
    'archives-navy memorial-penn quarter': 'F02',
    'waterfront': 'F04',
    'navy yard-ballpark': 'F05',
    'anacostia': 'F06',
    'congress heights': 'F07',
    'southern avenue': 'F08',
    'naylor road': 'F09',
    'suitland': 'F10',
    'branch ave': 'F11',
    'benning road': 'G01',
    'capitol heights': 'G02',
    'addison road-seat pleasant': 'G03',
    'morgan boulevard': 'G04',
    'downtown largo': 'G05',
    'van dorn street': 'J02',
    'franconia-springfield': 'J03',
    'court house': 'K01',
    'clarendon': 'K02',
    'virginia square-gmu': 'K03',
    'ballston-mu': 'K04',
    'east falls church': 'K05',
    'west falls church': 'K06',
    'dunn loring-merrifield': 'K07',
    'vienna/fairfax-gmu': 'K08',
    'mclean': 'N01',
    'tysons': 'N02',
    'greensboro': 'N03',
    'spring hill': 'N04',
    'wiehle-reston east': 'N06',
    'reston town center': 'N07',
    'herndon': 'N08',
    'innovation center': 'N09',
    'washington dulles international airport': 'N10',
    'loudoun gateway': 'N11',
    'ashburn': 'N12'
}

EACH_LINES_START_AND_END_STATION = {
    'BL': ('J03', 'G05'),
    'GR': ('F11', 'E10'),
    'OR': ('K08', 'D13'),
    'RD': ('A15', 'B11'),
    'SV': ('N12', 'G05'),
    'YL': ('C15', 'E06')
}

# swapped A01 -> C01 and B01 -> F01
# swapped B06 -> E06
# swapped D03 -> F03
EACH_LINES_DISTANCE_TO_PREVIOUS_STATION_LIST = {
    'BL': [['J03', 0], ['J02', 18695], ['C13', 20158], ['C12', 3453],
           ['C10', 8605], ['C09', 2939], ['C08', 4068], ['C07', 3216],
           ['C06', 7036], ['C05', 4936], ['C04', 6993], ['C03', 2783],
           ['C02', 2001], ['C01', 2359], ['D01', 1561], ['D02', 2016],
           ['F03', 2643], ['D04', 1757], ['D05', 3052], ['D06', 2703],
           ['D07', 3289], ['D08', 3750], ['G01', 12162], ['G02', 7779],
           ['G03', 5215], ['G04', 7960], ['G05', 7256]],
    'GR': [['F11', 0], ['F10', 9144], ['F09', 7658], ['F08', 6612],
           ['F07', 5508], ['F06', 6851], ['F05', 6254], ['F04', 3326],
           ['F03', 4158], ['F02', 2950], ['F01', 1879], ['E01', 2985],
           ['E02', 2527], ['E03', 2555], ['E04', 4715], ['E05', 4717],
           ['E06', 8348], ['E07', 10406], ['E08', 6670], ['E09', 10368],
           ['E10', 12981]],
    'OR': [['K08', 0], ['K07', 13165], ['K06', 12638], ['K05', 10918],
           ['K04', 13156], ['K03', 2980], ['K02', 2473], ['K01', 2687],
           ['C05', 5807], ['C04', 6993], ['C03', 2783], ['C02', 2001],
           ['C01', 2359], ['D01', 1561], ['D02', 2016], ['F03', 2643],
           ['D04', 1757], ['D05', 3052], ['D06', 2703], ['D07', 3289],
           ['D08', 3750], ['D09', 11080], ['D10', 4723], ['D11', 6149],
           ['D12', 9665], ['D13', 7655]],
    'RD': [['A15', 0], ['A14', 14151], ['A13', 10586], ['A12', 5895],
           ['A11', 7309], ['A10', 11821], ['A09', 5530], ['A08', 9095],
           ['A07', 4135], ['A06', 5841], ['A05', 3320], ['A04', 3740],
           ['A03', 6304], ['A02', 2487], ['C01', 4178], ['F01', 1505],
           ['B02', 1967], ['B03', 3446], ['B35', 3548], ['B04', 5771],
           ['B05', 4553], ['E06', 7378], ['B07', 10026], ['B08', 7484],
           ['B09', 8871], ['B10', 8484], ['B11', 9334]],
    'SV': [['N12', 0], ['N11', 10338], ['N10', 15145], ['N09', 10999],
           ['N08', 9095], ['N07', 7130], ['N06', 5961], ['N04', 30867],
           ['N03', 3634], ['N02', 3902], ['N01', 3440], ['K05', 24745],
           ['K04', 13156], ['K03', 2980], ['K02', 2473], ['K01', 2687],
           ['C05', 4936], ['C04', 6993], ['C03', 2783], ['C02', 2001],
           ['C01', 2359], ['D01', 1561], ['D02', 2016], ['F03', 2643],
           ['D04', 1757], ['D05', 3052], ['D06', 2703], ['D07', 3289],
           ['D08', 3750], ['G01', 12162], ['G02', 7779], ['G03', 5215],
           ['G04', 7960], ['G05', 7256]],
    'YL': [['C15', 0], ['C14', 2770], ['C13', 3734], ['C12', 3453],
           ['C10', 8605], ['C09', 2939], ['C08', 4068], ['C07', 3216],
           ['F03', 12524], ['F02', 2950], ['F01', 1879], ['E01', 2985],
           ['E02', 2527], ['E03', 2555], ['E04', 4715], ['E05', 4717],
           ['E06', 8348]]
}

EACH_LINES_DISTANCE_TO_PREVIOUS_STATION_DICT = {
    'BL': [{
        'J03': 0
    }, {
        'J02': 18695
    }, {
        'C13': 20158
    }, {
        'C12': 3453
    }, {
        'C10': 8605
    }, {
        'C09': 2939
    }, {
        'C08': 4068
    }, {
        'C07': 3216
    }, {
        'C06': 7036
    }, {
        'C05': 4936
    }, {
        'C04': 6993
    }, {
        'C03': 2783
    }, {
        'C02': 2001
    }, {
        'C01': 2359
    }, {
        'D01': 1561
    }, {
        'D02': 2016
    }, {
        'F03': 2643
    }, {
        'D04': 1757
    }, {
        'D05': 3052
    }, {
        'D06': 2703
    }, {
        'D07': 3289
    }, {
        'D08': 3750
    }, {
        'G01': 12162
    }, {
        'G02': 7779
    }, {
        'G03': 5215
    }, {
        'G04': 7960
    }, {
        'G05': 7256
    }],
    'GR': [{
        'F11': 0
    }, {
        'F10': 9144
    }, {
        'F09': 7658
    }, {
        'F08': 6612
    }, {
        'F07': 5508
    }, {
        'F06': 6851
    }, {
        'F05': 6254
    }, {
        'F04': 3326
    }, {
        'F03': 4158
    }, {
        'F02': 2950
    }, {
        'F01': 1879
    }, {
        'E01': 2985
    }, {
        'E02': 2527
    }, {
        'E03': 2555
    }, {
        'E04': 4715
    }, {
        'E05': 4717
    }, {
        'E06': 8348
    }, {
        'E07': 10406
    }, {
        'E08': 6670
    }, {
        'E09': 10368
    }, {
        'E10': 12981
    }],
    'OR': [{
        'K08': 0
    }, {
        'K07': 13165
    }, {
        'K06': 12638
    }, {
        'K05': 10918
    }, {
        'K04': 13156
    }, {
        'K03': 2980
    }, {
        'K02': 2473
    }, {
        'K01': 2687
    }, {
        'C05': 5807
    }, {
        'C04': 6993
    }, {
        'C03': 2783
    }, {
        'C02': 2001
    }, {
        'C01': 2359
    }, {
        'D01': 1561
    }, {
        'D02': 2016
    }, {
        'F03': 2643
    }, {
        'D04': 1757
    }, {
        'D05': 3052
    }, {
        'D06': 2703
    }, {
        'D07': 3289
    }, {
        'D08': 3750
    }, {
        'D09': 11080
    }, {
        'D10': 4723
    }, {
        'D11': 6149
    }, {
        'D12': 9665
    }, {
        'D13': 7655
    }],
    'RD': [{
        'A15': 0
    }, {
        'A14': 14151
    }, {
        'A13': 10586
    }, {
        'A12': 5895
    }, {
        'A11': 7309
    }, {
        'A10': 11821
    }, {
        'A09': 5530
    }, {
        'A08': 9095
    }, {
        'A07': 4135
    }, {
        'A06': 5841
    }, {
        'A05': 3320
    }, {
        'A04': 3740
    }, {
        'A03': 6304
    }, {
        'A02': 2487
    }, {
        'C01': 4178
    }, {
        'F01': 1505
    }, {
        'B02': 1967
    }, {
        'B03': 3446
    }, {
        'B35': 3548
    }, {
        'B04': 5771
    }, {
        'B05': 4553
    }, {
        'E06': 7378
    }, {
        'B07': 10026
    }, {
        'B08': 7484
    }, {
        'B09': 8871
    }, {
        'B10': 8484
    }, {
        'B11': 9334
    }],
    'SV': [{
        'N12': 0
    }, {
        'N11': 10338
    }, {
        'N10': 15145
    }, {
        'N09': 10999
    }, {
        'N08': 9095
    }, {
        'N07': 7130
    }, {
        'N06': 5961
    }, {
        'N04': 30867
    }, {
        'N03': 3634
    }, {
        'N02': 3902
    }, {
        'N01': 3440
    }, {
        'K05': 24745
    }, {
        'K04': 13156
    }, {
        'K03': 2980
    }, {
        'K02': 2473
    }, {
        'K01': 2687
    }, {
        'C05': 4936
    }, {
        'C04': 6993
    }, {
        'C03': 2783
    }, {
        'C02': 2001
    }, {
        'C01': 2359
    }, {
        'D01': 1561
    }, {
        'D02': 2016
    }, {
        'F03': 2643
    }, {
        'D04': 1757
    }, {
        'D05': 3052
    }, {
        'D06': 2703
    }, {
        'D07': 3289
    }, {
        'D08': 3750
    }, {
        'G01': 12162
    }, {
        'G02': 7779
    }, {
        'G03': 5215
    }, {
        'G04': 7960
    }, {
        'G05': 7256
    }],
    'YL': [{
        'C15': 0
    }, {
        'C14': 2770
    }, {
        'C13': 3734
    }, {
        'C12': 3453
    }, {
        'C10': 8605
    }, {
        'C09': 2939
    }, {
        'C08': 4068
    }, {
        'C07': 3216
    }, {
        'F03': 12524
    }, {
        'F02': 2950
    }, {
        'F01': 1879
    }, {
        'E01': 2985
    }, {
        'E02': 2527
    }, {
        'E03': 2555
    }, {
        'E04': 4715
    }, {
        'E05': 4717
    }, {
        'E06': 8348
    }]
}
