import csv

with open ('RF_Contributor_Metadata.csv','r') as f:
    reader = csv.reader(f)

    landmarkpics = []
    for row in reader:
        next(reader, None)  #Need this to get past header row
        caption1 = row[9]
        keyword1 = row[10]


        if 'landmark' in str(keyword1) and 'historical place' in str(keyword1):
            filename = row[0]
            image_loc = row[7]
            file_and_loc = [filename, image_loc]
            landmarkpics.append(file_and_loc)


#Use this to write all rows of metadata for selected condition
        # if 'landmark' in str(keyword1):
        #
        #     landmarkpics.append(tourismpics)

    print(len(landmarkpics))
    #print(landmarkpics)
#
# with open ('filenames.BLlandmarkpics.csv', 'w', newline='') as csvfile:  #newline eliminates extra blank lines after each entry
#
#     #headers = ['Filename', 'Photographer', 'Digital', 'Color','H/V', 'Date', 'Location', 'Release', 'Caption', 'Keywords', 'Photograph', 'Origin']
#     headers = ['Filename', 'Location']
#     writer = csv.writer(csvfile)
#
#
#     writer.writerow(headers)
#
#     for landmarkpics_meta in landmarkpics:
#
#         writer.writerow(landmarkpics_meta)
