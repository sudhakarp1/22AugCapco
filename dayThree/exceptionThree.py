'''
    Introduction to Exception Handling
'''
num = 0 
while False:
    try:
        num = int(input('Enter a num: '))
        print(f'Num: {num}')
    except ValueError as ve:
        print(f'Exception Occurred...{ve}')
    else:
        break
else:
    print('Else inside while loop')

print(f'Program continues...with num: {num}')