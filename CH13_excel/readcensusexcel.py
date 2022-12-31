#readcensusexcel.py -- tabulates population and number of census tracts for each county

import openpyxl, pprint

def main():
    print('Opening workbook')
    wb = openpyxl.load_workbook('censuspopdata.xlsx')
    sheet = wb['Population by Census Tract']

    #structure data as county_data[state abbrev][county]['tracts] and
    # county_data[state abbrev][county]['pop']
    county_data = {}

    print('Tabulating data...')
    for row in range(2, sheet.max_row + 1):
        #each column in the spreadsheet has data for one census tract
        state = sheet['B' + str(row)].value
        county = sheet['C' + str(row)].value
        pop = sheet['D' + str(row)].value

        #make sure key for the state exists
        county_data.setdefault(state, {})
        #make sure key for the county in this state exists
        county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})

        #each row represents one census tract, so increment by one
        county_data[state][county]['tracts'] += 1
        #increase the county pop by the pop in the census tract
        county_data[state][county]['pop'] += int(pop)

    print('Writing results...')
    with open('census2010.py', 'w') as output_file:
        output_file.write('allData = ' + pprint.pformat(county_data))
    print('Done!')

main()