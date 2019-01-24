def is_prime(number):
    for divisor in (2, int(number / 2)):
        if number % divisor == 0:
            return False
    return True


# print(is_prime(8))


def sum_upto_n(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum


# print(sum_upto_n(3))

def sum_of_divisors(number):
    sum = 0
    for i in range(1, number + 1):
        if number % i == 0 :
            sum += i
    return sum

# print(sum_of_divisors(6))

def print_number_triangle(number):
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()

print_number_triangle(5)