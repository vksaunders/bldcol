import os
import shutil
import csv


with open ('filenames.BLmountainpics.csv','r') as f:
    reader = csv.reader(f)
    next(reader, None)

    for row in reader:
         #print(row)

        valid_files = row[0]+'.jpg'

        full_name_src = "\\Users\\Valerie\\Documents\\GitHub\\bldcol\\Sourcejpg" + valid_files
        full_name_dest = "\\Users\\Valerie\\Documents\\GitHub\\bldcol\\Destjpg" + valid_files

        try:
            shutil.copy(full_name_src, full_name_dest)

         #print(valid_files)

        except FileNotFoundError as fnf_error:
            print(fnf_error)
            continue
