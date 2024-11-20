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



    def build_graph(self):

        self.n, self.m, self.q = map(int, input().split())

        self.degree = [0] * (self.n+1)
        self.agglomeration_coefficient = [0] * (self.n+1)
        self.adj = [list() for _ in range(self.n+1)]  
        self.nodes = [i for  i in range(1, self.n+1)]

        for i in self.nodes: self.graph.add_node(i)

        for _ in range(self.q):
            u, v = map(int, input().split())
            self.graph.add_edge(u, v)

            self.adj[u].append(v)
            self.adj[v].append(u)

            self.degree[u] += 1
            self.degree[v] += 1

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