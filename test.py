from requests import get

print(get('http://127.0.0.1:5000/api/items').json())

print(get('http://127.0.0.1:5000/api/items/2').json())

print(get('http://127.0.0.1:5000/api/users').json())

print(get('http://127.0.0.1:5000/api/items/safa').json())