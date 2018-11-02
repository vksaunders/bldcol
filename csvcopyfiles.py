import os
import shutil
import csv


with open ('testlist.csv','r') as f:
     reader = csv.reader(f)
     for row in reader:
         next(reader, None)
         print(row)

valid_files = row[0]
print(valid_files)

dir_src = ("\\Users\\Valerie\\Documents\\GitHub\\bldcol\\Sourcejpg")
dir_dst = ("\\Users\\Valerie\\Documents\\GitHub\\bldcol\\Destjpg")

for f in os.listdir(dir_src):
    if f in valid_files:
        src_file = os.path.join(dir_src, f)
        dst_file = os.path.join(dir_dst, f)
        shutil.copy(src_file, dst_file)
