from enum import Enum

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
    if block.startswith("- "):
        lines = block.split("\n")
        is_unordered = True
        for line in lines:
            if not line.startswith("- "):
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
