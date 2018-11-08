import os
import shutil
import csv



with open ('filenames.BLtouristattr.csv','r') as f:
    reader = csv.reader(f)
    next(reader, None)

    for row in reader:
         #print(row)

        valid_files = row[0]+'.jpg'

        full_name = "\\Users\\Valerie\\Documents\\GitHub\\bldcol\\bldthumbs\\" + valid_files
        full_name_dest = "\\Users\\Valerie\\Documents\\GitHub\\bldcol\\tourismpics\\" + valid_files

        try:
            shutil.copy(full_name, full_name_dest)

         #print(valid_files)

        except FileNotFoundError as fnf_error:
            print(fnf_error)
            continue

# except FileNotFoundError as fnf_error:
#     print(fnf_error)

# dir_src = ("\\Users\\Valerie\\Documents\\GitHub\\bldcol\\bldthumbs")
# dir_dst = ("\\Users\\Valerie\\Documents\\GitHub\\bldcol\\tourismpics")
#
# for f in os.listdir(dir_src):
#     if f in valid_files:
#         src_file = os.path.join(dir_src, f)
#         dst_file = os.path.join(dir_dst, f)
#         shutil.copy(src_file, dst_file)
