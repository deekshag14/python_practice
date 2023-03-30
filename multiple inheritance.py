class p1:
    def m1(self):
        print("parent1 method")
class p2:
    def m2(self):
        print("parent2 method")
class c(p2,p1):
    def m3(self):
        print("parent2 m1")


c=c()
c.m1()
c.m2()
c.m3()
       
