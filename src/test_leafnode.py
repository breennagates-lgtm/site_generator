import unittest
from htmlnode import LeafNode

def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

def test_leaf_to_html_a(self):
    node = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, "Just text")
    self.assertEqual(node.to_html(), "Just text")

def test_leaf_to_html_no_value(self):
    node = LeafNode("p", None)
    with self.assertRaises(ValueError):
        node.to_html()

def test_leaf_to_html_title(self):
    node = LeafNode("title", "My Page Title")
    self.assertEqual(node.to_html(), "<title>My Page Title</title>")

def test_leaf_to_html_bold(self):
    node = LeafNode("b", "Bold Text")
    self.assertEqual(node.to_html(), "<b>Bold Text</b>")

