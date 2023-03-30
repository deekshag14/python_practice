def outer_fun():
    print("outer function")
    
    def inner_fun():
        print("inner function")

    return inner_fun#we are returning address of the function

ret_val=outer_fun()
#print("return value:",ret_val)
#print("return value:",ret_val)
print("type of return value:",type(ret_val))
    
