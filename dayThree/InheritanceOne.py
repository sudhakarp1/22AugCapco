from baseClassEx import Base

class Derived(Base):
    def __init__(self):
        super().__init__()
        print(f'Derived class __init__() called') 

    def methodOne(self):
        print(f'Derived class methodOne() called')
        #return super().methodOne()

if __name__ == '__main__':
    obj = Derived()
    obj.methodOne()
    obj.methodTwo()
    print(obj)
