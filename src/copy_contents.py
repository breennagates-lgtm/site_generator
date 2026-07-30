import os
import shutil


def copy_contents_of_directory(source_dir, destination_dir):

    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)


    list= os.listdir(source_dir)

    for item in list:
        src_path = os.path.join(source_dir, item)
        dest_path = os.path.join(destination_dir, item)
        if os.path.isdir(src_path):
            copy_contents_of_directory(src_path, dest_path)
        elif os.path.isfile(src_path):
            print(f"copying {src_path} --> {dest_path}")
            shutil.copy(src_path, dest_path)

    

    
