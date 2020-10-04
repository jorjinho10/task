# convert input time to seconds

import pytest
import sys
import re

def test_task_1():
    input = '60.5m'
    if input == '':
        print('Exception raised')
        sys.exit()
    
    input = input.replace(',','.')
    
    check1 = re.match('^[0-9]*[smhd]{1}$', input)  # 2h pattern
    check2 = re.match('^[0-9]*[.][0-9]*[smhd]{1}$', input) #2.3h pattern
    check3 = re.match('^[0-9]*$', input) #2 pattern
    check4 = re.match('^[0-9]*[.][0-9]*$', input) #2.3 pattern
    
    if check1 or check2 or check3 or check4:
        
        length = len(input)
        time = ['s','m','h','d']
        mult = [1,60,3600,86400]
        
        
        check = 0
        
        for i in range(len(time)):
            if 0<= input.find(time[i],0,length) == length-1: # check that timesymbol is last in string
                f = input.split(time[i])
                if length == 1: #case of "s" input with no value
                    z = 1*mult[i]
                else: # normal behavior
                    z = float(f[0])*mult[i]
                check = 1
                break
            
        if check == 0:
            z = float(input)
             
        print('-----------------------------')
        print('Input value in seconds = ', z)
    else:
        print('Exception raised')
        sys.exit()
    
    if z == 3630.0:
        pass

   
# print("Hello, please write data to be converted and press 'ENTER' ")
# print('Supported input time formats are: "s","m","h","d".')
# print('For instance to convert 5 hours to seconds enter "5h"')
# input = '60.5m'
# test_task_1('60.5m')