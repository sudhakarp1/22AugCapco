'''
    exceptionFour.py
    multiple except blocks from one try
'''

a, b, res= 0, 0, 0

try:
    a = int(input('Enter first Num: '))
    b = int(input('Enter Second Num: '))
    res = a / b
    if b > a:
        raise TypeError('Just for Fun') 
except ValueError as ve:
    print(ve)
except ZeroDivisionError as ze:
    print(ze)
except Exception as e:
    print(f'Base class Exception: "{e}"')

print(f'{a}/{b} --> {res}')