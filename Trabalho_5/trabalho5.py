from igraph import Graph
from igraph.drawing import plot

import prop
import igraph
class trabalho_5:
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

    def caminho_DFS_pilha(self,direcao = 'menor'):
        x = Graph(len(self.grafo.vs))
        return prop.DFS_Pilha(self.grafo,self.origem,arvore=x,direcao = direcao)
        
    def caminho_DFS_recursivo(self):
        x = Graph(len(self.grafo.vs))
        prop.DFS_Recursivo(self.grafo,self.origem,arvore=x)
        return prop.DFS_C()

    def distancia(self):
        x = prop.BFS_Distancia(self.grafo,self.origem)
        
        return prop.dist(self.origem,x[0])

    def connected_components(self,graph: Graph):

        components = []
        visited = []

        for v in range(len(graph.vs)):
            if v not in visited:
                dfs_result = prop.DFS_Pilha(self.grafo,self.origem)
                components.append(dfs_result)
                visited.extend(dfs_result)

        components.sort(key=lambda l: len(l), reverse=True)

        return components

    def subgraph(self, vertices: "list[int]"):
        new_graph = self.grafo
        vertices_to_remove = [v.index for v in new_graph.vs if v.index not in vertices]
        new_graph.delete_edges([(2,3),(6,3),(4,5),(1,3)])
        return new_graph

    def plotar_arv(self,modo = 'defalt',dfs = 'r'):
        
        if dfs == 'r':
            x = Graph(len(self.grafo.vs))
            prop.DFS_Recursivo(self.grafo,self.origem,arvore=x)
            plot = x

        if dfs == 'p':
            x = Graph(len(self.grafo.vs))
            prop.DFS_Pilha(self.grafo,self.origem,arvore=x)
            print(self.connected_components(self.grafo))
            plot = self.subgraph([0])
       
        z = 800;y = 800
        if(modo == 'defalt'):
            plot.vs['label'] = range(1,len(plot.vs)+1)
        if(modo == 'br'):
            plot.vs['label'] = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 
            'PA','PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']  

        cor =  ['brown'] * len(self.grafo.vs)
        cor[self.origem] = 'teal'
        if len(self.grafo.vs) > 15: z=1000;y=1500
        igraph.plot(plot,"grafo_arv.png",(0,0,z,y),layout=plot.layout('tree',root=[self.origem]), 
        margin = 40,vertex_label_dist=0,vertex_size=40,edge_width = 6,vertex_color = cor,edge_color = 'black')