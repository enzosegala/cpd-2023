import numpy as np
array=[]
with open('entrada1.txt', 'r') as f:
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
    


def quicksort(A,p,r):
    if p <r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)        
        quicksort(A,q+1,r)

print(quicksort(array_novo[0],0,len(array_novo)))
print(array_novo[0])