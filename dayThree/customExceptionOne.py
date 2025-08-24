'''
    exceptionFour.py
    multiple except blocks from one try
'''

class MyException(ValueError):
    pass

a, b, res= 0, 0, 0

try:
    a = int(input('Enter first Num: '))
    b = int(input('Enter Second Num: '))
    res = a / b
    if b > a:
        raise MyException('Just for Fun') 
except ValueError as ve:
    print(f'Value Error: {ve}')
except ZeroDivisionError as ze:
    print(f'ZeroDivisionError {ze}')
except Exception as e:
    print(f'Base class Exception: "{e}"')

print(f'{a}/{b} --> {res}')