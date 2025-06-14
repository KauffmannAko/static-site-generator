from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        # Raise an error if the value is missing
        if self.value is None:
            raise ValueError("LeafNode must have a value to render as HTML.")
        
        # If no tag is provided, return the value as raw text
        if self.tag is None:
            return self.value
        
        # Render the HTML tag with props and value
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

