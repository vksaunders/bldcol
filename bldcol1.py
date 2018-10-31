import re

import csv
with open ('RF_Contributor_Metadata.csv','r') as f:
    reader = csv.reader(f)

    beachpics = []
    for row in reader:
        next(reader, None)  #Need this to get past header row
        caption1 = row[9]
        keyword1 = row[10]


        if 'beach' in str(caption1) and 'sand' in str(keyword1) and 'coast' in str(keyword1):

            beachpics.append(row)

            #print(row[0], 'beach image'), "/n"   #for filenames only


    print(len(beachpics))

    for row in beachpics:     #for full rows of metadata
        filename = row[0]
        image_loc = row[7]
        beachpics_meta = filename, image_loc

        #print(beachpics_meta)
        #for beachpics_meta in beachpics:
        #    writer.writerow(beachpics_meta)



    headers = ['Filename', 'Location']
    with open ('filenames.BLbeachpics.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerow(beachpics_meta)
