# ten prime numbers
def is_prime(number):
    for divisor in range(number, number // 2):
        if number % divisor == 0:
            return False

    return True


count = 0
number = 2
while count != 10:
    if is_prime(number):
        print(number)
        count = count + 1
    number = number + 1
