class p:
    def m1(self):
        print("parent method")
class c(p):
    def m2(self):
        print("child method")
class cc(c):
    def m3(self):
        print("sub child method")
    def m1(self):
        print("grandchild m1")

c=cc()
c.m1()
c.m2()
c.m3()
           
