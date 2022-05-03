import requests

people = requests.get('http://api.twitter.com')
json = people.json()

print(json)
