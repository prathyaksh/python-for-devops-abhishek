

try:
    user_input = int(input("Input a number : "))
    factorial = 1
    for i in range(1,user_input+1):
        factorial  *= i
        
except ValueError:
    print("Input only numbers.")
except Exception as e:
    print("Unknown exception occured. Try again.")
print(f"Factorial of {user_input} is : {factorial}")
