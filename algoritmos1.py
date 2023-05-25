c=[1,10,20,3,2,5,6,43,336,7,2,5,34,67]

# def insertion_sort(c,n):
#     for j in range(1,n):
#         chave = c[j]
#         i = j-1
#         while i>0 and c[i]>chave:
#             c[i+1]=c[i]
#             i=i-1
#         c[i+1]=chave
#     return c

# c_ordenado=insertion_sort(c,len(c))
# print(c_ordenado,"insertion sort")

# ######## insertion sort com binary search #########
    
def insertion_sort_binario(c,n):
    for j in range(1,n):
        chave = c[j]
        i =  binary_search(c,chave,0,j)+1
        for z in range(j,i,-1):
            c[z]=c[z-1]
        c[i]=chave
    return c

def  binary_search(c,chave,inicio,fim):
     
    if fim - inicio <=1:
        if chave < c[inicio]:
            return inicio - 1
        else:
            return inicio
    
    meio = (inicio+fim)//2
    if c[meio]<chave:
        return binary_search(c,chave,meio,fim)
    if c[meio]>chave:
        return binary_search(c,chave,inicio,meio)
    else: 
        return meio

c_ordenado=insertion_sort_binario(c,len(c))
print(c_ordenado,"insertion sort com binary")

###########shell sort##############



def insdiretashell(c,s,f,h):
    j = f+h
    while j < s:
        chave=c[j]
        i=j-h
        j=j+h
        while i>0 and c[i]>chave:
            c[i+h]=c[i]
            i=i-h
        c[i+h]= chave


def shell_sort(c,np,n):
    p = np
    while  p >= 1 :
        h = 2**(p-1)
        p=p-1
        j=1
        while j <= h:
            insdiretashell(c,n,j,h)
            j=j+1

shell_sort(c,8,len(c))
print(c)


########## shell sort 2 


def insdiretashell(c,s,f,h):
    j = f+h
    while j < s:
        chave=c[j]
        i=j-h
        j=j+h
        while i>0 and c[i]>chave:
            c[i+h]=c[i]
            i=i-h
        c[i+h]= chave


def shell_sort(c,np,n):
    p = np
    while  p >= 1 :
        h = 2**(p-1)
        p=p-1
        j=1
        while j <= h:
            insdiretashell(c,n,j,h)
            j=j+1

shell_sort(c,8,len(c))
print(c)