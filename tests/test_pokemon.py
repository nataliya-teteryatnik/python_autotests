import requests
import pytest

def test_pokemons_get_all_trainers() :
    url = "https://api.pokemonbattle-stage.me:9101/trainers"
    headers = {
        'trainer_token': '5235fa4933ab26f1105eb0f4ad36b918',
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    assert response.status_code == 200

def test_pokemons_my_trainer_name() :
    url = "https://api.pokemonbattle-stage.me:9101/trainers?trainer_id=1381"
    headers = {
        'trainer_token': '5235fa4933ab26f1105eb0f4ad36b918',
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    assert response.json()['trainer_name'] == 'Nataliya'