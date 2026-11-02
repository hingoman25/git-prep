import requests


url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

for user in users:
    print(user["name"], "-", user["email"])
    print("Completed Process.")


# This is for a test commit