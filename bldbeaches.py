import re

import csv
with open ('RF_Contributor_Metadata.csv','r') as f:
    reader = csv.reader(f)

    beachpics = []
    for row in reader:
        next(reader, None)  #Need this to get past header row
        caption1 = row[9]
        keyword1 = row[10]


        if 'beach' in str(caption1) and 'sand' in str(keyword1):
            filename = row[0]
            image_loc = row[7]
            file_and_loc = filename, image_loc
            beachpics.append(file_and_loc)
            # beachpics.append(row)

            #print(row[0], 'beach image'), "/n"   #for filenames only

    print(len(beachpics))
    #print(beachpics)


with open ('filenames.BLbeachpics.csv', 'w', newline='') as csvfile:  #newline eliminates extra blank lines after each entry

    #headers = ['Filename', 'Photographer', 'Digital', 'Color','H/V', 'Date', 'Location', 'Release', 'Caption', 'Keywords', 'Photograph', 'Origin']
    headers = ['Filename', 'Location']
    writer = csv.writer(csvfile)


    writer.writerow(headers)

    for beachpics_meta in beachpics:

        writer.writerow(beachpics_meta)
