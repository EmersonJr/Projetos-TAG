import networkx as nx
import matplotlib.pyplot as plt

class Node:
    """
    Classe que representa um nó no grafo, armazenando informações de uma partida.

    Atributos:
        id (int): Identificador único do nó.
        mandante (str): Time mandante da partida.
        visitante (str): Time visitante da partida.
        vizinhos (list): Lista de nós vizinhos.
        color (int): Cor atribuída ao nó (inicialmente -1, indicando não colorido).
    """

    def __init__(self, _mandante, _visitante, _id):

        self.id = _id
        self.mandante = _mandante
        self.visitante = _visitante
        self.vizinhos = list()
        self.color = -1

class Graph:
    """
    Classe que representa um grafo de partidas de futebol e realiza sua coloração.
    
    Atributos:
        graph (nx.Graph): Objeto de grafo do NetworkX.
        nodes (list): Lista de nós do grafo.
        ordered_nodes (list): Lista de nós ordenados por grau (número de vizinhos).
        total_colors (list): Lista de cores disponíveis para coloração do grafo.
    """
    
    def __init__(self):
        """
        Inicializa o grafo e constrói sua estrutura.
        """

        self.graph = nx.Graph()
        self.nodes = list()
        self.ordered_nodes = list()
        self.total_colors = [
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
            "olive",
            "teal",
            "white",
        ]
        self.build_graph()
    
    def build_graph(self):
        """
        Constrói o grafo inicial, que representa partidas entre times,
        garantindo restrições específicas sobre confrontos diretos e rodadas.

        - Primeiramente, cria 14 nós iniciais representando as rodadas.
        - Conecta todos os nós entre si para representar a possibilidade de jogos.
        - Em seguida, adiciona nós representando partidas entre times.
        - Aplica restrições específicas para impedir confrontos proibidos.
        """

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

            # Impedindo jogos específicos em certas rodadas:
            
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
                
                # Impedindo conexões entre nós que compartilham um time na mesma rodada:
                
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
                
                # Impedindo partidas onde ambos os times específicados são mandantes em qualquer rodada:
                
                if self.nodes[i].mandante == "TFC" and self.nodes[j].mandante == "OFC":
                    self.nodes[i].vizinhos.append(j)
                    self.nodes[j].vizinhos.append(i)
                    self.graph.add_edge(i, j)
                
                if self.nodes[i].mandante == "AFC" and self.nodes[j].mandante == "FFC":
                    self.nodes[i].vizinhos.append(j)
                    self.nodes[j].vizinhos.append(i)
                    self.graph.add_edge(i, j)

        # ordenando os vertices pelo clique das rodadas e grau 
        
        self.ordered_nodes.sort(key=lambda x: len(self.nodes[x].vizinhos), reverse=True)

        new_ordered_nodes = [_ for _ in range(0, 14)] 
        
        new_ordered_nodes = new_ordered_nodes + [id for id in self.ordered_nodes if id > 13]

        self.ordered_nodes = new_ordered_nodes
    
    def draw_graph(self):
        """
        Desenha o grafo utilizando a biblioteca NetworkX e Matplotlib.
        """
        
        colors = [self.total_colors[match.color] for match in self.nodes]

        pos = nx.circular_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color=colors[0:], edge_color = "black", node_size = 200, font_size = 12)
        plt.show()
        
    
    def find_matches(self, idx=0):
        """
        Realiza a coloração do grafo utilizando backtracking.
        
        Parâmetros:
            idx (int): Índice do nó sendo processado.
        
        Retorna:
            bool: True se for possível colorir o grafo, False caso contrário.
        """
        
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

    rodadas = [list() for _ in range(0, 15)]

    for i in range(14, len(gph.nodes)):

        rodadas[gph.nodes[i].color+1].append(
            list([gph.nodes[i].mandante, gph.nodes[i].visitante])
        )
    
    for rodada in range(1, len(rodadas)):
        print("Rodada ", end="")
        print(rodada, end=" -------------->\n")

        for partida in rodadas[rodada]:

            print(partida[0] + " vs " + partida[1])
    
    print()

    print("Legenda --------------")

    for i in range(0, 14):
        print("Rodada ", end="")
        print(i+1, end=": ---> ")
        print(
            gph.total_colors[gph.nodes[i].color]
        )

    gph.draw_graph()
