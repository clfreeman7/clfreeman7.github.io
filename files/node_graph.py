# Graph visualization to show experience and education that inform my research.
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx

# Create the graph. 
G = nx.Graph()

# Define groups of nodes and their labels.
phd_courses = ['Mechanical Vibrations', 'Advanced Linear Control', 'Engineering Optimization',
               'Linear Algebra', 'Machine Learning', 'Intro to Mechatronics', 
               'Digital Signal Processing', 'Intro to Robotics', 'Linear Optimization Theory',
               'MechE Analysis', 'Adv Robot Kinematics and Dynamics', 'Optimal Control and Estimation', 
               'Partial Differential Equations', 'Biomechanics of Human Movement']
committee_fields = ['Dr. Sameer Mulani<br>Optimization<br>Aerospace (UA)', 
                    'Dr. Vishesh Vikas<br>Soft Robotics<br>MechE (UA)',
                    'Dr. Sree Kalyan Patiballa<br>Metamaterials<br>MechE (UA)', 
                    'Dr. Hwan-Sik Yoon<br>AI/ML<br>MechE (UA)', 
                    'Dr. W. Steve Shepard Jr.<br>Vibrations/Acoustics<br>Mech E (UA)', 
                    'Dr. Barry Trimmer<br>Biology/Neuroscience<br>Tufts University']
committee_members = ['Sameer Mulani', 'Vishesh Vikas', 'Sree Kalyan Patiballa', 
                     'Hwan-Sik Yoon' , 'W. Steve Shepard Jr.', 'Barry Trimmer']
research_fields = ['Design Optimization', 'Modular Reconfigurable Robots', 'Reinforcement Learning',
                    'Mobile Soft Robots', 'Computer Vision', 'Visual Tracking', 'Bio-inspired Robots',
                   'Optimal Control', 'Probability and Statistics', 'Path Planning',
                   'Closed-Loop Control', 'Design of Experiments', 'Hypothesis Testing', 
                   'Neural Control', 'Locomotion Simulation and Analysis', 'Inertial Sensors', 
                   'Topology', 'Lie Algebra', 'Kinematics and Dynamics', 'Data Visualization', 
                   'Reproducibility', 'Bioacoustics', 'Biological Tissue Phantoms']
related_fields = ['Surgical Robots', 'Agricultural Robots', 'Search and Rescue Robots', 
                  'Central Pattern Generators', 'Materials Engineering', 'Biomechanical Modeling',
                  'Human Gait Analysis', 'Neuroscience', 'Computational Biology']
category_bubbles = [phd_courses, committee_fields, research_fields, related_fields]
category_names = ['PhD<br>Courses', 'Dissertation<br>Committee', 'Dissertation<br>Research', 'Related<br>Research']
node_sizes = []
node_labels = []
hover_labels = []
node_colors = []
# Create central node.
center_node = 'My<br>Research'
G.add_node(center_node)

node_labels.append(center_node)
node_sizes.append(80)
hover_labels.append(None)
node_colors.append(0)

# Add connections (edges) to connect the nodes.
for i, bubble in enumerate(category_bubbles):
    G.add_edge(center_node, category_names[i])
    node_sizes.append(80)
    node_labels.append(category_names[i])
    hover_labels.append(None)
    node_colors.append(i+1)
    for component in bubble:
        G.add_edge(category_names[i], component)
        node_sizes.append(20)
        node_labels.append(None)
        hover_labels.append(component)
        node_colors.append(i+1)
node_size_dict = {k:v for v,k in zip(G.nodes,node_sizes)}
pos = nx.forceatlas2_layout(G, seed=17, scaling_ratio=15, strong_gravity=True)
#pos = nx.forceatlas2_layout(G, seed=6, scaling_ratio=15, strong_gravity=True)
#pos = nx.forceatlas2_layout(G, seed=6, scaling_ratio=.5, strong_gravity=True, node_size=node_size_dict)
#pos = nx.forceatlas2_layout(G, seed=9, scaling_ratio=.5, node_size=node_size_dict)
#print(pos)
#print(list(G.nodes))

# Create edge trace and nodes scatter trace for plotly.
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=False,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale='YlGnBu',
        #reversescale=True,
        color=[],
        size=10,
 #       colorbar=dict(
 #           thickness=15,
 #           title=dict(
 #             text='Node Connections',
 #             side='right'
 #           ),
  #         xanchor='left',
#        ),
        line_width=2))

node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(G.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append('# of connections: '+str(len(adjacencies[1])))

node_trace.marker.color = node_colors
node_trace.marker.size = node_sizes
node_trace.hovertext = hover_labels

fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
              #  title=dict(
              #      text="<br>Network graph made with Python",
              #      font=dict(
              #          size=16
              #      )
              #),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code for this plot can be found on"
                    "<a href='https://github.com/clfreeman7/clfreeman7.github.io/blob/master/files/node_graph.py'>"
                    " my GitHub</a>.",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
# Add permanent annotations.
fig.add_trace(go.Scatter(x=node_x, y=node_y, 
                         mode = "text",
                         name = "Text",
                         text = node_labels,
                         textposition="middle center"))

fig.show()


fig.write_html('_pages/plotly_example.html', full_html=False, include_plotlyjs='cdn')
