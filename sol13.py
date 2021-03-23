import csv

person = {"name": input("Enter name: "), "city": input("Enter city: "), "age": input("Enter age: ")}

file = open(person["name"] + ".csv", "w")
writer = csv.DictWriter(file, fieldnames=person.keys())
writer.writeheader()
writer.writerow(person)

file.close()
