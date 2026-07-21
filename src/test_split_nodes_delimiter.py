import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

def test_delim_code(self):
    node = TextNode("This is text with a `code block` word", TextType.PLAIN)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
    self.assertEqual(
       [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.PLAIN),
        ],
        new_nodes
     )

def test_multi_delim_code(self):
    node = TextNode("This has `code` and `more code` in it", TextType.PLAIN)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    self.assertEqual(
        [
            TextNode("This has ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode(" and ",TextType.PLAIN),
            TextNode("more code", TextType.CODE),
            TextNode(" in it", TextType.PLAIN),
        ],
            new_nodes
    )

def test_delim_bold(self):
    node = TextNode("This is text with a **bold word** inside", TextType.PLAIN)
    new_nodes = split_nodes_delimiter([node], "**", TextType.PLAIN)

    self.assertEqual(
        [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("bold word", TextType.BOLD),
            TextNode(" inside", TextType.PLAIN),
        ],
            new_nodes
    )

def test_delim_end(self):
    node = TextNode("This is text with a **bold word**", TextType.PLAIN)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

    self.assertEqual(
        [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("bold word", TextType.BOLD),
        ],
            new_nodes
    )

def test_delim_start(self):
    node = TextNode("**bold word** is at the start", TextType.PLAIN)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

    self.assertEqual(
        [
            TextNode("bold word", TextType.BOLD),
            TextNode(" is at the start", TextType.PLAIN),
        ],
            new_nodes
    )   

def test_delim_missing(self):
    node = TextNode("This is text with a **bold word inside", TextType.PLAIN)
    with self.assertRaises(Exception):
        split_nodes_delimiter([node], "**", TextType.BOLD)

def test_delim_only(self):
    node = TextNode("**bold word**", TextType.PLAIN)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

    self.assertEqual(
        [
            TextNode("bold word", TextType.BOLD),
        ],
            new_nodes
    )


