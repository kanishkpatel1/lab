n=int(input("enter the number : "))
num=n
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("Number in reverse is ",rev)
if(rev==num):
    print("Number is palindrome :")
else:
    print("Number is not palindrome : ")