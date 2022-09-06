try :
    num = int(input('Enter an even number: '))
    assert num%2 ==0, 'You have enter an invalid input or odd number'
except AssertionError as obj:
    print(obj)

print('After the assertion')