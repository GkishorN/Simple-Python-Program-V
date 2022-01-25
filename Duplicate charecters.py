str1=input("Enter the string:")
a=[]
b=0
c=[]
for i in range(0,len(str1)):
        if(str1[b]==str1[i]):
            flag=0
            for j in a:
                if(j==str1[i]):
                    flag=1
            if(flag==0):
                a.append(str1[i])
        b=b+1
for i in a:
    counter=0
    for j in str1:
        if(i==j):
            counter=counter+1
    if(counter>1):
        c.append(i)
for i in c:
    print(i)
