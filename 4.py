x={}
n=int(input("Enter the value of n: "))
for i in range(1,n+1):
    
    v=0
    a=1
    c=a+v
    v=a
    a=c
    x.update({i:v})
    
print(x)