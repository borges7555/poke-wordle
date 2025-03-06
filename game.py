import random
import sys
from create_map import create_map_from_csv
from prints import help, print_results, print_stats
from options import options, dex
from show_pic import show_picture

def game(gens: list[int]):
    pokemon_data_map = create_map_from_csv()
    filtered_data = [row for row in pokemon_data_map if gens[0] <= int(row[3]) <= gens[1]]
    n_rand = random.randint(0, len(filtered_data)-1)
    random_pokemon = filtered_data[n_rand]
    #print(random_pokemon[0]) # Debugging purposes
    tries = min(9, max(gens[1] - gens[0] + 2, 6))

    results = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    print("\nI have thought of a pokemon, try to guess it (you have " + str(tries) + " tries): ")
    used_dex = False
    guessed_right = ["", "", 0]
    guessed_wrong_types = []
    guessed_wrong_gens = []
    
    while(tries > 0):   
        if tries <= 2 and not used_dex:
            print("Would you like to be shown a list of all the pokemons that are from the generation and have the type(s) that you have guessed right? (y/n)")
            if input() == 'y':
                dex(filtered_data, guessed_right, guessed_wrong_types, guessed_wrong_gens)
                used_dex = True
                print("You have " + str(tries) + " tries left")
            else:
                print("\nYou have " + str(tries) + " tries left")

        aux = input()
        tries -= 1
        
        if aux == 'help':
            help()
            tries += 1
            print("Press 'Enter' to continue.")
            input()
        elif aux == 'exit':
            sys.exit(1)
        elif ' -' in aux:
            options(aux.split(' -'), filtered_data)
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
                print("Congratulations, you guessed it right! It was " + random_pokemon[0] + "!")
                show_picture(random_pokemon[0].lower())
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

                for i in range(2, 9):
                    if guessed_pokemon[i+1] < random_pokemon[i+1]:
                        results[i] = " ↑ "
                    elif guessed_pokemon[i+1] > random_pokemon[i+1]:
                        results[i] = " ↓ "
                    else:
                        results[i] = " ✓ "
                    i += 1

                print_results(results)

            if results[0] == " ✓ " or results[1] == " ⇄ ":
                guessed_right[0] = random_pokemon[1]
            if results[1] == " ✓ " or results[0] == " ⇄ ":
                guessed_right[1] = random_pokemon[2]
            if results[2] == " ✓ ":
                guessed_right[2] = random_pokemon[3]

            if guessed_pokemon[1] not in guessed_wrong_types:
                if results[0] == ' x ':
                    guessed_wrong_types.append(guessed_pokemon[1])
            if random_pokemon[2] not in guessed_wrong_types:
                if results[1] == ' x ':
                    guessed_wrong_types.append(guessed_pokemon[2])

            if guessed_pokemon[3] not in guessed_wrong_gens:
                if results[2] == ' ↑ ':
                    for i in range(1, int(guessed_pokemon[3]) + 1):
                        guessed_wrong_gens.append(i)
                if results[2] == ' ↓ ':
                    for i in range(int(guessed_pokemon[3]), 10):
                        guessed_wrong_gens.append(i)

        print("You have " + str(tries) + " tries left")

        if tries == 0:
            print("\nYou have run out of tries, the pokemon was " + random_pokemon[0] + ".\n")
            print_stats(random_pokemon[0], filtered_data)
            show_picture(random_pokemon[0].lower())