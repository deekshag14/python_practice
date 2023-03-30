class Employee:
    def __init__(self):
        self.eno=100
        self.ename='Tony'
        self.esal=10000
e=Employee()
print(e.__dict__)
print("name of empl:",e.ename)
