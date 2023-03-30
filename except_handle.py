from test import TooYoungException,TooOldException

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise TooYoungException("You are young for this")
    elif age > 18:
        raise TooOldException("You are very old")
    else:
        print("You will get email")
        
except TooYoungException as e:
    print("Please wait for some time")
except TooOldException as e:
    print("You are old for this")
except:
    print("Something went wrong")
finally:
    print("Thanks for visiting our website")
