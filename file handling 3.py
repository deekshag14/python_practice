"""example:Attributes of file object"""
f=open("ecom_project.txt",'w')
print("file name:",f.name)
print("file mode:",f.mode)
print("is file readable:",f.readable())
print("is file writable:",f.writable())
print("is file closed:",f.closed)
f.close()
print("is file closed:",f.closed)
      
