add_number=lambda a,b:a+b
print(add_number(10,20))

square_number=lambda a:a*a
print(square_number(20))

#without filter function
def isEven(x):
    if x%2==0:
        return True
    else:
        return False
    l=[0,5,10,15,20,25,30]
    l1=list(filter(isEven,l))
    print(l1) #output:[0,10,20,30]

