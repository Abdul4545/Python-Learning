import requests

# response = requests.get('https://w3schools.com/python/demopage.htm')
# print(response.status_code)
# print(response.headers)
# print(response.content)

# print(response.text)



url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title":"hello moid",
    "body": "sent by Abdul Moid",
    "userId": 1234
}

headers = {
    'Content-type': 'application/json; charset=UTF-8',
}

response = requests.post(url, headers=headers, json=data)

print(response.text)

