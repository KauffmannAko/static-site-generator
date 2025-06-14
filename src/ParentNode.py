from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self,tag, children,props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag")
        if not children:
            raise ValueError("ParentNode must have children")
        super().__init__(tag=tag, value=None, children=children, props=props)
    def to_html(self):
         # Raise an error if the tag is missing
        if not self.tag:
            raise ValueError("ParentNode must have a tag to render as HTML.")
        
        # Raise an error if children are missing
        if not self.children:
            raise ValueError("ParentNode must have children to render as HTML.")
        
        # Convert props to HTML attributes
        props_html = self.props_to_html()
        
        # Recursively render children
        children_html = "".join(child.to_html() for child in self.children)
        
        # Return the HTML representation
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"