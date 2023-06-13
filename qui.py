import numpy as np
array=[]
with open('entrada-quicksort.txt', 'r') as f:
    for line in f.readlines():
        # array.append(line.replace(' ', ',')[:-2])
        array.append(line)
array= np.char.split(array)
# array=np.array(array,dtype=np.int)

array_temp=[]
array_novo=[] 

for x in array:    
    for y in x:
        
        array_temp.append(int(y))
        # array_temp=np.array(array_temp,dtype=int)
    array_novo.append(array_temp)
    
    array_temp=[]
#################################
def swap(i,j):
    # temp = i
    # i = j
    # j= temp 
    (i, j) = (j,i)



def partition_lomulos(A,p,r):
    chave = A[p]
    storeindex= p+1
    # for i in range(p+1,r+1):#### r +1 pq é nao inclusivo
    i=p+1
    while(i<=r):
        i+=1
        if A[i]<=chave:
            swap(A[i],A[storeindex])
            storeindex+=1
    swap(A[p],A[storeindex-1])
    return storeindex -1 


def partition_hoare(A,p,r):
    chave=A[p]
    while(p<r):
        while(A[r] > chave and p < r):
            r-=1
            A[p] = A[r]
        while(A[p] <= chave and p < r):
            p+=1 
            A[r] = A[p]
    A[p]=chave
    return p



def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            (A[i], A[j]) = (A[j], A[i])
            # temp=A[i]
            # A[i]=A[j]
            # A[j]=temp
    (A[i + 1], A[r]) = (A[r], A[i + 1])
    # temp2=A[i+1]
    # A[i+1]=A[r]
    # A[r]=temp2
    return i+1
    ############################# random 
def random_quicksort(A,p,r):
    if r > p:
        aleatorio = np.random ###checkar numpy
        temp=A[p]
        A[p]=A[aleatorio]
        A[aleatorio]=temp
        q=partition(A,p,r)
        quicksort(A,p,q-1)        
        quicksort(A,q+1,r)

#################### tradicional
def quicksort(A,p,r):
    if p <r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)        
        quicksort(A,q+1,r)
#################### mediana


def mediana_quicksort(A,p,r):
    if p <r:
        vec=[]
        vec=[A[p],A[(len(A)-1)//2],A[r]]
        mediana=np.median(vec) ## calculo alternativo
        mediana=int(mediana)
        # q=partition(A,p,mediana)
        # q=partition_lomulos(A,p,mediana)
        q=partition_hoare(A,p,mediana)

        quicksort(A,p,q-1)        
        quicksort(A,q+1,r)
print(array[0])
mediana_quicksort(array_novo[0],0,len(array_novo[0])-1)

######################### 



print(array_novo[0])