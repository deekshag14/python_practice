#without filter function
def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20,25,30]
l1=list(filter(isEven,l))
print(l1) #output:[0,10,20,30]

#with lambda function
l=[0,5,10,15,20,25,30]
l1=list(filter(lambda X:X%2==0,l))
print(l1)

list_num=[1,2,3,4,5,6]
def sq_num(x):
    return x*x

result_list=list(map(sq_num,list_num))
print("result list:",result_list)

list_num=[1,2,3,4,5,6]
sq_list=list(map(lambda x:x*x,list_num))
print("sq_list:",sq_list)

from functools import reduce
num_list=[10,20,30,40,50]
add_result=reduce(lambda x,y:x+y,num_list)
print("Addition result:",add_result)

def fun_print():
    print("Hello")
print(fun_print)
print(id(fun_print))
print(type(fun_print))



