from igraph import Graph
import prop

def fecho_hamil (grafo: Graph):
    fh = grafo.copy()
    n = len(fh.vs) 
    vert = prop.non_adj_vert(fh)
    for i,j in vert:
        if (fh.degree(i) + fh.degree(j) >=n):
            fh.add_edge(i,j)
            return fecho_hamil(fh)
    return fh

def ore (grafo: Graph):
    n = len(grafo.vs)

    for i, j in prop.non_adj_vert(grafo):
        if (grafo.degree(i) + grafo.degree(j) < n):
            return False
    return True

def bondy(grafo: Graph):
    fecho = fecho_hamil(grafo)

    if prop.verificar_fechado(fecho): return True
    return False

def dirac(grafo: Graph):
    n = len(grafo.vs)
    if (n < 3): return False
    for i in grafo.vs:
        if (i.degree() < n/2): 
            return False

    return True

def verificar (grafo: Graph):
    
    if(dirac(grafo)): print("Satisfaz o teorema de Dirac")
    if(ore(grafo)): print("Satisfaz o teorema de Ore")
    if(bondy(grafo)): print("Satisfaz o teorema de Bondy e Chvatal")
    if(bondy(grafo) is False and ore(grafo)is False and dirac(grafo)is False): print("Esse grafo nao satisfaz nenhum dos tres teoremas")

