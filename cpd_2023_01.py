
###########shell sort#############

file = open('entrada1.txt', 'r')
data = file.read()
clean_data=data.replace(' ', ',')
file.close()
array=[]
with open('entrada1.txt', 'r') as f:
    for line in f.readlines():
        array.append(line)
    
print(array[1])

# ['0', '0', '200', '0', '53', '1', '0', '255', '1.5', '2.5', '3.5', '4.5', '5.5', '0.1', '0.2', '0.3', '0.4', '0.5']
c=[16, 14, 12, 1, 8 ,4, 9 ,6, 15, 13, 11, 2, 7, 3, 10, 5]

shell=[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
knut=[1,4,13,40,121,364,1093,3280,9841,29524,88573,265720,797161,2391484]
ciura=[1,4,10,23,57,132,301,701,1577,3548,7983,17961,40412,90927,204585,460316,1035711]

def insdiretashell(c,s,f,h):
    for j in range(f+h,s,h):
        chave=c[j]
        i=j-h
        while i>0 and c[i]>chave: ### pseudo codigo diz i >0
            c[i+h]=c[i]
            i=i-h
        c[i+h]= chave
    # print(c,"incr= %d" %h)


def shell_sort(c,n,vec):
    p=1
    while vec[p] < len(c):
        p=p+1
    while  p >= 0 :
        h = vec[p]
        p=p-1
        j=1
        while j <= h:
        # for j in range (1,h+1):
            insdiretashell(c,n,j,h)
            j=j+1
        print(c,"incr= %d" %h, "%d")

shell_sort(c,len(c),ciura)
##print(c)

d=[ciura,shell,knut]

for i in d:
    shell_sort(c,len(c),i)