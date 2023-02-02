import random

print("+++++++++++++++++++++++ Rock, Paper, Scissors +++++++++++++++++++++++")
print()

while True:
    print("Enter the number of your choice \n1. Rock \n2. Paper \n3. Scissors \n")

    choice = int(input("Your turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print("Your choice is: " + choice_name)
    print()
    print("Computer is generating its choice...")

    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer's choice is: " + comp_choice_name)

    print()
    print(choice_name + " V/S " + comp_choice_name)

    result = (choice - comp_choice + 3) % 3

    if result == 0:
        print("Draw")
    elif result == 1:
        print("You win!")
    else:
        print("You lose!")

    print()
    print("Do you want to play again? (Y/N)")
    ans = input()
    if ans == 'N' or ans == 'n':
        break

print("Thanks for playing")
