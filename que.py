
#write a program when user input a negative number then raise a error and print that:
try:
    a=int(input("Enter the number"))
    if(a<0):
        raise ValueError
except ValueError:
    print("Number")
    
