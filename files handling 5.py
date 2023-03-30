"""Example:writing multiple lines to a file"""
f=open("besant_data.txt",'a')
list=["python\n","HTML\n","Javascript\n","data science"]
f.writelines(list)
print("list of lines written to the file sccessfully")
f.close()
