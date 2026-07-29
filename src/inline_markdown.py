from textnode import TextNode, TextType
import re

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


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches =re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        images= extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for image_alt, image_link in images:
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            image= TextNode(image_alt, TextType.IMAGE, image_link)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
            new_nodes.append(image)
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN))
    return new_nodes


            


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        links= extract_markdown_links(old_node.text)
        if not links:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for ink_text, link_url in links:
            sections = original_text.split(f"[{link_text}]({link_url})", 1)
            link_node= TextNode(ink_text, TextType.LINK, link_url)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
            new_nodes.append(link_node)
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.PLAIN)]
    #pass through all TextType options
    nodes = split_nodes_delimiter(nodes, "**" , TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_" , TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`" , TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes