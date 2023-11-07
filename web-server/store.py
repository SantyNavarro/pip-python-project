import requests


def getCategories():
    request = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(request.status_code)
    # print(request.text) This line will print a string
    categories = request.json()
    for category in categories:
        print(category["name"])
