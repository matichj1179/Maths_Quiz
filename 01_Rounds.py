# Ask user to enter the amount of rounds they want to play between 1 and a 100

def rounds():
    while True:
        user_input = input("Enter the amount of rounds you would like to play (between 1 and 100): ")

        try:
            num = int(user_input)
            if 0 < num <= 100:
                print("Program continues")
                break
            else:
                print("Please enter an integer that is more than 0 or less than 100")

        except ValueError:
            print("Please enter a valid integer")


print(rounds())
