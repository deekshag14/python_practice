class student:
    '''''Developed by besant tech for python demo'''
    def __init__(self):
        self.name='Mary'
        self.age=20
        self.marks=80
        print("self address:",id(self))

    def talk(self):
       print("hello i am:",self.name)
       print("my age is:",self.age)
       print("my marks are:",self.marks)
       print("self ad inside talk:",id(self))

student_one=student()
student_one.talk()
print("student_one address:",id(student_one))
