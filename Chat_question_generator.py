import random

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
    a = 4
    b = 20
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



operations = ['+', '-', 'x', '/']
random.shuffle(operations)  # Randomize the order of operations
score = 0
total_questions = check_rounds()

for operation in operations:
    expected_result = ask_question(operation)
    user_answer = float(input("Enter your answer: "))

    if user_answer == expected_result:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {expected_result}")

print(f"\nYou scored {score} out of {total_questions}.")
