class Nodo:
    def __init__(self, rating,idfifa,id):
        self.rating = rating
        self.idfifa = idfifa
        self.id = id 
        self.num = 0
        self.next = None


class Hash_table:
    def __init__(self,M):
        self.M = M #tamanho
        self.array=[0]*M
        self.contador=0

    def fhash(self, idfifa):
        return int(idfifa) % self.M
    
    def insercao(self,rating,idfifa,id):
        indice= self.fhash(idfifa)
        if self.array[indice]==None:
            self.array[indice] = Nodo(rating,idfifa,id)
            self.contador+=1

        else:
           novo_nodo=Nodo(rating,idfifa,id)
           novo_nodo.next = self.array[indice]
           self.array[indice]=novo_nodo
           self.contador+=1
    
    def pesquisa(self,idfifa):
        indice= self.fhash(idfifa)
        # node = Nodo(self.array[indice].rating,self.array[indice].idfifa,self.array[indice].id)
        node=self.array[indice]
        # nodo_atual = Nodo(node.rating,node.idfifa,node.id)
        rat=[]
        while node != 0:  
            if node.idfifa == idfifa:
                print(node.next)
                rat.append(node.rating)
            node=node.next
        return rat,self.array[indice]

