from igraph import Graph
def testar_euleriano(grafo: Graph):
    n = len(grafo.vs)
    testar = 0
    for i in grafo.vs:
        if (grafo.degree(i)%2 == 0):
            testar += 1
    if (testar == n): return print("É um grafo Euleriano")
    elif((n - testar) > 2): return print("É um grafo nao Euleriano")
    elif((n-testar) == 2): return print("É um grafo Semi-Euleriano")