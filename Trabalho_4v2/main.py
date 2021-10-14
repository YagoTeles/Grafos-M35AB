from trabalho4 import trabalho_4
from grafo import add

ler = open('brasil.txt')
gravar = open('gravar.txt','w', encoding="UTF-8")


origem = int(ler.readline())
arestas = ler.read().splitlines()

ler.close()
#origem = int(input("Informe o Nó raiz: "))
grafo = add(arestas)
grafo.adicionar()
grafo.plotar_grafo('kk','br')
grafo_arv = trabalho_4(origem,grafo.grafo_())
grafo_arv.plotar_arv('br')


gravar.write("Graus (Máximo,Médio e Mínimo): \n")
gravar.write(grafo.max_grau())
gravar.write(grafo.min_grau())
gravar.write(grafo.grau_medio())
gravar.write("======================================= \n")
gravar.write("Distância do nó " + str(origem) + " para cada vértice: \n")
gravar.writelines(grafo_arv.distancia())
gravar.write("======================================= \n")
gravar.write("O caminho percorrido para cada vértice: \n")
gravar.writelines(grafo_arv.caminho())
gravar.write("======================================= \n")

gravar.close()

