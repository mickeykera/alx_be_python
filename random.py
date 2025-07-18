"""import random

play_again = True
while play_again:
    secret_number = random.randint(1, 10)
    guess = int(input("Guess the secret number between 1 and 10: "))
    match guess:
        case guess if guess < secret_number:
            print("Too low")
        case guess if guess > secret_number:
            print("Too high")
        case _:
            print("Correct")
    
    # Ask if user wants to play again
    play_again_input = input("\nWould you like to play again? (yes/no): ").lower()
    play_again = play_again_input == "yes"
"""
number = [1, 5, 3, 9]
total = 0
for num in number:
    total += num
print("The total is:", total)
