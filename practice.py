import requests

api_key = '68b49dbf-fa0b-42c7-b225-954324523b8b'
word = 'potato'
url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)
definitions = res.json()

for definition in definitions:
    print(definition)