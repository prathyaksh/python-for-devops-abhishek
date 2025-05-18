atm_pin = 1538

attempts = 3

for i in range(3):
    user_input = int(input(f"enter your ATM PIN. you have {attempts} attempts left : "))
    attempts -= 1
    if user_input == atm_pin:
        print(f"Your Input is correct. you got it in {attempts+1} attempts ")
        break
    elif user_input != atm_pin:
        print(f"Wrong pin entered. you have {attempts} attempts left.")
    else:
        print(f"you have given 3 wrong inputs.Try after some time.")
        break