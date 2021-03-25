stack = []


def push(stack, item):
    stack.append(item)


def pop(stack):
    return stack.pop()


def is_empty(stack):
    return len(stack) == 0


text = input("Enter a text : ")

for char in text:
    push(stack, char)

while not is_empty(stack):
    print(pop(stack), end="")
