import requests

url = 'https://pokeapi.co/api/v2/pokemon/'

def create_url(pokemon_to_look):
    fetch_url = url + pokemon_to_look
    return fetch_url

def main():
    pokemon_to_look = input("What pokemon do you want info? ")
    fetch_url = create_url(pokemon_to_look.lower())

    poke_get = requests.get(fetch_url)

    if (poke_get.status_code != 200):
        print("Not a pokemon")
        return

    pokedex_json = poke_get.json()
    print(f"Showing information for: {pokedex_json['name']}")
    print(f"Id: {pokedex_json['id']}")
    print(f"Weight: {pokedex_json['weight']}")
    print("Abilities:")
    for ability in pokedex_json['abilities']:
        print("\t-",ability['ability']['name'])
    print("Types:")
    for type in pokedex_json['types']:
        print("\t-",type['type']['name'])

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("\nGoodbye")
            break
