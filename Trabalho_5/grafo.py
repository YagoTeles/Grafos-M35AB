import math
from igraph import Graph
import igraph
class add:
    def __init__(self,arestas):
        self.arestas = arestas
        self.total_de_vert = self.total_vert()
        self.graf = Graph(self.total_de_vert)
        self.dict_grau = self.graus()
    
    def total_vert(self):
        total = -math.inf
        for i in range(len(self.arestas)):
            tmp = self.arestas[i].split()
            v1 = int(tmp[0])
            v2 = int(tmp[-1])
            total = max(total,v1,v2)
        return total+1

    def adicionar(self):
        for i in range(len(self.arestas)):
            tmp = self.arestas[i].split()
            v1 = int(tmp[0])
            v2 = int(tmp[-1])
            self.graf.add_edge(v1,v2)

    def grafo_(self):
        return self.graf
    
    def graus(self):
        dic_grau = {}
        for i in range(self.total_de_vert): dic_grau[i] = 0  
        for i in range(len(self.arestas)):
            tmp = self.arestas[i].split()
            v1 = int(tmp[0])
            v2 = int(tmp[-1])
            dic_grau[v1] += 1
            dic_grau[v2] += 1
        return dic_grau
    
    def max_grau(self):
        total = -math.inf
        for item in self.dict_grau.items():
            total = max(total,item[1])
        return "O grau máximo é: " + str(total) + "\n"

    def min_grau(self):
        total = +math.inf
        for item in self.dict_grau.items():
            total = min(total,item[1])
        return "O grau mínimo é: " + str(total) + "\n"

    def grau_medio(self):
        soma = 0
        for item in self.dict_grau.items():
            soma += item[1]
        return "O grau médio é: " + str(soma/self.total_de_vert) + "\n"

    def plotar_grafo(self,tipo_grafo = 'circle',modo = 'defalt'):
        plot = self.grafo_()
        if(modo == 'defalt'):
            plot.vs['label'] = range(0,len(plot.vs))
        if(modo == 'br'):
            plot.vs['label'] = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 
            'PA','PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']   
                
        igraph.plot(plot,"grafo.png",(0,0,600,600),layout = plot.layout(tipo_grafo),
        margin = 40,vertex_label_dist=0,vertex_size=40,edge_width = 6,vertex_color = 'teal',edge_color = 'black')


    
    