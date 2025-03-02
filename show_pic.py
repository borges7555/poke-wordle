from pokemon_colorscripts import show_pokemon_by_name

def show_picture(name: str):
    if "alolan" in name:
        show_pokemon_by_name(name.split(" ")[1], "alola")
    elif "galarian" in name:
        show_pokemon_by_name(name.split(" ")[1], "galar")
    elif "mega" in name:
        if len(name.split(" ")) == 2:
            show_pokemon_by_name(name.split(" ")[1], "mega")
        elif 'x' in name:
            show_pokemon_by_name(name.split(" ")[1], "mega-x")
        elif 'y' in name:
            show_pokemon_by_name(name.split(" ")[1], "mega-y")
    elif "primal" in name:
        show_pokemon_by_name(name.split(" ")[1], "primal")
    elif len(name.split(" ")) == 2:
        show_pokemon_by_name(name.split(" ")[0], name.split(" ")[1])
    else:
        show_pokemon_by_name(name)