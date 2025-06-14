import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_same_properties(self):
        # Test equality when all properties are the same
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_eq_different_text(self):
        # Test inequality when text is different
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_text_type(self):
        # Test inequality when text_type is different
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)
    
    def test_eq_with_url(self):
        # Test equality when URL is provided and the same
        node1 = TextNode("This is a link", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://example.com")
        self.assertEqual(node1, node2)

    def test_not_eq_different_url(self):
        # Test inequality when URLs are different
        node1 = TextNode("This is a link", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a link", TextType.LINK, "https://different.com")
        self.assertNotEqual(node1, node2)

    def test_eq_url_none(self):
        # Test equality when URL is None
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node1, node2)


    if __name__ == "__main__":
        unittest.main()

