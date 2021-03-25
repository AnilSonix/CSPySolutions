stack = []


def push(stack, item):
    stack.append(item)


def pop(stack):
    return stack.pop()


def peek(stack):
    return stack[0]


def is_empty(stack):
    return len(stack) == 0


def is_left_bracket(bracket):
    return bracket in "[({"


def is_right_bracket(bracket):
    return bracket in "})]"


def counterpart_bracket(bracket):
    if bracket == "[":
        return "]"
    elif bracket == "(":
        return ")"
    elif bracket == "{":
        return "}"
    elif bracket == "]":
        return "["
    elif bracket == ")":
        return "("
    elif bracket == "]":
        return "["


def bracket_check(expression):
    for char in expression:
        if is_left_bracket(char):
            push(stack, char)
        elif is_right_bracket(char):
            if not is_empty(stack):
                left_bracket = pop(stack)
                if counterpart_bracket(left_bracket) != char:
                    print("Expecting {0} , found {1}".format(counterpart_bracket(left_bracket), char))
                    return False
            else:
                print("Missing some brackets")
                return False

    return is_empty(stack)


if bracket_check(input("Enter a expression : ")):
    print("Good")
else:
    print("Some brackets are missing")
