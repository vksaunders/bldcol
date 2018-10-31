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

            tourismpics.append(row)

            #print(row[0], 'beach image'), "/n"   #for filenames only


    print(len(tourismpics))



    for row in tourismpics:     #for full rows of metadata
        filename = row[0]
        image_loc = row[7]

        tourismpics_meta = filename, image_loc
        #print(tourismpics_meta)

for tourismpics_meta in tourismpics:
    headers = ['Filename', 'Location']
    with open ('tourismpics.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerow(tourismpics_meta)

#headers = ['Filename', 'Location']
#with open ('tourismpics.csv', 'w') as csvfile:
#    writer = csv.writer(csvfile)
#    writer.writerow(headers)
