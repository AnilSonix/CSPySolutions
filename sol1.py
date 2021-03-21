# biggest of six numbers
numbers = []


def biggest(numbers):
    biggestOne = numbers[0]
    for number in numbers:
        if number > biggestOne:
            biggestOne = number

    return biggestOne


for i in range(6):
    numbers.append(int(input("Enter a number : ")))

print("Biggest one is {0}".format(biggest(numbers)))
