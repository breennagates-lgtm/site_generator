from enum import Enum
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes



class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
 
def block_to_block_type(block):
    if block.startswith(("# ","## ","### ","#### ", "##### ","###### ")):
        return BlockType.HEADING
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        lines = block.split("\n")
        is_quote = True
        for line in lines:
            if not line.startswith(">"):
                is_quote = False
                break
        if is_quote:
            return BlockType.QUOTE
    if block.startswith("- ") or block.startswith("* "):
        lines = block.split("\n")
        is_unordered = True
        for line in lines:
            if not (line.startswith("- ") or line.startswith("* ")):
                is_unordered = False
                break
        if is_unordered:
            return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        lines = block.split("\n")
        is_ordered = True
        number=1
        for line in lines:
            if not line.startswith(f"{number}. "):
                is_ordered = False
                break
            number +=1 
        if is_ordered:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

    
    

def markdown_to_blocks(markdown):
    result = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        stripped = block.strip()
        if stripped != "":
            result.append(stripped)
    return result

#turns a block into a list of children nodes, which are html nodes
def text_to_children (text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        HTML_node = text_node_to_html_node(node)
        children.append(HTML_node)
    return children



def markdown_to_html_node(markdown):
    #create the blocks
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    #determine the types of each block
    for block in blocks:
        block_type = block_to_block_type(block)

        # if/elif for each type of block, and create the corresponding html node
        if block_type == BlockType.PARAGRAPH:
            block = block.replace("\n", " ")
            children = text_to_children(block)
            html_node = ParentNode("p", children)

        elif block_type == BlockType.HEADING:
            hash_count = 0
            for char in block:
                if char == "#":
                    hash_count += 1
                else:
                    break
            text = block[hash_count + 1:]
            children = text_to_children(text)
            html_node = ParentNode(f"h{hash_count}", children)  

        elif block_type == BlockType.CODE:
            stripped = block.strip('```\n')
            text_node = TextNode(stripped, TextType.PLAIN)
            code_node = text_node_to_html_node(text_node)
            html_node = ParentNode("pre", [code_node])
            
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
               line = line.strip("> ")
               new_lines.append(line)
            text = " ".join(new_lines)
            children = text_to_children(text)
            html_node = ParentNode("blockquote", children)


        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            html_children = []
            for line in lines:
                stripped = line[2:]
                children = text_to_children(stripped)
                li_node= ParentNode("li", children)
                html_children.append(li_node)
            html_node = ParentNode("ul", html_children)



            
        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            html_children = []
            for line in lines:
                space_index = line.find(". ")
                stripped = line[space_index + 2:]
                children = text_to_children(stripped)
                ol_node = ParentNode("li", children)
                html_children.append(ol_node)
            html_node = ParentNode("ol", html_children)

        block_nodes.append(html_node)

    #wrapping the block nodes in a parent div node
    return ParentNode("div", block_nodes)