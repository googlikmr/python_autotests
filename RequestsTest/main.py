import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "TOKEN" # put your token here
HEADER = {"Content-Type" : "application/json", "trainer_token" : TOKEN}

# Создание покемона
body_creation = {
    "name": "generate",
    "photo_id": -1
}

response_creation = requests.post(url = f"{URL}/pokemons", headers = HEADER, json = body_creation)
print(response_creation.text)

pokemon_id = response_creation.json()["id"] # Помещаем в pokemon_id id новосозданного покемона

# Смена имени и картинки покемона
body_change_name = {
    "pokemon_id": f"{pokemon_id}",
    "name": "generate",
    "photo_id": -1
}

response_change_name = requests.put(url = f"{URL}/pokemons", headers = HEADER, json = body_change_name)
print(response_change_name.text)

# Ловля покемона в покебол
body_catch = {
    "pokemon_id": f"{pokemon_id}"
}

response_catch = requests.post(url = f"{URL}/trainers/add_pokeball", headers = HEADER, json = body_catch)
print(response_catch.text)
