import os
import shutil
import csv


# with open ('testlist.csv','r') as f:
#     reader = csv.reader(f)
#
#     for row in reader:
#         next(reader,None)
#         name =row[0]
#         print(name)

    # for row in reader:
    #     next(reader,None)
    #     name = row[0]
    #     loc = row[7]
    #
    #     loc_list = name, loc
    #
    #     print(loc_list)

dir_src = ("\\Users\\Valerie\\Documents\\GitHub\\bldcol\\Sourcejpg")
dir_dst = ("\\Users\\Valerie\\Documents\\GitHub\\bldcol\\Destjpg")

# for f in os.listdir(dir_src):
#     if f.endswith(".jpg"):
#         shutil.move(source + f, destination)

for f in os.listdir(dir_src):
    src_file = os.path.join(dir_src, f)
    dst_file = os.path.join(dir_dst, f)
    shutil.copy(src_file, dst_file)

# import shutil, os
# source = r"C:\Project\layers"
# destination = r"C:\Project\layers\new"
# if not os.path.exists(destination):
#     os.makedirs(destination)
# for f in os.listdir(source):
#     if f.endswith(".jpg"):
#         shutil.move(source + f, destination)
#


 # keys=[]
 # with open('filenames.BLtouristattr.csv', 'r') as f:
 #     reader = csv.reader(f)
 #     for row in reader:
 #        filenames = keys[0]
 #        #keys[rowDict[0]] = rowDict[1]
 #        print(filenames)  # if desired
#
# valid_files = set(keys.values())  # file names found in csv
# dir_src = 'C:\\Users\\Willie\\Desktop\\Suppliers Dropship\\hunting\\'
# dir_dst = 'C:\\image\\'
# for file in os.listdir(dir_src):
#     if file in valid_files:
#         src_file = os.path.join(dir_src, file)
#         dst_file = os.path.join(dir_dst, file)
#         shutil.move(src_file, dst_file)
