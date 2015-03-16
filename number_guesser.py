import random


def main():
    number_guess()


def number_guess():
    """a function to generate a random number and has the user guess"""
    test = 0
    user_num = int(input("Guess a whole number(Non negative) from 1 to 100: \
                            "))
    randnum = random.randint(1, 100)
    while test == 0:
        if randnum == user_num:
            print("You're correct!")
            play_again = input("play again?")
            if play_again.upper() == "NO":
                print("Have a great day!")
                test = 1
            else:
                user_num = int(input("Guess a whole number(Non negative) from \
                                         1 to 100: "))
        elif randnum < user_num:
            print('lower')
            user_num = int(input("Guess Again: "))

        else:
            print('higher')
            user_num = int(input("Guess Again: "))

if __name__ == "__main__":
    main()
