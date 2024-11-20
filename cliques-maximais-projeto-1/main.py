import networkx as nx
import matplotlib.pyplot as plt


class Graph():

    def __init__(self) -> None:
        self.graph = nx.Graph()
        self.adj= list(set())
        self.degree = list()
        self.cliques = list()
        self.agglomeration_coefficient = list()
        self.nodes = list()
        self.n = None
        self.m = None
        self.q = None
        self.agglo_coeff_graph = 0

    def build_graph(self):

        self.n, self.m, self.q = map(int, input().split())

        self.degree = [0] * (self.n+1)
        self.agglomeration_coefficient = [0] * (self.n+1)
        self.adj = [set() for _ in range(self.n+1)]  
        self.nodes = [i for  i in range(1, self.n+1)]

        for i in self.nodes: self.graph.add_node(i)

        for _ in range(self.q):
            u, v = map(int, input().split())
            self.graph.add_edge(u, v)

            self.adj[u].add(v)
            self.adj[v].add(u)

            self.degree[u] += 1
            self.degree[v] += 1
            
    def bronKerbosch(self, p : set, x : set, r : set):

        if len(p) == 0 and len(x) == 0:
            self.cliques.append(r)
            return
        
        for v in p:

            p_v = p.intersection(self.adj[v])
            x_v = x.intersection(self.adj[v])
            r_v = r.union(set(v))

            self.bronKerbosch(p_v, x_v, r_v)

            p.pop(v)
            x.add(v)
    
    def calcAglomeration(self):

        for v in self.nodes:

            denom = len(self.adj[v]) *(len(self.adj[v]) - 1) / 2
            ti = 0

            aux = list(self.adj[v])

            for i in range(len(self.adj[v])):
                for j in range(i + 1, len(self.adj[v])):
                    if aux[v][j] in self.adj[aux[v][i]]:
                        ti += 1
            
            self.agglomeration_coefficient[v] = ti / denom
            self.agglo_coeff_graph += ti / denom
        
        self.agglo_coeff_graph /= self.n
    
    def __str__(self):

        print("Vértices e grau: ")

        for v in self.nodes:
            print("Vértice", end=" => ")
            print(v, end= ". Grau => ")
            print(self.degree[v])
        print()
        print("Cliques Maximais: ")

        for i in range(len(self.cliques)):
            print(f"Clique {i+1}", end=" => ")
            for u in self.cliques[i]:
                print(u, end=" ")
            print()
        print()
        print("Coeficientes de algomeração dos vértices: ")

        for v in self.nodes:
            print("Vértice", end=" => ")
            print(v, end= ". coeficiente de aglomeração => ")
            print(self.agglomeration_coefficient[v])
        
        print(f"Coeficiente de aglomeração do grafo: {self.agglo_coeff_graph}")
        print()