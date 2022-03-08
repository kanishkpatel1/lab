n=int(input("Enter any number that you want to check : "))
temp=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(temp==rev):
    print(temp," is palindrome")
else:
    print(temp,"is not palindrome ")