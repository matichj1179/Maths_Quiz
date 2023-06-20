# ask user if they want to view instructions else program continues
def instructions():
    print("This will be a maths quiz on basic facts and true or false maths questions")
    print("Enter the amount of rounds you wish to play or press <enter> for infinite mode")


def question():
    user_input = input("Do you want to see the instructions? (yes/no): ")

    if user_input.lower() == "yes":
        instructions()

    elif user_input.lower() == "no":
        print("program continues")

    elif user_input.lower() == "y":
        instructions()

    elif user_input.lower() == "n":
        print("program continues")

    else:
        print("please enter yes or no")

    # Continue with the rest of the program


# Run the main function
question()
