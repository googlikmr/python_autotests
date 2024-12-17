import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "65ca50f7f4fd63714b9d19c3e6a1b220"
HEADER = {"Content-Type" : "application/json", "trainer_token" : TOKEN}
TRAINER_ID = "13471"

def test_status_code():
    respose_trainers = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : TRAINER_ID})
    assert respose_trainers.status_code == 200
    

def test_my_trainer_id():
    respose_trainers = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : TRAINER_ID})
    assert respose_trainers.json()["data"][0]["id"] == TRAINER_ID