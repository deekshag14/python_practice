"""
1.create tuple of numbers 1 to 10
"""
num_tuple=tuple(range(1,11))
print("tuple is:",num_tuple)
"""
2.create single value tuple
"""
single_val_tup=(4)
print(type(single_val_tup))
"""
3.create one number element tuple and square all the elements in that tuple and store in new list
"""
number_tuple=tuple(range(1,11))
print("number tuple:",number_tuple)
op_list=[]
for number in number_tuple:
    op_list.append(number**2)
print("final output list is:",op_list)
"""
4.write a python program to create a tuple
"""
t1=(1,2,3,4,"a","b",7,True)
print("t1:",t1)
t2=1,2,3,4
print("t2:",t2)
t3=tuple(range(1,6))
print("t3:",t3)
l=[11,22,33]
t4=tuple(l)
print("t4:",t4)
"""
5.write a python program to create a tuple with different datatypes
"""
t1=(1,2,3,"pune",True,"A",3.14)
print("t1:",t1)
"""
6.write a python program to create a tuple of numbers and print second item.
"""
t1=tuple(range(1,6))
print("t1:",t1)
print(t1[1])
"""
7.write a python program to unpack a tuple in to several variables.
"""
a=20
b=30
c=40
#packing
t=a,b,c
print(type(t))
#unpacking
x,y,z=t
print("x:",x)
print("y:",y)
print("z:",z)
"""
9.write a python program to convert a list to a tuple
"""
num_list=list(range(1,6))
print("list is:",num_list)
num_tuple=tuple(num_list)
print("tuple is:",num_tuple)
"""
10.write a python program to find the length of a tuple without using len function
"""
t1=tuple(range(1,6))
print("t1:",t1)
c=0
for t in t1:
    c +=1
print("length of tuple is:",c)
"""
11.write a python program to reverse a tuple
"""
t1=(1,2,3,4,5,6,7,8,9,32,9,42)

op_t=reversed(t1)
print("output tuple:",op_t)
print("original tuple:",t1)
"""
12.write a python program to convert a list of tuples in to a dictionary
"""
l1=[("a",100),("b",200),("c",300)]
print("list is:",l1)
d1=dict(l1)
print("dictionary:",d1)
"""
13.write a python program  to calculate the product multiplying all the numbers in a given type
"""
num_tuple=tuple(range(1,11))
print("number tuple is:",num_tuple)
m=1
for num in num_tuple:
    m*=num #m=m*num
print("multiplication of all numbers:",m)
"""
14.write a python program to calculate the average value of the numbers in a given tuple
"""
num_tuple=tuple(range(1,11))
print("original tuple is:",num_tuple)
s=0
for num in num_tuple:
    s +=num
print("sum is:",s)
avg=s/len(num_tuple)
print("average is:",avg)
"""
15.write a python program to convert a tuple of string values to a tuple of integar values
"""
string_num_tup=("1","2","3","4","5")
print("string num tuple:",string_num_tup)
l_str=list(string_num_tup)
num_list=[]
for num in string_num_tup:
    num_list.append(int(num))
print("number list:",num_list)
num_tuple=tuple(num_list)
print("final output tuple:",num_tuple)
"""
16.write a python program to convert a given list of tuples to a lists of lists
"""
list_of_tup=[("A","a"),("B","b"),("C","c")]
print("list of tuple:",list_of_tup)
op_list=[]
for t in list_of_tup:
    op_list.append(list(t))
print("Final output list:",op_list)
"""
17.write a python program to get size of tuple
"""
from sys import getsizeof
t=tuple(range(1,11))
print("tuple is :",t)
print("size of tuple is:",getsizeof(t))
"""
18.create one list and one tuple with same elements and compare their sizes
"""
num_list=list(range(1,11))
print("number list:",num_list)
num_tuple=tuple(range(1,11))
print("number tuple:",num_tuple)
print("size of list is:",getsizeof(num_list))
print("size of tuple is:",getsizeof(num_tuple))
"""
19.get count a particular element in tuple
"""
num_tuple=(1,2,1,2,3,4,5,6,1,2,3,4)
print("original tuple:",num_tuple)
s=set(num_tuple)
for n in s:
    print("number is :",n,"count is:",num_tuple.count(n))
"""
20.write a python program to get the 4th element from a last  of a tuple
"""
t=tuple(range(1,11))
print("tuple is:",t)
print("4th element from first part:",t[3])
print("4th element from last part:",t[-4])
        



         
