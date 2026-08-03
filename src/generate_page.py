import os
from markdown_blocks import markdown_to_html_node
from extract_title import extract_title



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'.")
    with open(from_path,"r") as f:
        md_contents = f.read()
    with open(template_path, "r") as g:
        template = g.read()

    html_node = markdown_to_html_node(md_contents)
    html_string = html_node.to_html()
    title = extract_title(md_contents)

    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
       os.makedirs(dest_dir, exist_ok = True)
       
    with open(dest_path, "w") as h:
     h.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    items =  os.listdir(dir_path_content)
    for item in items:
        item_full_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_full_path):
           html_filename = item.replace (".md", ".html")
           item_dest_path = os.path.join(dest_dir_path, html_filename)
           generate_page(item_full_path, template_path,item_dest_path)
        else:
           item_dest_path = os.path.join(dest_dir_path, item)
           generate_pages_recursive(item_full_path, template_path, item_dest_path)
