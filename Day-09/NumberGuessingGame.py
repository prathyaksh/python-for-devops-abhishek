import random

secret_number  = random.randint(1,10)

attempts =3

while True:
    user_input = int(input("You have 3 guesses. Give your Number: "))
    attempts -= 1     

    if user_input > secret_number:
        print(f"your guess is higher.  {attempts} attempts left")
    elif user_input < secret_number:
        print(f"your guess is lower. {attempts} attempts left")
    else:
        print(f"you chose the right number in : {3- attempts} attempt")
        break

    if attempts == 0:
        print(f"you have used your number of attempts. play again. Random number is  - {secret_number}")
        break
