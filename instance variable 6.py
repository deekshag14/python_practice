class student:
    school_name="SGVG"

    def __init__(self):
        self.a=100

    def disp(self):
        a=100
        print("the value of a is:",self.a)
        print("the value of a is:",a)

s=student()
s.disp()
print(s.__dict__)
print(student.__dict__)


