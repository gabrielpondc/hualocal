i=int(input('Enter a 3-digit integer:'))
d1=i%10
d2=i%100//10
d3=i//100
print(str(d1)+"\n"+str(d2)+"\n"+str(d3),end= ' ')
