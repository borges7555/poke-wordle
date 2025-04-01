from pokemon_colorscripts import show_pokemon_by_name

def show_picture(name: str) -> bool:
    if "alolan" in name:
        return show_pokemon_by_name(name.split(" ")[1], "alola")
    elif "galarian" in name:
        return show_pokemon_by_name(name.split(" ")[1], "galar")
    elif "hisuian" in name:
        return show_pokemon_by_name(name.split(" ")[1], "hisui")
    elif "paldean" in name:
        return show_pokemon_by_name(name.split(" ")[1], "paldea")
    elif "mega" in name:
        if len(name.split(" ")) == 2:
            return show_pokemon_by_name(name.split(" ")[1], "mega")
        elif 'x' in name:
            return show_pokemon_by_name(name.split(" ")[1], "mega-x")
        elif 'y' in name:
            return show_pokemon_by_name(name.split(" ")[1], "mega-y")
    elif "primal" in name:
        return show_pokemon_by_name(name.split(" ")[1], "primal")
    elif len(name.split(" ")) == 2:
        if not show_pokemon_by_name(name.split(" ")[0], name.split(" ")[1]):
            if not show_pokemon_by_name(name.split(" ")[0], "regular"):
                if not show_pokemon_by_name(name.split(" ")[0] + "-" + name.split(" ")[1]):
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True
    else:
        return show_pokemon_by_name(name)