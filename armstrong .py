n=int(input("Enter the number that you want to check : "))
temp=n
leng=len(str(n))
sum=0
while (temp>0):
    c=temp%10
    sum+=c**leng
    temp=temp//10


if n==sum:
    print("Number is armstrong!")
else:
    print("number is Not armstrong")
