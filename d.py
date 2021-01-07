def lsort(lista):
    result=[]
    for i in lista:
        result.append(int(i))
    result.sort()
    return result
inputn=input()
inputlist=inputn.split(',')
s=lsort(inputlist)
for i in s:
    print(i,end=" ")
