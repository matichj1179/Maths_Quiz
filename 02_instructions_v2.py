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
    print("This will be a maths quiz on basic facts and true or false maths questions")
    print("Enter the amount of rounds you wish to play or press <enter> for infinite mode")


# Main routine
played_before = yes_no("have you played this game before? ")

if played_before == "no":
    instructions()

print("program continues")
