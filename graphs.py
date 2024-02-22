# Import necessary modules
import networkx as nx
import matplotlib.pyplot as plt
import nxviz as nv
from nxviz import annotate, highlights


# Initialize empty graph
T = nx.Graph()

# Add Nodes
# a. From List
T.add_nodes_from([1, 2, 3])

# Add Node Metadata
T.nodes()[1]['label'] = 'blue'
T.nodes()[2]['label'] = 'blue'
T.nodes()[3]['label'] = 'blue'

# Add Edges
T.add_edge(1, 2)

# nx.draw(T)
# plt.show()

# Create the CircosPlot object: c
c = nv.circos(T)

# Draw c to the screen
annotate.circos_group(G=T, group_by="label")

# Display the plot
# plt.show()
