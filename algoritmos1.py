c=[1,10,20,3,2,5,6,43,336,7,2,5,34,67]

def insertion_sort(c,n):
    for j in range(1,n):
        chave = c[j]
        i = j-1
        while i>0 and c[i]>chave:
            c[i+1]=c[i]
            i=i-1
        c[i+1]=chave
    return c

c_ordenado=insertion_sort(c,len(c))
print(c_ordenado,"insertion sort")

######## insertion sort com binary search #########
    
def insertion_sort_binario(c,n):
    for j in range(1,n):
        chave = c[j]
        i =  binary_search(c,chave,0,j)
        while i>0 and c[i]>chave:
            c[i+1]=c[i]
            i=i-1
        c[i+1]=chave
    return c

def  binary_search(c,chave,inicio,fim):
    ### caso 
    if fim - inicio <=1:
        if chave < c[inicio]:
            return inicio - 1
        else:
            return inicio
    ## caso 
    meio = (inicio+fim)//2
    if c[meio]<chave:
        return binary_search(c,chave,meio,fim)
    if c[meio]>chave:
        return binary_search(c,chave,inicio,meio)
    else: 
        return meio

c_ordenado=insertion_sort_binario(c,len(c))
print(c_ordenado,"insertion sort com binary")