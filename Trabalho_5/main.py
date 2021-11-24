from trabalho5 import trabalho_5
from grafo import add

ler = open('prova.txt')
gravar = open('gravar.txt','w', encoding="UTF-8")


origem = int(ler.readline())
arestas = ler.read().splitlines()

ler.close()
origem = int(input("Informe o Nó raiz: "))
grafo = add(arestas)
grafo.adicionar()
grafo.plotar_grafo('lgl')
grafo_arv = trabalho_5(origem,grafo.grafo_())
grafo_arv.plotar_arv(dfs='r')


gravar.write("Caminho percorrido usando a DSF Recursiva: \n")
#gravar.writelines(grafo_arv.caminho_DFS_recursivo()) 
gravar.write("\n\nCaminho percorrido usando a DSF em Pilha: \n")
#gravar.writelines(grafo_arv.caminho_DFS_pilha())
gravar.write("\n\nCaminho percorrido porem descobrindo os vertices de maior valor primeiro: \n")
#gravar.writelines(grafo_arv.caminho_DFS_pilha('maior'))



gravar.close()

