from math import inf

class grafo_():

    def __init__(self, vert):
        self.vert = vert
        self.grafo = [[0] * self.vert for i in range(self.vert)]
        self.grafo_ = [];self.caminho = [];self.print = [];self.caminho_letras = []
        self.stx = ["s","t","x","y","z"];self.sabc =["s","a","b","c","d","e","f","g"]
        self.letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M"
                    ,"N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
        
    def add_edge(self, x, y,peso):
        self.grafo_.append([x, y, peso])

    def add_edges(self, lista,mode = "num"):
        if mode == "num":
            for i in range(len(lista)):
                tmp = lista[i].split()
                v1 = int(tmp[0])
                v2 = int(tmp[1])
                peso = int(tmp[2])
                self.grafo[v1][v2] = peso
                self.grafo_.append([v1, v2, peso])

    def escr(self, dist,mode = "num"):
        self.print.append("Vertice | Distancia\n\n")
        if mode == "num" :
            for i in range(self.vert):
                self.print.extend(["\t",str(i),"\t|\t",str(dist[i]),"\n"])
            self.print.append("____________________\n")
        if mode == "stx":
            for i in range(self.vert):
                self.print.extend(["\t",self.stx[i],"\t|\t",str(dist[i]),"\n"])
            self.print.append("____________________\n")
        if mode == "sabc":
            for i in range(self.vert):
                self.print.extend(["\t",self.sabc[i],"\t|\t",str(dist[i]),"\n"])
            self.print.append("____________________\n")
    
    def escrCaminho(self, parent:list, j,origem):
            if parent[j] == -1:
                try:
                    parent.index(j)
                except:
                    return "except"
                self.caminho.extend([str(j)," -> "])
                self.caminho_letras.extend([self.letras[j]," -> "])
                return

            self.escrCaminho(parent , parent[j],origem)
            self.caminho.extend([str(j)," -> "])
            self.caminho_letras.extend([self.letras[j]," -> "])

    def escrever(self, dist, parent,origem):

        self.caminho.append("_________________________________\n")
        self.caminho.extend(["Vertice |"," Caminho Percorrido\n\n"])
        self.caminho_letras.append("_________________________________\n")
        self.caminho_letras.extend(["Vertice |"," Caminho Percorrido\n\n"])

        for i in range(0, len(dist)):
            self.caminho.extend(["\t",str(i),"\t| "])
            self.caminho_letras.extend(["\t",self.letras[i],"\t| "])

            if self.escrCaminho(parent,i,origem) != "except": 
                del self.caminho[-1:]
                del self.caminho_letras[-1:]
                self.caminho.append("\n")   
                self.caminho_letras.append("\n")
            else:
                self.caminho.append("Caminho n??o existe\n")
                self.caminho_letras.append("Caminho n??o existe\n")
                

        self.caminho.append("_________________________________\n")
        self.caminho.extend(["Vertice |"," Menor Caminho \n\n"])
        self.caminho_letras.append("_________________________________\n")
        self.caminho_letras.extend(["Vertice |"," Menor Caminho \n\n"])

        for vert in range(self.vert):

            if dist[vert] == inf: 
                self.caminho.extend(["\t",str(vert),"\t| ","Caminho n??o existe\n"])  
                self.caminho_letras.extend(["\t",self.letras[vert],"\t| ","Caminho n??o existe\n"]) 
            else: 
                self.caminho.extend(["\t",str(vert), "\t|\t", str(dist[vert]),"\n"])
                self.caminho_letras.extend(["\t",self.letras[vert], "\t|\t", str(dist[vert]),"\n"])
                
        self.caminho.append("_________________________________\n")
        self.caminho_letras.append("_________________________________\n")


    def lista_caminho(self,mode="num"):
        if mode == "num":return self.caminho
        if mode == "letra":return self.caminho_letras
        
    def show_matrix(self):
        print('Matriz:')
        for j in range(self.vert):
            print(self.grafo[j])

    def dijkstra(self, origem):
        if type(origem) == str:
            origem = self.letras.index(origem.upper())
        dist = [inf] * self.vert
        dist[origem] = 0
        parente = [-1] * self.vert
        fila = []

        for i in range(self.vert):
            fila.append(i)

        while fila:
            
            min = inf
            min_index = -1
            for i in range(self.vert):
                if dist[i] < min and i in fila:
                    min = dist[i]
                    min_index = i
            u = min_index
            
            try:
                fila.remove(u)    
            except:
                break
            
            for i in range(len(self.grafo[0])):
                if self.grafo[u][i] and i in fila:
                    if dist[u] + self.grafo[u][i] < dist[i]:
                        dist[i] = dist[u] + self.grafo[u][i]
                        parente[i] = u

        self.escrever(dist,parente,origem)

    def bellman_ford(self, origem,mode = "num"):
        if type(origem) == str:
            origem = self.letras.index(origem.upper())
        dist = [inf] * self.vert
        dist[origem] = 0
        parente = [-1] * self.vert

        for _ in range(self.vert - 1):
            for y, x, peso in self.grafo_:
                if dist[y] != inf and dist[y] + peso < dist[x]:
                    dist[x] = dist[y] + peso

        for x, y, peso in self.grafo_:
            if dist[x] != inf and dist[x] + peso < dist[y]:
                print("Grafo cont??m ciclo de peso negativo")
                return

        self.escr(dist,mode)




    