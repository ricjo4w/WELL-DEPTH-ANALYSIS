import csv
from geopy.geocoders import Nominatim
from tqdm import tqdm


def getState(address):
    # Returns the state that an address is in
    allStates = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    for state in allStates:
        if state in address:
            return state


geolocator = Nominatim(user_agent="coordinateconverter")

# open the input and output files
with open('data.csv', 'r') as infile, open('output.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # read in the header row and add the new column name
    header = next(reader)
    header.append('Address')
    writer.writerow(header)

    # iterate over each row and the address of the well
    for row in tqdm(reader, desc='Processing items', unit='item'):
        location = geolocator.reverse(row[0] + ',' + row[1])
        value = ''
        try:
            value = getState(location.address)
        except:
            value = 'Other'
            pass
        row.append(value)
        writer.writerow(row)

    print('File updated successfully!')
