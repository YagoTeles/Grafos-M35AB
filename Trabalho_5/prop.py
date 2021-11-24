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
caminho2 = []

def DFS_Recursivo(grafo: Graph,inicio,descoberto: list = [],arvore: Graph = None):
    if inicio not in descoberto:
        descoberto.append(inicio)
        #print(inicio,end=" -> ")
        caminho2.append(str(inicio))
        for i in grafo.neighbors(inicio, mode="all"):
            if i not in descoberto:
                if arvore is not None: arvore.add_edge(inicio,i)
                DFS_Recursivo(grafo,i,descoberto = descoberto,arvore = arvore)

def DFS_C():
    frase = []
    frase.append(" -> ".join(caminho2))
    return frase
    

def DFS_Pilha(grafo: Graph,inicio,arvore: Graph = None,direcao = 'menor'):
    descoberto = [];pilha = [inicio]
    ultimo = -1
    caminho = [];frase = []
    
    while len(pilha) > 0:
        p = pilha.pop()
        if p not in descoberto:
            #print(p,end=" -> ")
            caminho.append(str(p))
            if (arvore is not None) and (ultimo >= 0) :
                #if(ultimo in grafo.neighbors(p, mode="all")):
                    arvore.add_edge(ultimo,p)    
            descoberto.append(p)
            ultimo = p
            if(direcao == 'menor'):
                for i in reversed(grafo.neighbors(p, mode="all")):
                    pilha.append(i)
            if(direcao == 'maior'):
                for i in grafo.neighbors(p, mode="all"):
                    pilha.append(i)

    frase.append(" -> ".join(caminho))
    return descoberto

def dist(origem,lista):
    frase = []
    for j in range(len(lista)):
        #print("Distancia de",origem,"para",j,"é",lista[j])
        frase.append("Para o vértice " + str(j) + " a distância é: " + str(lista[j]) + "\n")

    return frase
        