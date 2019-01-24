
number1 = input('Enter First Number:')

number2 = input('Enter Second Number:')


def menu():
    print('1 - Add \n 2 - Subtract \n  3 - Multiply \n 4 - Divide')


def calculator(choice, number1, number2):
    num1 = int(number1)
    num2 = int(number2)
    if choice == '1':
        return (num1 + num2)
    elif choice == '2':
        return (num1 - num2)
    elif choice == '3':
        return (num1 * num2)
    elif choice == '4':
        return (num1 / num2)
    else:
        print('Wrong Choice!')


choice = input('Enter Your Choice')
print('Result is -', calculator(choice,number1,number2))

