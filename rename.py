

import os

dir_name = #enter path  here as a raw string

#Insert newfile names here as strings, if your file name has an extension just append the extension at the end of every item in the list
newnames_list = []

for index,file in enumerate(os.listdir(dir_name)): 

    original_name = os.path.join(dir_name, file)
    new_name = os.path.join(dir_name, newnames_list[index])
    os.rename(original_name, new_name)
    
