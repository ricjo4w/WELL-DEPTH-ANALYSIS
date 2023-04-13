import csv

'''
  Author: John Rice
  Purpose: This script opens a file pullled from USGS Groundwater Data for the Nation that does not have a traditional format. To comabt
           this each well listed in the file is interpreted and its relating data is added as a row in a csv file that is outputted called
           depthMapDeepest.csv
'''

# Define header
header = ['Latitude', 'Longitude', 'Depth to water (ft)', 'lastLoc']

# Open file and read lines
with open("dv", "r") as file1:
    lines = file1.readlines()

    # Get number of entries
    lengthString = lines[15]
    length = lengthString[25:29]
    print('Number of Entries:', length)
    entryCount = int(length)

    lastDepth = -500
    lastLoc = ''

    # Create output csv file and write header
    with open('depthMapDeepest.csv', 'w+', encoding='UTF8', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(header)

        # Iterate through lines and extract data
        for line in lines:
            if '2021-11-25' in line:
                latDeg = float(line[5:7])
                latMin = float(line[7:9])
                latSec = float(line[9:11])
                latitude = latDeg + (latMin * (1/60)) + (latSec * (1/3600))
                location = line[5:18]

                lonDeg = float(line[11:14])
                lonMin = float(line[14:16])
                lonSec = float(line[16:18])
                longitude = (lonDeg + (lonMin * (1/60)) + (lonSec * (1/3600))) * (-1)

                start = line.find("2021-11-25	") + len("2021-11-25	")
                end = line.find("	P")
                substring = line[start:end]

                if substring not in ['Eqp', '***', 'Dis']:
                    depth = float(substring)
                    data = [latitude, longitude, depth, (lastLoc + 'd')]

                    if location == lastLoc:
                        if lastDepth < depth:
                            lastDepth = depth
                            writer.writerow(data)
                    else:
                        writer.writerow(data)
                        lastDepth = -500

                    lastLoc = location
