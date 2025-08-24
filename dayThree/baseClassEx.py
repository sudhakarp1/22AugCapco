'''baseClassEx.py'''

class Base:
    def __init__(self):
        print(f'Base class __init__() called')

    def methodOne(self):
        print(f'Base class methodOne() called')

    def methodTwo(self):
        print(f'Base class methodTwo() called')

    def __str__(self):
        return f'Base class __str__() called'
    
if __name__ =='__main__':
    obj = Base()
    obj.methodOne()
    obj.methodTwo()
    print(obj)