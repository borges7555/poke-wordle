def choose_generations() -> list[int]:
    gen_input = input()
    if gen_input == 'help':
        help()
        print("Press 'Enter' to continue.")
        input()
        print("\nChoose the generations you want the pokemon to be from (1-9): ")
        return choose_generations()
    elif gen_input == 'exit':
        return [0, 0]
    elif not gen_input:
        return [1, 9]
    else:
        if '-' in gen_input:
            if  1 <= gen_input.split('-')[0] <= 9 and 1 <= gen_input.split('-')[1] <= 9:
                if gen_input.split('-')[0] <= gen_input.split('-')[1]:
                    return [int(gen_input.split('-')[0]), int(gen_input.split('-')[1])]
                else:
                    return [int(gen_input.split('-')[1]), int(gen_input.split('-')[0])]
            else:
                print("\nThe generaions available are only 1-9, try again: ")
                return choose_generations()
        else:
            if 9 <= int(gen_input) <= 9:
                return [int(gen_input), int(gen_input)]
            else:
                print("\nThe generaions available are only 1-9, try again: ")
                return choose_generations()