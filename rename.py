

import os

def rename(dir_name,newnames_list):
"""
dir_name = #enter path  here as a raw string
Example: r"C:\Users\Fardin\Desktop\Coop\datasets\google_videos\drowning"

Insert newfile names here as strings in an iterable, if your file name has an extension just append the extension at the end of every item in the list
Example: I want to name a folder of videos from 1 to 10, my list would be [str(i) + ".mp4" for i in range(1,11)]

"""
    for index,file in enumerate(os.listdir(dir_name)): 

        original_name = os.path.join(dir_name, file)
        new_name = os.path.join(dir_name, newnames_list[index])
        os.rename(original_name, new_name)
        
if __name__ == "__main__":
    rename(#your_dir_name,#your_newnames_list)
    
    
