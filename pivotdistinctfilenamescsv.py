#Write one CSV that has all filenames with no duplicates--to see total number of distinct files found

import csv

with open('allBlendcollections.csv','r') as in_file:

    data_captured = csv.reader(in_file)
    filename = []
    for line in data_captured:
        if line[0] not in filename:
            filename.append(line)

        else:
            pass


        # for all_filenames in filename:
        #     out_file.write(all_filenames)

with open ('indivfilenames.csv', 'w', newline='') as csvfile:  #newline eliminates extra blank lines after each entry

    #headers = ['Filename', 'Photographer', 'Digital', 'Color','H/V', 'Date', 'Location', 'Release', 'Caption', 'Keywords', 'Photograph', 'Origin']
    #headers = ['Filename', 'Location']
    writer = csv.writer(csvfile)


    #writer.writerow(headers)

    for all_filenames in filename:

        writer.writerow(all_filenames)


# DataCaptured = csv.reader(DataFile, delimiter=',', skipinitialspace=True)
#
# Category, Year = [], []
# for row in DataCaptured:
#     if row[0] not in Year:
#         Year.append(row[0])
#     if row[1] not in Category:
#         Category.append(row[1])
