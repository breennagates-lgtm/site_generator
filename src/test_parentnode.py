
import unittest
from htmlnode import ParentNode, LeafNode


def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

def test_to_html_with_multiple_leaves(self):
    child1 = LeafNode("b", "bold")
    child2 = LeafNode("i", "italic")
    parent_node = ParentNode("p", [child1, child2])
    self.assertEqual(
        parent_node.to_html(),
        "<p><b>bold</b><i>italic</i></p>",

    )

def test_to_html_missing_tag(self):
    child_node = LeafNode("b", "child")
    parent_node = ParentNode(None, [child_node])
    with self.assertRaises(ValueError):
        parent_node.to_html()

def test_to_html_missing_children(self):
    parent_node = ParentNode("div", None)
    with self.assertRaises(ValueError):
        parent_node.to_html()

def test_to_html_mixed_siblings(self):
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, " and normal text with "),
            LeafNode("i", "italic text"),
        ],
    )
    self.assertEqual(
        node.to_html(),
        "<p><b>Bold text</b> and normal text with <i>italic text</i></p>"
    )