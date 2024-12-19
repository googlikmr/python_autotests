import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "TOKEN" # put your token here
HEADER = {"Content-Type" : "application/json", "trainer_token" : TOKEN}
TRAINER_ID = "ID" # put your trainer id here

def test_status_code():
    respose_trainers = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : TRAINER_ID})
    assert respose_trainers.status_code == 200
    

def test_my_trainer_id():
    respose_trainers = requests.get(url = f"{URL}/trainers", params = {"trainer_id" : TRAINER_ID})
    assert respose_trainers.json()["data"][0]["id"] == TRAINER_ID
