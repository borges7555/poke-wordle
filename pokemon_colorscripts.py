import json
import os

PROGRAM = os.path.realpath(__file__)
PROGRAM_DIR = os.path.dirname(PROGRAM)
COLORSCRIPTS_DIR = f"{PROGRAM_DIR}/colorscripts"
REGULAR_SUBDIR = "regular"
SMALL_SUBDIR = "small"

def print_file(filepath: str) -> None:
    with open(filepath, "r") as f:
        print(f.read())

def show_pokemon_by_name(name: str, form: str = "") -> None:
    print("")
    base_path = COLORSCRIPTS_DIR
    color_subdir =  REGULAR_SUBDIR
    size_subdir =  SMALL_SUBDIR
    with open(f"{PROGRAM_DIR}/pokemon.json") as file:
        pokemon_json = json.load(file)
        pokemon_names = {pokemon["name"] for pokemon in pokemon_json}
        if name not in pokemon_names:
            print(f"Couldn't show picture of {name}")
            return

        if form:
            for pokemon in pokemon_json:
                if pokemon["name"] == name:
                    forms = pokemon["forms"]
                    alternate_forms = [f for f in forms if f != "regular"]
            if form in alternate_forms:
                name += f"-{form}"
            else:
                print(f"Invalid form '{form}' for pokemon {name}")
                if not alternate_forms:
                    print(f"No alternate forms available for {name}")
                else:
                    print(f"Available alternate forms are")
                    for form in alternate_forms:
                        print(f"- {form}")
                return
    pokemon_file = f"{base_path}/{size_subdir}/{color_subdir}/{name}"
    print_file(pokemon_file)
