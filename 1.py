try:
    a=int(input("Enter the number :"))
    b=int(input("Enter the number:"))
    c=a/b
    print(c)    
# except ZeroDivisionError:
#     print("zero division error")
# except ValueError:
#     print("value error")
except Exception as e:
    print("Error in this code is:",e)
else:
    print("No error occured:")
finally:        #thios block always execute weather error came or not
    print("kanishk")
    