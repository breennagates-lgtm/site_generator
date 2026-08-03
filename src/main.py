from textnode import TextNode, TextType
from copy_contents import copy_contents_of_directory
import shutil
from generate_page import generate_pages_recursive
import os
import sys


def main():
    #check commmand to see what directory to use?
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"



    # Create a TextNode instance
    text_node = TextNode("Hello, World!", text_type=TextType.BOLD, url="https://example.com")

    # Print the TextNode instance
    print(text_node)   


    source_dir = "./static"
    destination_dir = "./docs" 

    #deleting public directory if it exists
    if os.path.exists(destination_dir):
        print(f"Deleting '{destination_dir}' directory")
        shutil.rmtree(destination_dir)
   

    #copy everythign recursively
    print(f"Copying files from'{source_dir}' to '{destination_dir}'")
    copy_contents_of_directory(source_dir, destination_dir)

    generate_pages_recursive("content", "template.html", "docs", basepath)
   

main()