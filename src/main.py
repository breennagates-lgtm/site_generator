from textnode import TextNode, TextType

def main():
    # Create a TextNode instance
    text_node = TextNode("Hello, World!", text_type=TextType.BOLD_TEXT, url="https://example.com")

    # Print the TextNode instance
    print(text_node)   

main()