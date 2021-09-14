    #es -> aresta
    #vs -> vert
from igraph import Graph
from adicionar import adicionar
def non_adj_vert(grafo: Graph):
        x = len(grafo.vs)
        no_adj = []
        for i in range(x):
            for j in range(i+1,x):
                if grafo.get_eid(i,j,error = False,directed = False) == -1:
                    no_adj.append((i,j))
        return no_adj
def verificar_fechado(grafo:Graph):
    verificar = len(grafo.vs)
    for i in grafo.vs:
        if(i.degree() < verificar -1):
            return False
    return True