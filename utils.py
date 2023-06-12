import graphviz

def render(root):

    nodes, edges = set(), set()

    # Find all the nodes
    def visit(p):
        nodes.add(p)
        for c in p._children:
            edges.add((c, p))
            visit(c)
    visit(root)
    
    dot = graphviz.Digraph(graph_attr={'rankdir': 'LR'})

    for node in nodes:
        dot.node(name=str(id(node)), label=node.graph_str(), shape='record')
        if node._op:
            node_name = str(id(node))
            op_name = node_name + node._op
            dot.node(name=op_name, label=node._op)
            dot.edge(op_name, node_name)

    for n1, n2 in edges:
        dot.edge(str(id(n1)), str(id(n2))+n2._op)
        
    dot.view()

    
    
