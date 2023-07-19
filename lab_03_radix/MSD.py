A=[]
with open("test1.txt",'r') as f:
    for line in f.readlines():
        A.append(line)


R =256
M=15
aux=[]
def charAT(s,d):
    if d<len(s):
        return s.charAT(d)
    else:
        return

def sort1(A):
    n=len(A)
    aux=[]*n
    sort(A,0,n-1,aux)

def sort(A,low,hi,d):
    d=int(d)
    if(hi<=low+M):
        insertion_sort(A,low,hi,d)
    new=[R+2]
    count= new
    for i in range(low,hi+1):
        c= charAT(A[i],d)
        count+=count[c+2]

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

def insertion_sort(A,low,hi,d):
    for i in range(low,hi+1):
        j=i
        while j>low and less(A[j],A[j-1],d):
            j-=1
            swap(A,j,j-1)

def swap(A,i,j):
    (A[i],A[j])=(A[j],A[i])

def less(v,w,d):
    for i in range(d,min(len(v),len(w))):
        if (v.charAt(i) < w.charAt(i)): 
            return True
        if (v.charAt(i) > w.charAt(i)): 
            return False
    return len(v)< len(w)

sort1(A)
for i in range(0,len(A)+1):
    print(A[i])