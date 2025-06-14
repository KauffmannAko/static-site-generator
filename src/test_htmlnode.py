import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # Test props_to_html with multiple attributes
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_props_to_html_empty(self):
        # Test props_to_html with no attributes
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        # Test __repr__ method
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com"})
        expected_repr = ("HTMLNode(tag='a', value='Click here', children=[], "
                         "props={'href': 'https://www.google.com'})")
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()