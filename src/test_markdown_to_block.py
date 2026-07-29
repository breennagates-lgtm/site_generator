import unittest
from markdown_blocks import markdown_to_blocks

def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ], 
        )

def test_empty_markdown(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])    

def test_markdown_excessive_blank_lines(self):
        md = """


This is a paragraph with excessive blank lines before and after it


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph with excessive blank lines before and after it",
            ],
        )

def test_markdown_one_block(self):
        md = "This is a single block of text with no blank lines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a single block of text with no blank lines",
            ],
        )

def test_markdown_messy_white_space(self):
    md = """
   # Heading with leading spaces   

  This paragraph has spaces before and after it.
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "# Heading with leading spaces",
            "This paragraph has spaces before and after it.",
        ], 
    )


def test_markdown_only_blank_lines(self):
    md = """


"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(blocks, [])

def test_markdown_paragraph_with_new_single_lines(self):
    md = "This is line one.\nThis is line two.\nThis is line three."
    blocks = markdown_to_blocks(md)
    self.assertEqual(
    blocks,
    [
        "This is line one.\nThis is line two.\nThis is line three.",
    ], 
)         


def test_markdown_to_blocks_complex_document(self):
        md = """
# Welcome to My Project

This is an **introductory paragraph** with _italicized_ text and `inline code`.
It spans multiple lines in the same block.


> "Simplicity is prerequisite for reliability."
> — Edsger W. Dijkstra
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Welcome to My Project",
                "This is an **introductory paragraph** with _italicized_ text and `inline code`.\nIt spans multiple lines in the same block.",
                "> \"Simplicity is prerequisite for reliability.\"\n> — Edsger W. Dijkstra", 
            ], 
        )




