import random
import string

# Create a string of all possible characters including space, punctuation, digits, and letters
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)  # Convert the string to a list of characters
key = chars.copy()  # Make a copy of the list to use as the key

# Shuffle the key list to create a random mapping of characters
random.shuffle(key)

# Uncomment the following lines to see the original and shuffled lists
# print(f"chars : {chars}")
# print(f"key   : {key}")

# ENCRYPTION
cipher_text = input("Enter a message to encrypt: ")  # Get the message to encrypt from the user
plain_text = ""  # Initialize an empty string for the decrypted message

# Loop through each character in the cipher text
for letter in cipher_text:
    index = key.index(letter)  # Find the index of the letter in the key list
    plain_text += chars[index]  # Append the corresponding character from the chars list to the plain text

# Print the encrypted and original messages
print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")
