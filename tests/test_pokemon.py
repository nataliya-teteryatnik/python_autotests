import requests
import pytest

def test_pokemons_get_all_trainers() :
    url = "https://api.pokemonbattle.me:9101/trainers"
    headers = {
        'trainer_token': '6d0ded5fb8177eadd2446862ff39a4c9',
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    assert response.status_code == 200

def test_pokemons_my_trainer_name() :
    url = "https://api.pokemonbattle.me:9101/trainers?trainer_id=3797"
    headers = {
        'trainer_token': '6d0ded5fb8177eadd2446862ff39a4c9',
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    assert response.json()['trainer_name'] == 'Nataliya'
