from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from sphinx.application import Sphinx

# -- Options for CollapseNode handler ----------------------------------------------
class CollapseNode(nodes.General,nodes.Element):
    pass

class CollapseDirective(SphinxDirective):
    required_arguments = 0 # summary text is required as first argument
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        node = CollapseNode()
        summary = self.arguments[0] if self.arguments else "Details" # store the summary text here
        node['summary'] = summary
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]

def visit_collapse_html(self, node):
    self.body.append(self.starttag(node, 'details'))
    self.body.append(f"<summary>{node['summary']}</summary>")

def depart_collapse_html(self, node):
    self.body.append('</details>')

def setup(app: Sphinx):
    app.add_node(
        CollapseNode,
        html=(visit_collapse_html, depart_collapse_html),
        html5=(visit_collapse_html, depart_collapse_html)
    )
    app.add_directive('collapse', CollapseDirective)