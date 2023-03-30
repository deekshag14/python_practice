class p:
    def m1(self):
        print("parent method")
class c(p):
    def m2(self):
        print("child method")

c=c()
c.m1()
c.m2()
