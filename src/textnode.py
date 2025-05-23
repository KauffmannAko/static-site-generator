from enum import Enum


class TextType(Enum):
    TEXT = "text"           # Normal text
    BOLD = "bold"           # **Bold text**
    ITALIC = "italic"       # _Italic text_
    CODE = "code"           # `Code text`
    LINK = "link"           # [anchor text](url)
    IMAGE = "image"         # ![alt text](url)      


class TextNode:
    def __init__(self, text, text_type, url=None):
        # Initializes a TextNode with text, type, 
        # and optional URL for links/images
        self.text = text
        self.text_type = text_type
        if self.text_type in {TextType.LINK, TextType.IMAGE}:
            self.url = url
        else:
            self.url = None

    def __repr__(self):
        # Returns a string representation of the TextNode
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def __eq__(self, other):
        # Compares two TextNode objects for equality
        if not isinstance(other, TextNode):
            return False  
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)