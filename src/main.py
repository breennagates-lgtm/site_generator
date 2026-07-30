from textnode import TextNode, TextType
from copy_contents import copy_contents_of_directory
import shutil
import os

def main():
    # Create a TextNode instance
    text_node = TextNode("Hello, World!", text_type=TextType.BOLD, url="https://example.com")

    # Print the TextNode instance
    print(text_node)   


    source_dir = "./static"
    destination_dir = "./public" 

    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    os.mkdir(destination_dir)


    copy_contents_of_directory(source_dir, destination_dir)

   

main()