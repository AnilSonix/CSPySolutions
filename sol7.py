# mean

numbers = []


def arithmetic_mean(dataset):
    total = 0
    for number in dataset:
        total = total + number

    return total / len(dataset)


for i in range(10):
    numbers.append(int(input("Enter a number : ")))

print("arithmetic mean is {0}".format(arithmetic_mean(numbers)))
