# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 02:20:32 2021

@author: Fardin
"""

import os

dir_name = #enter path  here as a raw string

#Insert newfile names here as strings, if your file name has an extension just append the extension at the end
newnames_list = []

for index,file in enumerate(os.listdir(dir_name)): 


    original_name = os.path.join(dir_name, file)
    new_name = os.path.join(dir_name, #insert your iterable item here)
    os.rename(original_name, new_name)
    
"""
Example:
    
import os

dir_name = r'C:\Users\Fardin\Desktop\Coop\datasets\google_videos\Under_water\drowning'

i = 15

for file in os.listdir(dir_name): 

    i += 1
    original_name = os.path.join(dir_name, file)
    new_name = os.path.join(dir_name, str(i)+".mp4")
    os.rename(original_name, new_name)
    
"""