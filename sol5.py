# factorial

def factorial(number):
    if number in (0, 1):
        return 1
    else:
        return number * factorial(number - 1)


for i in range(5, 21):
    print("factorial of {0} is {1}".format(i, factorial(i)))
