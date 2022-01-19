l=[['Gfg', 'good'], ['is', 'for']]
b=[]
for i in range(0,len(l[0])):
               a=""
               for j in range(0,len(l)):
                       a=a+l[j][i]
               b.append(a)
print(b)
