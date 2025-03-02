import csv
import random
from pokemon_colorscripts import show_pokemon_by_name

def main() -> int:
    pokemon_db_file = "pokemon_db.csv"

    def create_map_from_csv(file_path: str) -> list:
        with open(file_path, mode='r') as file:
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

    pokemon_data_map = create_map_from_csv(pokemon_db_file)
    print("Choose the generations you want (1-8): ")
    gen_input = input()
    if not gen_input:
        gens = [1, 8]
    else:
        if '-' in gen_input:
            gens = list(map(int, gen_input.split('-')))
        else:
            gens = [int(gen_input), int(gen_input)]

    filtered_data = [row for row in pokemon_data_map if gens[0] <= int(row[3]) <= gens[1]]
    n_rand = random.randint(0, len(filtered_data)-1)
    random_pokemon = filtered_data[n_rand]
    #print(random_pokemon[0])
    tries = min(9, max(gens[1] - gens[0] + 2, 6))

    type1 = "[ Type 1:"
    type2 = "| Type 2:"
    gen = "| Gen:"
    hp = "| HP:"
    att = "| Att:"
    deff = "| Def:"
    spa = "| Spa:"
    spd = "| Spd:"
    spe = "| Spe:"
    bst = "| BST:"
    print("I have thought of a pokemon, try to guess it (you have " + str(tries) + " tries): ")

    while(tries > 0):
        tries -= 1
        aux = input()

        if ' -' in aux:
            guess = aux.split(' ')
        else:
            guess = [aux]

        results = ["", "", "", "", "", "", "", "", "", ""]
        guessed_pokemon = next((row for row in filtered_data if row[0].lower() == guess[0].lower()), None)
        
        if guess[0].lower() == random_pokemon[0].lower():
            for i in range(10):
                results[i] = " ✓ "
            print(type1 + results[0] + type2 + results[1] + gen + results[2] + hp + results[3] + att + results[4] + deff + results[5] + spa + results[6] + spd + results[7] + spe + results[8] + bst + results[9] + "]")
            print("Congratulations, you guessed it right! It was " + random_pokemon[0])
            show_pokemon_by_name(random_pokemon[0].lower())
            return 0
        else:  
            if guessed_pokemon == None:
                print("Pokemon not found, try again")
                tries += 1
            elif len(guess) == 2:
                if guess[1] == '-s':
                    print(guessed_pokemon)
                    tries += 1
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

                print(type1 + results[0] + type2 + results[1] + gen + results[2] + hp + results[3] + att + results[4] + deff + results[5] + spa + results[6] + spd + results[7] + spe + results[8] + bst + results[9] + "]")
                print("You have " + str(tries) + " tries left")

    print("You have run out of tries, the pokemon was " + random_pokemon[0])
    show_pokemon_by_name(random_pokemon[0])
    return 0

if __name__ == "__main__":
    main()