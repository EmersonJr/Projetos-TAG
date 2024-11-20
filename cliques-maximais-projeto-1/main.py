import networkx as nx
import matplotlib.pyplot as plt


class Graph():

    def __init__(self) -> None:
        self.graph = nx.Graph()
        self.adj= list(list())
        self.degree = list()
        self.cliques = list()
        self.agglomeration_coefficient = list()
        self.nodes = list()
        self.n = None
        self.m = None
        self.q = None



    def build_graph():
        global n, m, q, degree, graph, adj, agglomeration_coefficient ,nodes

        n, m, q = map(int, input().split())

        degree = [0] * (n+1)
        agglomeration_coefficient = [0] * (n+1)
        adj = [list() for _ in range(n+1)]  
        matrix = [[False] * (n+1) for _ in range(n+1)]
        nodes = [i for  i in range(1, n+1)]

        for i in nodes: graph.add_node(i)

        for _ in range(q):
            u, v = map(int, input().split())
            graph.add_edge(u, v)

            adj[u].append(v)
            adj[v].append(u)

            degree[u] += 1
            degree[v] += 1

    total_colors = [
        "red",
        "blue",
        "green",
        "yellow",
        "purple",
        "orange",
        "pink",
        "brown",
        "gray",
        "violet",
        "lightblue",
        "cyan",
        "magenta",
        "teal",
        "maroon", 
        "gold",
    ]

    colors = [None] * (n+1)


    for click in cliques:
        flag = True
        if(len(total_colors) == 0): break
        
        for node in click:
            if(colors[node]): flag = False

        if(not flag): continue
        color = choice(total_colors)
        for node in click:
            colors[node] = color
        total_colors.remove(color)

    colors = [i if i is not None else 'white' for i in colors]


    pos = nx.spring_layout(graph, k=1) 
    nx.draw(graph, pos, with_labels=True, node_color=colors[1:], edge_color='gray', node_size=200, font_size=12)

    plt.show()