from queue import Queue
from math import inf  
from igraph import Graph

def BFS_Distancia(grafo: Graph, origem): 
    f = Queue()
    f.put(origem)
    total_vert = grafo.vcount()
    passou = [False] * total_vert
    passou[origem] = True
    distancia = [inf] * total_vert
    distancia[origem] = 0
    parente =[None] * total_vert
    while f.qsize() != 0:
        a = f.get()
        for i in grafo.neighbors(a, mode="out"):
            if not passou[i]:
                passou[i] = True
                distancia[i] = distancia[a] + 1
                parente[i] = a
                f.put(i)   
          
    return distancia,parente



def arvore(grafo: Graph, origem):
    f = Queue()
    f.put(origem)
    total_vert = grafo.vcount()
    passou = [True] * total_vert
    passou[origem] = False
    distancia = [inf] * total_vert
    distancia[origem] = 0
    arv = Graph(total_vert)

    while f.qsize() != 0:
        a = f.get()
        for i in grafo.neighbors(a, mode="out"):
            if passou[i]:
                arv.add_edge(a,i)
                passou[i] = False
                distancia[i] = distancia[a] + 1
                f.put(i)
    return arv

def dist(origem,lista):
    frase = []
    for j in range(len(lista)):
        #print("Distancia de",origem,"para",j,"é",lista[j])
        frase.append("Para o vértice " + str(j) + " a distância é: " + str(lista[j]) + "\n")

    return frase
        