def add_fun(a,b,c):
    t=a+b+c
    print(t)
    
add_fun(10,20,30)
#add_fun(10,20)

def ad_function(*args):
    print("args are:",args)
    print("type of args:",type(args))

    ad_function()
    ad_function(1)
    ad_function(1,2)
    ad_function(1,2,3,4,5)




