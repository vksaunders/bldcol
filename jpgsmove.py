import os
import shutil
import csv



dir_src = ("\\Users\\Valerie\\Documents\\GitHub\\bldcol\\Sourcejpg")
dir_dst = ("\\Users\\Valerie\\Documents\\GitHub\\bldcol\\Destjpg")



for f in os.listdir(dir_src):
    src_file = os.path.join(dir_src, f)
    dst_file = os.path.join(dir_dst, f)
    shutil.move(src_file, dst_file)
