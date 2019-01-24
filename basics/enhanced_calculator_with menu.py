number1 = input('Enter First Number:')
number2 = input('Enter Second Number:')

def menu():
    print('1 - Add \n2 - Subtract \n3 - Multiply \n4 - Divide \n5 - Exit')


def calculator(choice, number1, number2):
    num1 = int(number1)
    num2 = int(number2)
    if choice == 1:
        print (num1 + num2)
    elif choice == 2:
        print (num1 - num2)
    elif choice == 3:
        print (num1 * num2)
    elif choice == 4:
        print (num1 / num2)
    elif choice == 5:
        print('Exiting...')
    else:
        print('Wrong Choice!')

menu()
choice = int(input('Enter Your Choice:'))
calculator(choice,number1, number2)
while choice != 5 :
    number1 = input('Enter First Number:')
    number2 = input('Enter Second Number:')
    menu()
    choice = int(input('Enter Your Choice:'))
    calculator(choice, number1, number2)

