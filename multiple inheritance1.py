class p1:
    def m1(self):
        print("parent1 method")
class p2:
    def m1(self):
        print("parent2 method")
class c(p1,p2):
    def m2(self):
        print("child method")
    def m1(self):
        print("child method m1")


c=c()
c.m1()
c.m2()

       
