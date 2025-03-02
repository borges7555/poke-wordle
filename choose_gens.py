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