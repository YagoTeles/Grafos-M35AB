class trabalho:
    estados = ['RS', 'SC', 'PR', 'MS', 'SP', 'RJ', 'ES', 'MG', 'GO', 'MT', 'RO', 'AC', 'AM', 'RR',
               'PA', 'AP', 'MA', 'TO', 'DF', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA']

    def __init__(self, vert):
        self.arestas = 1
        self.vert = vert
        self.graphs = [[0] * self.vert for i in range(self.vert)]
        self.vetor = self.graphs

    def add_arrest(self, x, y):
        self.graphs[x-1][y-1] = 1
        self.arestas += 0.5

    def show_matrix(self):
        estados = trabalho.estados
        print()
        print('Matriz:')
        for j in range(self.vert):
            print(estados[j], self.graphs[j])

    def soma(self):
        contador = 0
        estados = trabalho.estados
        soma2 = []
        for i in range(self.vert):
            soma2.append(sum(self.graphs[i]))

        maximo = max(soma2)
        print("Maximo de vizinhos: ", end=" ")
        while(1):

            if(max(soma2) == maximo):
                print(estados[soma2.index(max(soma2))+contador], end=": ")
                for i in range(self.vert):
                    if(self.graphs[soma2.index(max(soma2))+contador][i] == 1):
                        print(estados[i], end=" ")

                soma2.remove(max(soma2))
                contador += 1
            else:
                contador = 0
                break
        print()
        print("Minimo de vizinhos: ", end=" ")
        minimo = min(soma2)
        while(1):
            if(min(soma2) == minimo):
                print(estados[soma2.index(min(soma2))+contador], end=": ")
                for i in range(self.vert):
                    if(self.graphs[soma2.index(min(soma2))+contador][i] == 1):
                        print(estados[i], end="   ")
                soma2.remove(min(soma2))
                contador += 1
            else:
                print("")
                contador = 0
                break

    def densidade(self):
        print("Densidade do Grafo: ", end=" ")
        print(self.vert/(self.arestas+1))

    def freq(self):
        soma2 = []
        for i in range(self.vert):
            soma2.append(sum(self.graphs[i]))
        contador = 0
        print()
        print("Frequencia do Grau dos Vertices: ")
        print("       Grau  Frequencia")
        for i in range(min(soma2), max(soma2)+1):
            contador = 0
            print("         ", end="")
            print(i, end="        ")
            for j in range(self.vert):
                if(i == soma2[j]):
                    contador += 1

            print(contador)
    def traco(self):
        print("--------------------------------------------------------------------------------------")