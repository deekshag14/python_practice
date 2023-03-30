class p:
    def m1(self):
        print("parent method")
class c1(p):
    def m2(self):
        print("child1 method")
class c2(p):
    def m3(self):
        print("child2 method")


c1=c1()
c1.m1()
c1.m2()
c2=c2()
c2.m1()
c2.m3()
           
