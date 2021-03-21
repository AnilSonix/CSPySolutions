# bubble sort

numbers = []


def insertion_sort(numbers):
    # Traverse through 1 to len(arr)
    for i in range(1, len(numbers)):

        key = numbers[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key


for i in range(7):
    numbers.append(int(input("Enter number : ")))

insertion_sort(numbers)

print("after sorting")
for number in numbers:
    print(number)
