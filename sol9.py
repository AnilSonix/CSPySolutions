source_filename = input("Enter source filename : ")
target_filename = input("Enter target filename : ")

source = open(source_filename, "r")
target = open(target_filename, "w")

for line in source.readlines():
    for char in line:
        target.write(char.upper())

source.close()
target.close()
