# user defined exceptions
class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg = arg
      
        
class TooOldException(Exception):
    def __init__(self,arg):
        self.msg = arg
        
if __name__ == "__main__":
    
    age = int(input("Enter your age: "))

    if age < 18:
        raise TooYoungException()
    elif age > 18:
        raise TooOldException("You are old")
    else:
        print("You will get email")


    
        
