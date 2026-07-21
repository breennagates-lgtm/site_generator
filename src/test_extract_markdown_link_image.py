
import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links

def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

def test_extract_markdown_links(self):
    matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev)"
    )
    self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

def test_extract_markdown_links_multiple(self):
    matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    )
    self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

def test_extract_markdown_links_with_image(self):
    matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev) and an image ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)        

def test_extract_markdown_links_with_image_and_link(self):
    matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev) and an image ![image](https://i.imgur.com/zjjcJKZ.png) and another link [to youtube](https://www.youtube.com/@bootdotdev)"
    )
    self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

def test_extract_markdown_images_multiple(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

def test_extract_markdown_images_empty_string(self):
    matches = extract_markdown_images(
        "This is just plain text."
    )
    self.assertListEqual([], matches)   

def test_extract_markdown_links_none(self):
    matches = extract_markdown_links(
        "This is just plain text."    
    )
    self.assertListEqual([], matches)

