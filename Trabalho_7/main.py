from grafo import grafo_

ler = open('problema1.txt');ler2 = open('problema2.txt')                               
gravar = open('gravar.txt','w', encoding="UTF-8")

try:
    input = input("Digite o vertice inicial:")
    origem = int(input)
except ValueError:origem = input
    
g = grafo_(int(ler.readline()))
g2 = grafo_(int(ler2.readline()))

arestas = ler.read().splitlines()
arestas2 = ler2.read().splitlines()

g.add_edges(arestas,mode="num")
g2.add_edges(arestas2,mode="num")

ler.close()

gravar.write("Problema 1: \n")
g.bellman_ford(origem)
gravar.writelines(g.lista_caminho(mode="stx"))
gravar.write("\nProblema 2: \n")
g2.bellman_ford(origem)
gravar.writelines(g2.lista_caminho(mode="sabc"))
