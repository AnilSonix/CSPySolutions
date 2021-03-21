# stack

stack = []


def push(stack, item):
    stack.append(item)


def pop(stack):
    return stack.pop()


for i in range(4):
    push(stack, int(input("Enter a number to push ")))

while len(stack):
    print(pop(stack))
