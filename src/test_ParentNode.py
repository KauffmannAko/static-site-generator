import unittest
from ParentNode import ParentNode
from LeafNode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        # Test rendering a ParentNode with one child
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        # Test rendering a ParentNode with nested children
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        # Test rendering a ParentNode with multiple children
        child1 = LeafNode("p", "Paragraph 1")
        child2 = LeafNode("p", "Paragraph 2")
        parent_node = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>",
        )

    def test_to_html_missing_tag(self):
        # Test raising ValueError when tag is missing
        child_node = LeafNode("span", "child")
        with self.assertRaises(ValueError):
            ParentNode(None, [child_node])

    def test_to_html_missing_children(self):
        # Test raising ValueError when children are missing
        with self.assertRaises(ValueError):
            ParentNode("div", [])

if __name__ == "__main__":
    unittest.main()