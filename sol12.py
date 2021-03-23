filename = input("Enter filename : ")

file = open(filename, "r")

for line in file.readlines():
    if line[0] == "T":
        print(line)

file.close()
