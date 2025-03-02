import random
from create_map import create_map_from_csv
from prints import help, print_results
from options import options
from show_pic import show_picture

def game(gens: list[int]):
    pokemon_data_map = create_map_from_csv()
    filtered_data = [row for row in pokemon_data_map if gens[0] <= int(row[3]) <= gens[1]]
    n_rand = random.randint(0, len(filtered_data)-1)
    random_pokemon = filtered_data[n_rand]
    print(random_pokemon[0]) # Debugging purposes
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
                print("Congratulations, you guessed it right! It was " + random_pokemon[0] + "!\n")
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
        show_picture(random_pokemon[0])