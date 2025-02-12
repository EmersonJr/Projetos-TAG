import networkx as nx
import matplotlib.pyplot as plt

class Node:

    # Definição de uma classe nó para armazenar
    # todas as informações comuns a uma partida

    def __init__(self, _mandante, _visitante, _id):

        self.id = _id
        self.mandante = _mandante
        self.visitante = _visitante
        self.vizinhos = list()
        self.color = -1

class Graph:

    def __init__(self):

        self.graph = nx.Graph()
        self.nodes = list()
        self.ordered_nodes = list()
        self.build_graph()
    
    def build_graph(self):

        for i in range(0, 14):
            self.nodes.append(Node("-1", "-1", i))
        
        for i in range(0, 14):
            for j in range(i+1, 14):
                self.graph.add_edge(i, j)

                self.nodes[i].vizinhos.append(j)
                self.nodes[j].vizinhos.append(i)
        
        times = ["DFC", "TFC", "AFC", "LFC", "FFC", "OFC", "CFC"]

        for time_mandante in times:
            for time_visitante in times:
                if time_mandante != time_visitante:
                    self.nodes.append(Node(time_mandante, time_visitante, len(self.nodes)))
        
        for i in range(0, len(self.nodes)):

            self.ordered_nodes.append(i)

            if self.nodes[i].mandante == "DFC" and self.nodes[i].visitante == "CFC":
                self.nodes[i].vizinhos.append(0)
                self.nodes[i].vizinhos.append(13)
                self.nodes[0].vizinhos.append(i)
                self.nodes[13].vizinhos.append(i)
                self.graph.add_edge(i, 13)
                self.graph.add_edge(i, 0)
            
            if self.nodes[i].mandante == "LFC" and self.nodes[i].visitante == "FFC":
                self.nodes[i].vizinhos.append(6)
                self.nodes[i].vizinhos.append(12)
                self.nodes[6].vizinhos.append(i)
                self.nodes[12].vizinhos.append(i)
                self.graph.add_edge(i, 12)
                self.graph.add_edge(i, 6)
            
            if self.nodes[i].mandante == "OFC" and self.nodes[i].visitante == "LFC":
                self.nodes[i].vizinhos.append(9)
                self.nodes[i].vizinhos.append(10)
                self.nodes[9].vizinhos.append(i)
                self.nodes[10].vizinhos.append(i)
                self.graph.add_edge(i, 9)
                self.graph.add_edge(i, 10)

            if self.nodes[i].mandante == "AFC" and self.nodes[i].visitante == "FFC":
                self.nodes[i].vizinhos.append(11)
                self.nodes[i].vizinhos.append(12)
                self.nodes[11].vizinhos.append(i)
                self.nodes[12].vizinhos.append(i)
                self.graph.add_edge(i, 11)
                self.graph.add_edge(i, 12)

            if self.nodes[i].mandante == "CFC" and self.nodes[i].visitante == "TFC":
                self.nodes[i].vizinhos.append(1)
                self.nodes[i].vizinhos.append(2)
                self.nodes[1].vizinhos.append(i)
                self.nodes[2].vizinhos.append(i)
                self.graph.add_edge(i, 1)
                self.graph.add_edge(i, 2)
            
            for j in range(i+1, len(self.nodes)):
                
                if self.nodes[i].mandante == self.nodes[j].mandante:
                    self.nodes[i].vizinhos.append(j)
                    self.nodes[j].vizinhos.append(i)
                    self.graph.add_edge(i, j)
                    continue

                if self.nodes[i].mandante == self.nodes[j].visitante:
                    self.nodes[i].vizinhos.append(j)
                    self.nodes[j].vizinhos.append(i)
                    self.graph.add_edge(i, j)
                    continue

                if self.nodes[i].visitante == self.nodes[j].mandante:
                    self.nodes[i].vizinhos.append(j)
                    self.nodes[j].vizinhos.append(i)
                    self.graph.add_edge(i, j)
                    continue

                if self.nodes[i].visitante == self.nodes[j].visitante:
                    self.nodes[i].vizinhos.append(j)
                    self.nodes[j].vizinhos.append(i)
                    self.graph.add_edge(i, j)
                    continue
                if self.nodes[i].mandante == "TFC" and self.nodes[j].mandante == "OFC":
                    self.nodes[i].vizinhos.append(j)
                    self.nodes[j].vizinhos.append(i)
                    self.graph.add_edge(i, j)
                
                if self.nodes[i].mandante == "AFC" and self.nodes[j].mandante == "FFC":
                    self.nodes[i].vizinhos.append(j)
                    self.nodes[j].vizinhos.append(i)
                    self.graph.add_edge(i, j)
            
            new_ordered_nodes = list()

            self.ordered_nodes.sort(key=lambda x: len(self.nodes[x].vizinhos), reverse=True)

            for i in range(0, 14):
                new_ordered_nodes.append(i)
            
            for id in self.ordered_nodes:
                if id > 13:
                    new_ordered_nodes.append(id)
            
            self.ordered_nodes = new_ordered_nodes
    
    def draw_graph(self):
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
            "white"
        ]

        colors = [total_colors[match.color] for match in self.nodes]

        pos = nx.spring_layout(self.graph, k=1)
        nx.draw(self.graph, pos, with_labels=True, node_color=colors[0:], edge_color = "black", node_size = 200, font_size = 12)
        plt.show()
        
    
    def find_matches(self, idx=0):
        if idx == len(self.ordered_nodes):
            return True
        cant = 0
        for vizin in self.nodes[self.ordered_nodes[idx]].vizinhos:
            if self.nodes[vizin].color == -1:
                continue
            cant |= (1 << self.nodes[vizin].color)
        if cant == ((1 << 14) - 1):
            return False
        for i in range(0, 14):
            if (cant & (1 << i)) > 0:
                continue
            self.nodes[self.ordered_nodes[idx]].color = i
            ret = self.find_matches(idx+1)
            if ret:
                return True
            self.nodes[self.ordered_nodes[idx]].color = -1
        return False

if __name__ == "__main__":

    gph = Graph()

    gph.draw_graph()

    gph.find_matches()
    for i in range(0, len(gph.nodes)):
        print(gph.nodes[i].mandante + " " + gph.nodes[i].visitante, end=" - > ")
        print(gph.nodes[i].color+1)
    
    gph.draw_graph()