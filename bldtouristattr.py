import re

import csv
with open ('RF_Contributor_Metadata.csv','r') as f:
    reader = csv.reader(f)

    tourismpics = []
    for row in reader:
        next(reader, None)  #Need this to get past header row
        caption1 = row[9]
        keyword1 = row[10]


        if 'tourist attraction' in str(keyword1):
            filename = row[0]
            image_loc = row[7]
            file_and_loc = [filename, image_loc]
            tourismpics.append(file_and_loc)


#Use this to write all rows of metadata for selected condition
        # if 'tourist attraction' in str(keyword1):
        #
        #     tourismpics.append(tourismpics)

    print(len(tourismpics))


with open ('filenames.BLtouristattr.csv', 'w', newline='') as csvfile:  #newline eliminates extra blank lines after each entry

    #headers = ['Filename', 'Photographer', 'Digital', 'Color','H/V', 'Date', 'Location', 'Release', 'Caption', 'Keywords', 'Photograph', 'Origin']
    headers = ['Filename', 'Location']
    writer = csv.writer(csvfile)


    writer.writerow(headers)

    for tourismpics_meta in tourismpics:

        writer.writerow(tourismpics_meta)
