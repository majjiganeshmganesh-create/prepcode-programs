try:
    a = int (input("enter number:"))
    b = int(input("enter another number:"))
    print("result:",a / b)
except ZeroDivisionError:
    print("can't divide by zero")
except ValueError:
    print("please enter vaild number")