given_number = int(input("give the number: "))

is_prime = True
for i in range(2,given_number):
    if given_number % i == 0:
        is_prime = False
        break
if is_prime:
    print("NUmber is prime")
else :
    print("Number is not prime")
