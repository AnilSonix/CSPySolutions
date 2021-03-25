import requests

url = input("Enter url : ")
response = requests.get(url)

print(response.text)
file = open(url, "w")
file.write(response.text)
file.close()

response.close()
