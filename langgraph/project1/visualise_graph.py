from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except:
    pass

#copy this in the end of Jupiter notebook, separate cell, execute
