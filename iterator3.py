class numbers:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
       x=self.a
       self.a+=1
       return x

number_class=numbers()
number_iter=iter(number_class)
print("number iter:",type(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))

