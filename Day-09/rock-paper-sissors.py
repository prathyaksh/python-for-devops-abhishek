import random

system_input = random.choice(["Rock", "paper", "scissors"]).lower()

user_input = input("Enter your choice Rock, Paper, Scissors: ")
user_input = user_input.lower()

if user_input == system_input:
    print("You both win.")
elif user_input == "rock" and system_input == "paper":
    print("Paper beats rock. You lose, Systems Win.")
elif user_input == "paper" and system_input == "scissors":
    print("Scissors beats paper. You lose, Systems Win.")
elif user_input == "scissors" and system_input == "rock":
    print("Rock beats Scissors. You lose, Systems Win.")
else:
    print(f"{user_input} beats {system_input}. You Win")
print(f"system input = {system_input}")
