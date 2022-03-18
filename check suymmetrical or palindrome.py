n=input("Enter the string that you want to check: ")
a=len(n)
b=a//2
start=n[:b]
end=n[b:]
print(start)
print(end)
if(start==end):
    print("Number is symmetrical ")
else:
    print("Number is not symmetrical")
if(n[: :]==n[-1: :-1]):
    print("string is palindrome")
else:
    print("String is not palindrome :")
