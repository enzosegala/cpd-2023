
import numpy as np
A=[]
with open("war_and_peace.txt",'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        A.extend(line.split())
def less(v,w,d):
    for i in range(d,min(len(v),len(w))):
        if (charAT(v,i) < charAT(w,i)): 
            return True
        if (charAT(v,i) > charAT(w,i)): 
            return False
    return len(v)< len(w)

# def charAT(s, d):
#     if d<len(s):
#         return charAT(s,d)
#     else: 
#         return -1
def charAT(s, d):
    # assert d >= 0 and d <= len(s)
    # if (d == len(s)): 
    #     return -1
    # else:
    #     return charAT(s,d)
    if len(s) <= d:
        return -1
    else:
        return ord(s[d])

def swap(A,i,j):
    (A[i],A[j])=(A[j],A[i])


# def insertion_sort(A,low,hi,d):
#     for i in range(low,hi+1):
#         j=i
#         while j>=low and less(A[j],A[j-1],d):
#             j-=1
#             swap(A,j,j-1)

def insertion_sort(A):
     for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and key < A[j] :
                A[j + 1] = A[j]
                j -= 1
        A[j + 1] = key

R=256
M=15
aux=[]

def sort1(A):
    n=len(A)
    print(n)
    aux=[0]*n
    sort(A,0,n-1,0,aux)

def sort(A,low,hi,d,aux):

    if(hi<=low+M):
        # insertion_sort(A,low,hi,d)
        insertion_sort(A)
        return
    count=[0]*(R+2)
    for i in range(low,hi+1):
        c= charAT(A[i],d)
        # count+=count[c+2]###checar
        count[c+2]+=1

    for r in range(0,R+1):
        count[r+1]+=count[r]

    for i in range(low,hi+1):
        c= charAT(A[i],d)
        aux[count[c+1]] = A[i]
        count[c+1]+=1
    for i in range(low,hi+1):
        A[i]=aux[i-low]
    for r in range (0,R):
        sort(A, low + count[r], low + count[r+1] - 1, d+1, aux)


sort1(A)
for i in range(0,len(A)):
    print(A[i])

with open('war_and_peace_sorted.txt.txt', 'w') as f:
        f.write(A)
        f.write('\n')