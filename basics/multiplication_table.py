def multiplication_table(number, start = 1 , stop = 10 ):
    for i in range(start,stop + 1):
        print(f"{number} * {i} = {number * i}")


multiplication_table(5)
