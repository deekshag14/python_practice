class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        print("Id of b_one inside magic method is:",id(self))
        print("Id of b_two inside magic method is:",id(other))
        return self.pages+other.pages

b_one=Book(100)
b_two=Book(200)

b_three=b_one+b_two

print("Id of b_one is:",id(b_one))
print("Id of b_two is:",id(b_two))

print(b_three)
