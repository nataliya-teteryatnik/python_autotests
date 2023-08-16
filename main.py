import requests
import json

url = "https://api.pokemonbattle-stage.me:9101/pokemons"

payload = json.dumps({
  "name": "generate",
  "photo": "generate"
})
headers = {
  'trainer_token': '5235fa4933ab26f1105eb0f4ad36b918',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

id = response.json()['id']

print(id)

payload = json.dumps({
  "pokemon_id": id,
  "name": "Alex"
})

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

url = "https://api.pokemonbattle-stage.me:9101/trainers/add_pokeball"

payload = json.dumps({
  "pokemon_id": id
})

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
