import graphviz

# def draw_dot(root, format='svg', rankdir='LR'):
#     """
#     format: png | svg | ...
#     rankdir: TB (top to bottom graph) | LR (left to right)
#     """
#     assert rankdir in ['LR', 'TB']
#     nodes, edges = trace(root)
#     dot = Digraph(format=format, graph_attr={'rankdir': rankdir}) #, node_attr={'rankdir': 'TB'})
    
#     for n in nodes:
#         dot.node(name=str(id(n)), label = "{ data %.4f | grad %.4f }" % (n.data, n.grad), shape='record')
#         if n._op:
#             dot.node(name=str(id(n)) + n._op, label=n._op)
#             dot.edge(str(id(n)) + n._op, str(id(n)))
    
#     for n1, n2 in edges:
#         dot.edge(str(id(n1)), str(id(n2)) + n2._op)
    
#     return dot



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

    
    
