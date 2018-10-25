import re

import csv
with open ('RF_Contributor_Metadata.csv','r') as f:
    reader = csv.reader(f)


    for row in reader:
        next(reader, None)  #Need this to get past header row
        caption1 = row[9]
        keyword1 = row[10]


        if 'beach' in str(caption1) and 'sand' in str(keyword1) and 'coast' in str(keyword1):
            print(row[0], 'beach image'), "/n"

            print(count(beachpics))
