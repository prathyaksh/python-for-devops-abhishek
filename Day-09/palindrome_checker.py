input_word = input("Input a single word with no spaces: ").lower()
is_palindrome = True  # Flag to track palindrome status

for i in range(len(input_word) // 2):  # Loop through half the word
    if input_word[i] != input_word[-(i + 1)]:  # Compare first and last characters
        is_palindrome = False  # If mismatch found, it's not a palindrome
        break

if is_palindrome:
    print(f"{input_word} is a palindrome")
else:
    print(f"{input_word} is not a palindrome")
