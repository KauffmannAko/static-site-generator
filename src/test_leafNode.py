import unittest
from LeafNode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_props(self):
        # Test rendering a LeafNode with a tag and props
        leaf = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(), '<ahref="https://www.google.com">Click me!</a>')

    def test_to_html_with_tag_no_props(self):
        # Test rendering a LeafNode with a tag and no props
        leaf = LeafNode(tag="p", value="This is a paragraph.")
        self.assertEqual(leaf.to_html(), '<p>This is a paragraph.</p>')

    def test_to_html_no_tag(self):
        # Test rendering a LeafNode with no tag
        leaf = LeafNode(value="This is raw text.")
        self.assertEqual(leaf.to_html(), "This is raw text.")

    def test_to_html_missing_value(self):
        # Test raising ValueError when value is missing
        with self.assertRaises(ValueError):
            LeafNode(tag="p")

if __name__ == "__main__":
    unittest.main()