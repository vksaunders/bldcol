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


with open ('filenames.BLtouristattr.csv', 'w', newline='') as csvfile:  #newline eliminates extra blank lines after each entry

    headers = ['Filename', 'Photographer', 'Digital', 'Color','H/V', 'Date', 'Location', 'Release', 'Caption', 'Keywords', 'Photograph', 'Origin']
    writer = csv.writer(csvfile)
    # filename = row[0]
    # image_loc = row[7]

    writer.writerow(headers)


    for tourismpics_meta in tourismpics:
        #tourismpics_meta = filename, image_loc
        writer.writerow(tourismpics_meta)

# with open ('filenames.BLtouristattr.csv','r') as f:
#     reader = csv.reader(f)
#
#     for row in reader:
#         next(reader,None)
#         filename = row[0]
#         image_loc = row[7]
#         tourism_list = filename, image_loc
#
# with open ('tourismlist.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#
#     headers = ['Filename', 'Location']
#
#     writer.writerow(headers)
#
#     filename = row[0]
#     image_loc = row[7]
#     tourism_list = filename, image_loc
#
#     for toursim_list in tourismpics:
#         writer.writerow(toursim_list)
