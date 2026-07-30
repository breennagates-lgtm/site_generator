import unittest
from extract_title import extract_title

def test_extract_title(self):
    markdown = "# This is a title\n\nThis is some content."
    expected_title = "This is a title"
    self.assertEqual(extract_title(markdown), expected_title)

def test_extract_title_no_h1(self):
    markdown = "This is some content without a title."
    with self.assertRaises(Exception) as context:
        extract_title(markdown)
    self.assertEqual(str(context.exception), "No H1 Title Found")

def test_extract_title_multiple_h1(self):
    markdown = "# First Title\n\n# Second Title\n\nThis is some content."
    expected_title = "First Title"
    self.assertEqual(extract_title(markdown), expected_title)

def test_extract_title_with_whitespace(self):
    markdown = "#   Title with whitespace   \n\nThis is some content."
    expected_title = "Title with whitespace"
    self.assertEqual(extract_title(markdown), expected_title)

def test_extract_buried_title(self):
    markdown = "Some content before the title.\n\n# Buried Title\n\nThis is some content."
    expected_title = "Buried Title"
    self.assertEqual(extract_title(markdown), expected_title)

def test_extract_title_surrounded_by_other_headers(self):
    markdown = "## Subtitle\n\n# Main Title\n\n### Sub-subtitle\n\nThis is some content."
    expected_title = "Main Title"
    self.assertEqual(extract_title(markdown), expected_title)

def test_extract_title_nospaces_after_hash(self):
    markdown = "#TitleWithoutSpaces\n\nThis is some content."
    with self.assertRaises(Exception) as context:
        extract_title(markdown)
    self.assertEqual(str(context.exception), "No H1 Title Found")



def test_extract_title_no_input(self):
    markdown = ""
    with self.assertRaises(Exception) as context:
        extract_title(markdown)
    self.assertEqual(str(context.exception), "No H1 Title Found")
    