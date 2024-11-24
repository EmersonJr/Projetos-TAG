import networkx as nx
import matplotlib.pyplot as plt
from random import choice


class Graph():

    def __init__(self) -> None:
        self.file = 'in.txt'
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
        with open(self.file, 'r') as file:
            self.n, self.m, self.q = map(int, next(file).split())

            self.degree = [0] * (self.n+1)
            self.agglomeration_coefficient = [0] * (self.n+1)
            self.adj = [set() for _ in range(self.n+1)]  
            self.nodes = [i for  i in range(1, self.n+1)]

            for i in self.nodes: self.graph.add_node(i)

            # Aqui montamos a lista de adjacências do grafo
            for _ in range(self.q):
                u, v = map(int, next(file).split())
                self.graph.add_edge(u, v)

                self.adj[u].add(v)
                self.adj[v].add(u)

                self.degree[u] += 1
                self.degree[v] += 1
            
    def BronKerbosch(self, p : set, x : set, r : set):

        '''
            Algoritmo para encontrar cliques maximais de um grafo:
                Bron-Kerbosch sem pivô:
                    . P = candidatos a compor um clique maximal
                    . X = vertices que não podem contribuir mais para o clique
                    . R = clique atual

        '''
        if (len(p) == 0 and len(x) == 0):

            ''' 
                Se P e X estiverem vazios então temos que R é um clique maximal

            '''
            self.cliques.append(list(r))
            return
        
        for v in set(p):
            r.add(v)
            '''
                BronKerbsoch(R U {v}, P inter N(v), X inter N(v))

            '''
            self.BronKerbosch(p.intersection(self.adj[v]), x.intersection(self.adj[v]), r)
            r.remove(v)
            p.remove(v)
            x.add(v)
    
    def find_cliques(self):
        self.BronKerbosch(set(self.nodes), set(), set())

        self.cliques = sorted(self.cliques, key= len)
        self.cliques = self.cliques[::-1]
    
    def calcAglomeration(self):

        '''
            Calculamos o coeficiente de aglomeração utilizando a formula
            aprendida na disciplina, onde se é feito a razão entre as ligações
            existentes entre os vizinhos e as possiveis ligações entre os vizinhos
            
            Para calcular o coeficiente do grafo efetuamos o calculo da media dos coeficientes
            já calculados para cada nodo
            
        '''
        for v in self.nodes:

            denom = len(self.adj[v]) * (len(self.adj[v]) - 1) / 2
            if (denom == 0): 
                continue
            
            ti = 0

            aux = list(self.adj[v])

            for i in range(len(self.adj[v])):
                for j in range(i + 1, len(self.adj[v])):
                    if aux[j] in self.adj[aux[i]]:
                        ti += 1
            
            self.agglomeration_coefficient[v] = ti / denom
            self.agglo_coeff_graph += ti / denom
        
        self.agglo_coeff_graph /= self.n

    def draw_graph(self):

        '''

            Aqui realizamos a definição das cores que usaremos para
            pintar a representação do grafo

        '''
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

        colors = [None] * (self.n + 1)
        
        for click in self.cliques:
            is_none = True 
            
            for(v) in click:
                if(colors[v] != None):
                    is_none = False
                    break
            if(not is_none): continue

            color = choice(total_colors)
            for (v) in click:
                colors[v] = color 
            total_colors.remove(color)

        colors = [color if color is not None else 'white' for color in colors]

        '''

            Para fazer o desenho do grafo usamos duas bibliotecas a
            NetworkX e a MatPlotLib da NetworkX usamos o método
            "spring_layout" que realiza a formatação do grafo para o desenho,
            para realizar um desenho em um grafico do matplotlib usamos o
            método "draw" e para mostrar na tela usamos o método do matplotlib
            "show"

        '''
        pos = nx.spring_layout(self.graph, k=1)
        nx.draw(self.graph, pos, with_labels=True, node_color=colors[1:], edge_color = "black", node_size = 200, font_size = 12)
        plt.show()

        

    def __str__(self):

        '''

            No paradigma que escolhemos a maneira mais convencional
            para mostrar as coisas do grafo foi a implementação de um
            metodo

        '''
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

        '''
            
            Aqui a gente chama a função que realiza
            o desenho do grafo

        '''
        self.draw_graph()

def solve():
    graph = Graph()

    graph.build_graph()
    graph.find_cliques()
    graph.calcAglomeration()

    print(graph)

if __name__ == "__main__":
    solve()