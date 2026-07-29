

def markdown_to_blocks(markdown):
    result = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        stripped = block.strip()
        if stripped != "":
            result.append(stripped)
    return result
