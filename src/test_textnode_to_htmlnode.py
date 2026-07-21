import unittest
from textnode import TextNode, TextType, text_node_to_html_node


def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

def test_bold(self):
    node = TextNode("This is a bold text node", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "This is a bold text node")

def test_italic(self):
    node = TextNode("This is an italic text node", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "i")
    self.assertEqual(html_node.value, "This is an italic text node")

def test_code(self):
    node = TextNode("This is a code text node", TextType.CODE)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.value, "This is a code text node")

def test_image(self):
    node = TextNode("This is an image text node", TextType.IMAGE, url="https://example.com/image.jpg")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(html_node.props, {"src": "https://example.com/image.jpg", "alt": "This is an image text node"})

def test_link(self):
    node = TextNode("This is a link text node", TextType.LINK, url="https://example.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "This is a link text node")
    self.assertEqual(html_node.props, {"href": "https://example.com"})

def test_unsupported_text_type(self):
    node = TextNode("This is an unsupported text node", TextType.COMIC_SANS)
    with self.assertRaises(ValueError):
        text_node_to_html_node(node)

def test_empty_text(self):
    node = TextNode("", TextType.PLAIN)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "")

def test_none_text(self):
    node = TextNode(None, TextType.PLAIN)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, None)

def test_none_url_for_image(self):
    node = TextNode("This is an image text node", TextType.IMAGE, url=None)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(html_node.props, {"src": None, "alt": "This is an image text node"})