import random


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
    print("This will be a maths quiz on basic facts and true or false maths questions")
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


def ask_question(operation):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if operation == '+':
        print("")
        print(f"What is {a} + {b}?")
        return a + b
    elif operation == '-':
        print("")
        print(f"What is {a} - {b}?")
        return a - b
    elif operation == 'x':
        print("")
        print(f"What is {a} x {b}?")
        return a * b
    elif operation == '/':
        print("")
        print(f"What is {a} / {b}? (Round your answer to 2 decimal places)")
        return round(a / b, 2)


def main():
    operations_list = ['+', '-', 'x', '/']
    random.shuffle(operations_list)
    operation = operations_list[0]
    score = 0
    total_questions = check_rounds()

    expected_result = ask_question(operation)
    user_answer = float(input("Enter your answer: "))

    if user_answer == expected_result:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {expected_result}")

    print(f"\nYou scored {score} out of {total_questions}.")


# Main routine
played_before = yes_no("have you played this game before? ")

if played_before == "no":
    instructions()

rounds_played = 0
choose_instruction = ask_question('+')
print(choose_instruction)

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
