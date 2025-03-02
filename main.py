import csv
import random
from pokemon_colorscripts import show_pokemon_by_name

def help():
    print("\nThe goal of the game is to guess the pokemon I'm thinking of.")
    print("You can guess the pokemon by typing their name.")
    print("First, you have to choose the generations of the pokemon you want to guess.")
    print("You can do this by typing the generation number (5) or a range of generations (2-6).")
    print("If no input is given, it will choose a pokemon from generations 1-8.")
    print("When inside the game, if you want to see the stats of a pokemon, type its name followed by ' -s'.")
    print("If you want to see the pokemon's picture, type its name followed by ' -p'.")
    print("You have a limited number of tries to guess the pokemon.")


def create_map_from_csv() -> list:
        with open("pokemon_db.csv", mode='r') as file:
            csv_reader = csv.reader(file)
            data_map = []
            for row in csv_reader:
                row[3] = int(row[3])  # Generation
                row[4] = int(row[4])  # HP
                row[5] = int(row[5])  # Att
                row[6] = int(row[6])  # Def
                row[7] = int(row[7])  # Spa
                row[8] = int(row[8])  # Spd
                row[9] = int(row[9])  # Spe
                row[10] = int(row[10])  # BST
                data_map.append(row)
        return data_map


def choose_generations() -> list[int]:
    gen_input = input()
    if gen_input == 'help':
        help()
        print("Press 'Enter' to continue.")
        input()
        print("\nChoose the generations you want the pokemon to be from (1-8): ")
        return choose_generations()
    elif gen_input == 'exit':
        return [0, 0]
    elif not gen_input:
        return [1, 8]
    else:
        if '-' in gen_input:
            if  1 <= gen_input.split('-')[0] <= 8 and 1 <= gen_input.split('-')[1] <= 8:
                if gen_input.split('-')[0] <= gen_input.split('-')[1]:
                    return [int(gen_input.split('-')[0]), int(gen_input.split('-')[1])]
                else:
                    return [int(gen_input.split('-')[1]), int(gen_input.split('-')[0])]
            else:
                print("\nThe generaions available are only 1-8, try again: ")
                return choose_generations()
        else:
            if 1 <= int(gen_input) <= 8:
                return [int(gen_input), int(gen_input)]
            else:
                print("\nThe generaions available are only 1-8, try again: ")
                return choose_generations()  


def options(array: list[str], data: list):
    if array[1] == '-s':
        print("\n" + next((row for row in data if row[0].lower() == array[0].lower()), None))
    if array[1] == '-p':
        show_pokemon_by_name(array[0].lower())


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
    '''print(" " + "_" * (len(output) - 2))
    print("|" + " " * (len(output) - 2) + "|")
    print(output)
    print("|" + "_" * (len(output) - 2) + "|\n")'''
    print(" " + "_" * 11 + " " + "_" * 11 + " " + "_" * 8 + " " + "_" * 7 + " " + "_" * 8 + " " + "_" * 8 + " " + "_" * 8 + " " + "_" * 8 + " " + "_" * 8 + " " + "_" * 8)
    print("|" + " " * 11 + "|" + " " * 11 + "|" + " " * 8 + "|" + " " * 7 + "|" + " " * 8 + "|" + " " * 8 + "|" + " " * 8 + "|" + " " * 8 + "|" + " " * 8 + "|" + " " * 8 + "|")
    print(output)
    print("|" + "_" * 11 + "|" + "_" * 11 + "|" + "_" * 8 + "|" + "_" * 7 + "|" + "_" * 8 + "|" + "_" * 8 + "|" + "_" * 8 + "|" + "_" * 8 + "|" + "_" * 8 + "|" + "_" * 8 + "|\n")


def game(gens: list[int]):
    pokemon_data_map = create_map_from_csv()
    filtered_data = [row for row in pokemon_data_map if gens[0] <= int(row[3]) <= gens[1]]
    n_rand = random.randint(0, len(filtered_data)-1)
    random_pokemon = filtered_data[n_rand]
    print(random_pokemon[0]) # mostra o pokemon escolhido
    tries = min(9, max(gens[1] - gens[0] + 2, 6))

    results = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    print("\nI have thought of a pokemon, try to guess it (you have " + str(tries) + " tries): ")

    while(tries > 0):   
        tries -= 1
        aux = input()

        if aux == 'help':
            help()
            tries += 1
            print("Press 'Enter' to continue.")
            input()
        elif aux == 'exit':
            tries += 1
            break
        elif ' -' in aux:
            options(aux.split(' '), filtered_data)
            tries += 1
        else:
            guess = aux
            guessed_pokemon = next((row for row in filtered_data if row[0].lower() == guess.lower()), None)
            
            if guessed_pokemon == None:
                print("\nPokemon not found, try again: ")
                tries += 1
            elif guessed_pokemon[0].lower() == random_pokemon[0].lower():
                for i in range(10):
                    results[i] = " ✓ "

                print_results(results)
                print("Congratulations, you guessed it right! It was " + random_pokemon[0] + "!\n")
                show_pokemon_by_name(random_pokemon[0].lower())
                break
            else:      
                for i in range(2):
                    if guessed_pokemon[i+1] == random_pokemon[i+1]:
                        results[i] = " ✓ "
                    else:
                        results[i] = " x "

                if guessed_pokemon[1] == random_pokemon[2]:
                    results[0] = " ⇄ "
                if guessed_pokemon[2] == random_pokemon[1]:
                    results[1] = " ⇄ "

                for i in range(2, 10):
                    if guessed_pokemon[i+1] < random_pokemon[i+1]:
                        results[i] = " ↑ "
                    elif guessed_pokemon[i+1] > random_pokemon[i+1]:
                        results[i] = " ↓ "
                    else:
                        results[i] = " ✓ "
                    i += 1

                print_results(results)
        print("You have " + str(tries) + " tries left")

    if tries == 0:
        print("\nYou have run out of tries, the pokemon was " + random_pokemon[0] + ".\n")
        show_pokemon_by_name(random_pokemon[0])


def main() -> int:
    print("Welcome to the Pokemon Wordle!")
    print("Type 'help' for instructions, 'exit' to leave or press 'Enter' to start the game.")
    aux = input()

    if aux == 'help':
        help()
        print("If you want to see this again, type 'help'.")
        print("Press 'Enter' to start the game.")
        input()
    elif aux == 'exit':
        return 0

    print("Choose the generations you want the pokemon to be from (1-8): ")
    gens = choose_generations()
    if gens == [0, 0]:
        return 0
    else:
        game(gens)
        
    return 0


if __name__ == "__main__":
    main()