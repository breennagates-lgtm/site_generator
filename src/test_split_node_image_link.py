from inline_markdown import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
import unittest


def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

def test_split_links(self):
    node = TextNode(
        "This is text with a [link](https://example.com) and another [second link](https://example.org)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://example.org"),
        ],
        new_nodes,
    )

def test_split_images_and_links(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    new_nodes = split_nodes_link(new_nodes)
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
        ],
        new_nodes,
    )

def test_split_images_with_no_links(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

def test_split_links_with_no_images(self):
    node = TextNode(
        "This is text with a [link](https://example.com) and another [second link](https://example.org)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://example.org"),
        ],
        new_nodes,
    )

def test_split_images_and_links_with_no_text(self):
    node = TextNode(
        "![image](https://i.imgur.com/zjjcJKZ.png)[link](https://example.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    new_nodes = split_nodes_link(new_nodes)
    self.assertListEqual(
        [
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode("link", TextType.LINK, "https://example.com"),
        ],
        new_nodes,
    )

def test_split_images_and_links_with_text_at_start_and_end(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com) at the end",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    new_nodes = split_nodes_link(new_nodes)
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" at the end", TextType.TEXT),
        ],
        new_nodes,
    )

def test_split_images_and_links_with_text_only(self):
    node = TextNode(
        "This is text with no images or links",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    new_nodes = split_nodes_link(new_nodes)
    self.assertListEqual(
        [
            TextNode("This is text with no images or links", TextType.TEXT),
        ],
        new_nodes,
    )

def test_split_images_and_links_with_empty_text(self):
    node = TextNode(
        "",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    new_nodes = split_nodes_link(new_nodes)
    self.assertListEqual(
        [
            TextNode("", TextType.TEXT),
        ],
        new_nodes,
    )

def test_split_images_and_links_with_none_text(self):
    node = TextNode(
        None,
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    new_nodes = split_nodes_link(new_nodes)
    self.assertListEqual(
        [
            TextNode(None, TextType.TEXT),
        ],
        new_nodes,
    )

def test_split_images_and_links_with_non_plain_text(self):
    node = TextNode(
        "This is **bold** text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)",
        TextType.BOLD,
    )
    new_nodes = split_nodes_image([node])
    new_nodes = split_nodes_link(new_nodes)
    self.assertListEqual(
        [
            TextNode(
                "This is **bold** text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)",
                TextType.BOLD,
            ),
        ],
        new_nodes,
    )

def test_split_images_and_links_with_mixed_text_types(self):
    nodes = [
        TextNode(
            "This is **bold** text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)",
            TextType.BOLD,
        ),
        TextNode(
            "This is *italic* text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)",
            TextType.ITALIC,
        ),
        TextNode(
            "This is `code` text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)",
            TextType.CODE,
        ),
    ]
    new_nodes = split_nodes_image(nodes)
    new_nodes = split_nodes_link(new_nodes)
    self.assertListEqual(
        [
            TextNode(
                "This is **bold** text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)",
                TextType.BOLD,
            ),
            TextNode(
                "This is *italic* text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)",
                TextType.ITALIC,
            ),
            TextNode(
                "This is `code` text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)",
                TextType.CODE,
            ),
        ],
        new_nodes,
    )

