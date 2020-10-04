
# read files from path and print set lines file-by-file
import re

from os import listdir
from os.path import isfile, join


def task_3(path):
    allfiles = [f for f in listdir(path) if isfile(join(path, f))]
    
    file_number = 0
    max_line_number = 0
    line_mem = []
    i_iter = []
    
    # read all files from path, find max number of lines
    for f in allfiles:
        line_num = len(re.findall(r"[\n']+?", open(path+f).read())) + 1
        
        if max_line_number < line_num:
            max_line_number = line_num
        line_mem.append(line_num)
    
    # generate matrix of idexes for further line-by-line open    
    mas = [[0] * len(allfiles) for i in range(max_line_number)]
    
    # fill matrix by right-order-read indexes
    for i in range(len(allfiles)):
        for l in range(line_mem[i]): # build massive iter massive
            i_iter.append(l)
        
        loc_iter = i_iter*max_line_number  # [0,1] -> [0,1,0,1,...n]
        loc_iter = loc_iter[:max_line_number]
        i_iter.clear()    
        for j in range(max_line_number):
            mas[j][i] = loc_iter[j]
            
    file_names = listdir(path)
    
    # print opened file in needed order
    for i in range(max_line_number): #go by line
        for j in range(len(allfiles)):  # go by file
            loc_file = open(path+file_names[j],'r')
            z = loc_file.readlines()[mas[i][j]]        
            print(z)
        print('-----------')  



path = './data/'
task_3(path)