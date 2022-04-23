# Enter the value of n: 4
# {1: 1, 2: 4, 3: 9, 4: 16}
x={}
n=int(input("Enter the value of n: "))
for i in range(1,n+1):
    
    v=i**2
     
    x.update({i:v})
print(x)