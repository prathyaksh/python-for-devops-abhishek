import sys

user_input = int(sys.argv[1])

for j in range(1,11):
    number = user_input*j
    print(f"{user_input} * {j} = {number}")
    j += 1
