# bubble sort

numbers = []


def bubble_sort(numbers):
    n = len(numbers)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


for i in range(7):
    numbers.append(int(input("Enter number : ")))

bubble_sort(numbers)

print("after sorting")
for number in numbers:
    print(number)
