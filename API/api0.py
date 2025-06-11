import requests

response = requests.get("http://randomfox.ca/floof")
print(response.status_code)
print(response.text)#string returned
print(response.json()) #dictionary returned
fox = response.json()
print(fox['image'])

base_url = "http://pokeapi.co/api/v2/"

def get_poke_info(name):
    url = f"{base_url}/pokemon/{name}"
    response0 = requests.get(url)
    print(response0)
    
pokemon_name = "pikachu"
get_poke_info(pokemon_name)
