'''
    Introduction to Exception Handling
'''
num = 0 
while True:
    try:
        num = int(input('Enter a num: '))
        print(f'Num: {num}')
    except:
        print('Exception Occurred...')
    else:
        break

print(f'Program continues...with num: {num}')