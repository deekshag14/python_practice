t=()
print("datatype:",type(t))
print("t:",t)
t1=(1,2,3,4,5)
print("t1:",t1)
t2=11,22,33
print("datatype of t2:",type(t2))
print("t2:",t2)
print("third element of t2 is:",t2[2])
t3=tuple(range(1,6))
print("t3:",t3)
num_list=[333,444,555,666]
t4=tuple(num_list)
print("t4:",t4)
t5=(1,2,3,4,5,6,7,8,9)
for i in t5:
   print(i*i)

   t6=(111,)
   print("t6:",t6)
   print("datatype t6:",type(t6))

   t7=(1,2,3,True,"pune",[1,2,3],3.14)
   print("t7:",t7)
