try:
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))
    print(x/y)

except zerodivisionerror:
    print("can't divide with zero")
except valueerror:
    print("pleace provide int value only")
