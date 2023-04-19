first_number = int(input('Please enter your first number: '))
operation = input('Please enter operation: + or - or * or /: ')
second_number = int(input('Please enter your second number: '))

if operation == '+':
    print(first_number + second_number)
else:
    print('invalid number or operation')