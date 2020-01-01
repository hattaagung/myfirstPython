for number in range (2,10):
    for x in range (2,number):
        if number % 2 == 0:
            print (f"{number} equals {x} * {number//x}")
            break
    else:
        print (f"{number} is a prime number")