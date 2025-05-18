amount_available = 3000
attempts = 3
for i in range(attempts):
    try:
        amount_required = float(input("Enter your desired amount:"))
        if amount_available >= amount_required:
            updated_amount = amount_available - amount_required 
            amount_available = updated_amount
            break
        else:
            attempts -= 1
            print(f"Amount requested is higher than available balance. you have {attempts} remaining")  
    except ValueError:
            print("Input only numbers. Alphabet and special charecters are not allowed except . ")
    except Exception as e:
            print(f"unknown Exception occured : {e}")
    if attempts ==0:
         print("You have exhausted number of tries")
print(f"Transaction is complete. Current available balance is : {updated_amount}")