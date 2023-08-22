# 2.1 tabela hash guardar media de informacao e total de avaliacoes para cada jogador.
# Para responder esta pesquisa deve-se implementar uma arvore trie, buscando o nome ou prefixo e depois busca na tabela hash o complemento.

# 2.2retornar a lista com max 20 jogadorews revisados pelo  usuario contendo .... ordenado

# 2.3 
from csv import reader
from hash import *
from trie import *
import time 
seconds = time.time()

def csv_read(filename):
    with open(filename,"r",encoding="utf8") as file:
        next(file)
        for line in file:
        # lines = reader(file)
            yield line.split(",")


def mean(a):
    z=0
    for i in range(len(a)):
        z+=a[i]
    return float(z/len(a))


if __name__ == "__main__":
    file_path = "rating.csv"
    # data_rating = csv_read(file_path)
    
        
    file_path2 = "players.csv"
    # data_players= csv_read(file_path2)   

    # print(len(data_players))
    data_players_len=18.944
    start = time.time()



    tabela_hash = Hash_table(int(data_players_len*1.3))#vi que 'e um rule of dedao
    trie_tree=trie()
    tabela_hash_players=Hash_table(int(data_players_len*1.3))

    #for i in data_rating[1:]:
    matriz=[]
    for row in csv_read(file_path): 
        tabela_hash.insersao(float(row[2]),int(row[1]),int(row[0]),None)
    for row in csv_read(file_path2):
        trie_tree.insersao(row[1])
        tabela_hash_players.insersao(float(row[2]),int(row[1]),int(row[0]),None)

    done = time.time()
    
    for i in tabela_hash:
        if i != 0:
            a,b=tabela_hash_players.pesquisa(i.idfifa)
            tamanho=len(a)
            a_media=mean(a)

    a=(trie_tree.prefixo('Lion '))
    print(a) 
    elapsed = done - start
    print(elapsed)