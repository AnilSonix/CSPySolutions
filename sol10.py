filename = input("Enter filename : ")

file = open(filename, "r")

stats = {
    "lines": 0,
    "letters": 0,
    "digits": 0,
    "words": 0
}

for line in file.readlines():
    stats["lines"] += 1
    stats["words"] += len(line.split(" "))

    for char in line:
        if char.isalpha():
            stats["letters"] += 1
        elif char.isdigit():
            stats["digits"] += 1

print("lines {0}".format(stats["lines"]))
print("letters {0}".format(stats["letters"]))
print("digits {0}".format(stats["digits"]))
print("words {0}".format(stats["words"]))

file.close()
