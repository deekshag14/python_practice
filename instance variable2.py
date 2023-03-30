#class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def talk(self):
        print("hello my name is:",self.name)
        print("my rollno is:",self.rollno)
        print("my marks are:",self.marks)

student_one=student("mary",101,90)
student_one.talk()
student_two=student("john",102,95)
student_two.talk()


class Employee:
    def __init__(self):
        self.eno=100
        self.ename='Tony'
        self.esal=10000
e=Employee()
print(e.__dict__)
