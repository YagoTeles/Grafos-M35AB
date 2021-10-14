from igraph import Graph
from igraph.drawing import plot

import prop
import igraph
class trabalho_4:
    def __init__(self,origem,grafo:Graph):
        self.origem = origem
        self.grafo = grafo

    def caminho(self):
        frase = []
        x = prop.BFS_Distancia(self.grafo,self.origem)
        lista = x[1]
        total_vert = self.grafo.vcount()
        for i in range(total_vert):
            caminho = [str(i)]
            temp = i
            while lista[temp] != None:
                caminho.insert(0,str(lista[temp]))
                temp = lista[temp]
            #print(" -> ".join(caminho))
            frase.append(" -> ".join(caminho) + "\n")
        return frase
    
    def distancia(self):
        x = prop.BFS_Distancia(self.grafo,self.origem)
        
        return prop.dist(self.origem,x[0])

    def plotar_arv(self,modo = 'defalt'):
        plot = prop.arvore(self.grafo,self.origem)
        if(modo == 'defalt'):
            plot.vs['label'] = range(0,len(plot.vs))
        if(modo == 'br'):
            plot.vs['label'] = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 
            'PA','PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']             
        cor =  ['brown'] * len(self.grafo.vs)
        cor[self.origem] = 'teal'
        igraph.plot(plot,"grafo_arv.png",(0,0,600,600),layout=plot.layout('tree',root=[self.origem]), 
        margin = 40,vertex_label_dist=0,vertex_size=40,edge_width = 6,vertex_color = cor,edge_color = 'black')