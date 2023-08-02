import random


# check if the number inputted was and integer else print and error and detecting exit code
def int_check(question, low=None, high=None, exit_code=None):
    if low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    elif low is not None:
        error = f"Please enter an integer more than {low}"
        situation = "low only"
    else:
        situation = "any integer"
        error = "Please enter an integer"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check that integer is valid (ie: not too low / too hig etc.)
            if situation == "any integer":
                return response

            elif situation == "both":
                if low <= response <= high:
                    return response

            elif situation == "low only":
                if response >= low:
                    return response

            print(error)

        except ValueError:
            print(error)


# detects users choice between yes or no
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


# ask user if they want to view instructions else program continues
def instructions():
    print("")
    print("This will be a maths quiz on basic facts")
    print("Enter the amount of rounds you wish to play")


# Ask user to enter the amount of rounds they want to play between 1 and a 100
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


# gets random numbers and sets up the question using number between 1 and 10
def ask_question(var_operation):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if var_operation == '+':
        print("")
        print(f"What is {a} + {b}?")
        return a + b
    elif var_operation == '-':
        print("")
        print(f"What is {a} - {b}?")
        return a - b
    elif var_operation == 'x':
        print("")
        print(f"What is {a} x {b}?")
        return a * b


# Main routine
score = 0
played_before = yes_no("have you played this game before? ")

if played_before == "no":
    instructions()

rounds_played = 0

rounds = int_check("How many rounds: ", 1, exit_code="")

low_number = 1
high_number = 10

# Ask user for # of rounds, <enter> for infinite mode

end_game = "no"
while end_game == "no":
    # Rounds Heading
    print()
    if rounds == "":
        heading = f'Continuous Mode: round {rounds_played + 1}'
    else:
        heading = f'Round {rounds_played + 1} of {rounds}'

    rounds_played += 1

    operations_list = ['+', '-', 'x']
    random.shuffle(operations_list)
    operation = operations_list[0]

    # rest of loop / game
    expected_result = ask_question(operation)
    user_answer = int_check("Enter your answer: ", exit_code="xxx")
    if user_answer == "xxx":
        rounds_played -= 1

    if user_answer == "xxx":
        break

    if user_answer == expected_result:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {expected_result}")

    if rounds_played == rounds:
        break

    print(f'You chose {user_answer}')
    print("")

print("***Game Over***")
print(f"\nYou scored {score} out of {rounds_played}.")
