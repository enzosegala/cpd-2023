import numpy as np
import time
recur=0

########################## leitura ##########################
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
################################# funções ##############
def swap(i,j):
    # temp = i
    # i = j
    # j= temp 
    (i, j) = (j,i)

def funcao_mediana(ini,meio,fim):
    if ini<meio:
        if meio<fim:
            return meio
        else:
            if ini<fim:
                return fim
            else:
                return ini
    else:
        if fim <meio:
            return meio
        else:
            if fim< ini:
                return fim
            else:
                return ini    


####  A = vetor de entrada
####  p = indice menor elemento
####  r = indice maior elemento
# def partition_lomuto(A,p,r):
#     global n_swaps
#     chave = A[r]
#     storeindex= p-1

#     for i in range(p,r,1):
#         if A[i]<chave: 
            
#             swap(A[i],A[storeindex])
#             storeindex+=1 
#             n_swaps+=1
#             # swap(A[i],A[i+1]) 
#     swap(A[r],A[storeindex+1])
#     return(storeindex+1)

def partition_lomuto(arr, low, high):
     
    # pivot
    pivot = arr[high]
     
    # Index of smaller element
    i = (low - 1)
    for j in range(low, high):
         
        # If current element is smaller than or
        # equal to pivot
        if (arr[j] <= pivot):
             
            # increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
     

def partition_hoare(A,p,r):
    chave =A[p]
    i=p
    j=r
    while(i<j):
        while(A[j] > chave and i<j):
            j-=1
            A[i]=A[j]
        while(A[i] <= chave and i < j ):
            i+=1
            A[j]=A[i]
    A[j]=chave
    return i 


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


#####################chamada quicksort ##############


    ############################# random 
def random_quicksort(A,p,r):
    if r > p:
        aleatorio = int(np.random.uniform(p,r)) ###checkar numpy
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

def quicksort_lomuto(A,p,r):
    if p<r: 
        global recur 
        recur+=1
        print(r)
        q=partition_lomuto(A,p,r)
        quicksort_lomuto(A,p,q-1) 
        quicksort_lomuto(A,q+1,r)
        # return#,n_swaps+n_swaps2

def quicksort_hoare(A,p,r):
    if p <r:
        q=partition_hoare(A,p,r)
        quicksort_hoare(A,p,q-1)        
        quicksort_hoare(A,q+1,r)                
#################### mediana


def mediana_quicksort_hoare(A,p,r):
    if p<r:
        mediana=funcao_mediana(A[p],A[(len(A[1:])-1)//2],A[r])
        q=partition_hoare(A,p,mediana)
        quicksort_hoare(A,p,q-1)        
        quicksort_hoare(A,q+1,r)
        

def mediana_quicksort_lomuto(A,p,r):
    if p<r:
        global recur
        recur=0
        global n_swaps
        n_swaps=0
        mediana=funcao_mediana(A[p],A[(len(A[1:])-1)//2],A[r])
        q=partition_lomuto(A,p,mediana)
        
        quicksort_lomuto(A,p,q-1)        
        quicksort_lomuto(A,q+1,r)
        
        return A
###########################3

print(mediana_quicksort_lomuto(array_novo[0],1,len(array_novo[0])-1))
# with open('stats-mediana-lomuto.txt.txt', 'w') as f:
#     for i in range(0,5):
#         st = time.time()
#         mediana_quicksort_lomuto(array_novo[i],1,len(array_novo[i])-1)
#         et = time.time()
#         f.write('TAMANHO ENTRADA %i'%(len(array_novo[i])-1))
#         f.write('\n')

#         f.write('SWAPS %i'%n_swaps)
#         f.write('\n')

#         f.write('RECURSOES %i' %(recur))
#         f.write('\n')

#         f.write('TEMPO %f'%(et-st))
#         f.write('\n')


