"""Example:To read  line by line"""
f=open("besant_data.txt",'r')
lines=f.readlines()
for line in lines:
    print(line,end='')
f.close()
