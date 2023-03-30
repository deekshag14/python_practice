class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs...'.format(name,cls.legs))

Animal.walk('Dog')
Animal.walk('Cat')
