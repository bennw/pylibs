import math
import os
import shutil
import sys
import time

# e.g. expand_numbers("5,8-11,15")
# output = [5, 8, 9, 10, 11, 15]
def expand_numbers(str):
    res = []
    for token in str.split(","):
        r = token.split("-")
        if len(r) == 1:
            res.append(int(r[0]))
        elif len(r) == 2:
            for i in range(int(r[0]), int(r[1])+1):
                res.append(i)
        else:
            raise Exception("Invalid numerical string")
    return res
    
# e.g. make_percentage(1/3, dp=4)
# output = 33.3333
def make_percentage(p, dp=2):
    m = 10 ** dp
    return math.floor(p*100*m)/m
    
# doesn't move/copy if file already exists in dest
# also makes directory
def move(src, dest, is_dest_parent=True, copy=False):
    p = dest if is_dest_parent else os.path.dirname(dest)
    if p and not os.path.exists(p):
        os.makedirs(p, exist_ok=True)
    d = os.path.join(p, os.path.basename(src)) if is_dest_parent else os.path.join(p, os.path.basename(dest))
    if not os.path.exists(d):
        if copy:
            if os.path.isdir(src):
                shutil.copytree(src, d)
            else:
                shutil.copy(src, d)
        else:
            shutil.move(src, d)
def copy(src, dest, is_dest_parent=True):
    move(src, dest, is_dest_parent=is_dest_parent, copy=True)
        
# usage: for (fname, fullpath) in enum_dir("C:/"):
def enum_dir(folder):
    for subdir, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(subdir, file)
            yield file, file_path
            
# iterate each line in text file, newlines already stripped
def enum_file(txtfile):
    with open(txtfile, "r") as f:
        for line in f:
            l = line.strip("\r\n")
            yield l
            
def test():
    pass
        
if __name__ == "__main__":
    test()