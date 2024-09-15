import random
from itertools import count


fixed_random_number = (random.randint(1,100))

attemps = []
leaderboard = ({})

while True:
    user_random_number = int(input("Guess a random number: "))
    if user_random_number == fixed_random_number:

        print(f"Congratulation, the random number was {fixed_random_number}")
        user_name = input("Enter your name: ")

        all_attemps = attemps.count(1) + 1


        print(f"{user_name}, It took you '{all_attemps}' attemps")
        leaderboard[user_name] = all_attemps
        leaderboard.update({user_name: all_attemps})
        print(leaderboard)

    elif user_random_number < fixed_random_number:
        print("Too low. Try again.")
        attemps.append(1)

    elif user_random_number > fixed_random_number:
        print("Too high. Try again.")
        attemps.append(1)