

import os

dir_name = #enter path  here as a raw string

#Insert newfile names here as strings, if your file name has an extension just append the extension at the end of every item in the list
#for example I want to name a folder of videos from 1 to 10, my list would be [str(i) + ".mp4" for i in range(1,11)]
newnames_list = []

for index,file in enumerate(os.listdir(dir_name)): 

    original_name = os.path.join(dir_name, file)
    new_name = os.path.join(dir_name, newnames_list[index])
    os.rename(original_name, new_name)
    
