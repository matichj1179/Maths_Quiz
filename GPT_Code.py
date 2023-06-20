import random


def generate_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return a, b


def ask_question(operation):
    a, b = generate_question()
    if operation == '+':
        print(f"What is {a} + {b}?")
        return a + b
    elif operation == '-':
        print(f"What is {a} - {b}?")
        return a - b
    elif operation == 'x':
        print(f"What is {a} x {b}?")
        return a * b
    elif operation == '/':
        print(f"What is {a} / {b}? (Round your answer to 2 decimal places)")
        return round(a / b, 2)


def main():
    operations = ['+', '-', 'x', '/']
    random.shuffle(operations)  # Randomize the order of operations
    score = 0
    total_questions = 4

    for operation in operations:
        expected_result = ask_question(operation)
        user_answer = float(input("Enter your answer: "))

        if user_answer == expected_result:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {expected_result}")

    print(f"\nYou scored {score} out of {total_questions}.")


if __name__ == "__main__":
    main()
