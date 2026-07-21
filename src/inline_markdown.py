from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        sections =  node.text.split(delimiter)
        if len(sections) %2 == 0:
            raise Exception ("Invalid markdown: missing matching delimeter")
        for i in range (len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                even = TextNode(sections[i], TextType.PLAIN)
                new_nodes.append(even)
            else:
                odd = TextNode(sections[i], text_type)
                new_nodes.append(odd)
    return new_nodes
