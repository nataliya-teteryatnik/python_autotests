import requests
import json

url = "https://api.pokemonbattle.me:9101/pokemons"

payload = json.dumps({
  "name": "generate",
  "photo": "generate"
})
headers = {
  'trainer_token': '6d0ded5fb8177eadd2446862ff39a4c9',
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

url = "https://api.pokemonbattle.me:9101/trainers/add_pokeball"

payload = json.dumps({
  "pokemon_id": id
})

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
