import unittest

from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType

def test_all(self):
    node = "This is **bold** and _italic_ with `code` and an ![image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    new_nodes = text_to_textnodes(node)
    self.assertEqual(
        [
            TextNode("This is ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" with ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ],
        new_nodes
    )

def test_plain_text(self):
    node = "This is plain text with no formatting"
    new_nodes = text_to_textnodes(node)
    self.assertEqual(
        [
            TextNode("This is plain text with no formatting", TextType.PLAIN),
        ],
        new_nodes
    )

def test_multiple_same_delimiters(self):
    node = "This is **bold** and **another bold**"
    new_nodes = text_to_textnodes(node)
    self.assertEqual(
        [
            TextNode("This is ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.PLAIN),
            TextNode("another bold", TextType.BOLD),
        ],
        new_nodes
    )

def test_no_input(self):
    node = ""
    new_nodes = text_to_textnodes(node)
    self.assertEqual(
        [
            TextNode("", TextType.PLAIN),
        ],
        new_nodes
    )

def test_missing_link_text(self):
    node = "This is a [](https://boot.dev) with no link text"
    new_nodes = text_to_textnodes(node)
    self.assertEqual(
        [
            TextNode("This is a ", TextType.PLAIN),
            TextNode("", TextType.LINK, "https://boot.dev"),
            TextNode(" with no link text", TextType.PLAIN),
        ], new_nodes
    )
        
