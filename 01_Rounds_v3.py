def check_rounds():
    while True:
        response = input("How many rounds: ")
        round_error = "Please type either <enter> or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)
                if response < 1:
                    print(round_error)
                    continue
            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here...

rounds_played = 0
choose_instruction = "Question Filler"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":
    # Rounds Heading
    print()
    if rounds == "":
        heading = f'Continuous Mode: round {rounds_played + 1}'
    else:
        heading = f'Round {rounds_played + 1} of {rounds}'

    print(heading)
    choose = input(f'{choose_instruction} = ')

    # end game if exit code is typed
    if choose == "xxx":
        break

    rounds_played += 1

    if rounds_played >= rounds:
        break

    # rest of loop / game
    print(f'You chose {choose}')

print("Thank you for playing")
