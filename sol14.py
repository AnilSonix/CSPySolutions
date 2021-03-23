import csv

file = open(input("Enter filename"), "r")
lines = 0
reader = csv.DictReader(file)

for row in reader:
    if lines == 0:
        print(f'Column names are {", ".join(row)}')
        lines += 1
    print(f'\t{row["name"]} lives in the {row["city"]} , and is  {row["age"]}. years old')
    lines += 1

print(f'Processed {lines} lines.')

file.close()
