def help():
    print("\nThe goal of the game is to guess the pokemon I'm thinking of.")
    print("You can guess the pokemon by typing their name.")
    print("First, you have to choose the generations of the pokemon you want to guess.")
    print("You can do this by typing the generation number (5) or a range of generations (2-6).")
    print("If no input is given, it will choose a pokemon from generations 1-8.")
    print("When inside the game, if you want to see the stats of a pokemon, type its name followed by ' -s' or '--stats.")
    print("If you want to see the pokemon's picture, type its name followed by ' -p' or '--picture'.")
    print("If you want to see a list of pokemons that contain a certain string, type the string followed by ' -l' or '--list'.")
    print("You have a limited number of tries to guess the pokemon.")  


def print_stats(array: list[str], data: list):
    info = next((row for row in data if row[0].lower() == array[0].lower()), None)
    if info != None:
        print("\n" + info[0] + ":")
        print("Type 1: " + info[1])
        print("Type 2: " + info[2])
        print("Gen: " + str(info[3]))
        print("HP : " + str(info[4]))
        print("Att: " + str(info[5]))
        print("Def: " + str(info[6]))
        print("Spa: " + str(info[7]))
        print("Spd: " + str(info[8]))
        print("Spe: " + str(info[9]))
        print("BST: " + str(info[10]) + "\n")
    else:
        print("\nPokemon not found, try again: ")


def print_results(results: list[str]):
    type1 = "| Type 1:"
    type2 = "| Type 2:"
    gen = "| Gen:"
    hp = "| HP:"
    att = "| Att:"
    deff = "| Def:"
    spa = "| Spa:"
    spd = "| Spd:"
    spe = "| Spe:"
    bst = "| BST:"
    output = type1 + results[0] + type2 + results[1] + gen + results[2] + hp + results[3] + att + results[4] + deff + results[5] + spa + results[6] + spd + results[7] + spe + results[8] + bst + results[9] + "|"
    print(" " + "_" * 11 + " " + "_" * 11 + " " + "_" * 8 + " " + "_" * 7 + " " + "_" * 8 + " " + "_" * 8 + " " + "_" * 8 + " " + "_" * 8 + " " + "_" * 8 + " " + "_" * 8)
    print("|" + " " * 11 + "|" + " " * 11 + "|" + " " * 8 + "|" + " " * 7 + "|" + " " * 8 + "|" + " " * 8 + "|" + " " * 8 + "|" + " " * 8 + "|" + " " * 8 + "|" + " " * 8 + "|")
    print(output)
    print("|" + "_" * 11 + "|" + "_" * 11 + "|" + "_" * 8 + "|" + "_" * 7 + "|" + "_" * 8 + "|" + "_" * 8 + "|" + "_" * 8 + "|" + "_" * 8 + "|" + "_" * 8 + "|" + "_" * 8 + "|\n")
