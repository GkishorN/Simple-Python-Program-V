a=[1,2,3,4,5]
b=len(a)
temp=a[0]
a[0]=a[b-1]
a[b-1]=temp
print(a)
