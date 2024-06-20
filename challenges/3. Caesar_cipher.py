"""
One of the first known examples of encryption was used by Julius Caesar.
Read more about here: https://en.wikipedia.org/wiki/Caesar_cipher
Create a program that implements a Caesar cipher.
Allow the user to supply the message and the shift amount, and then display the shifted message.
Ensure that your program encodes both uppercase and lowercase letters. Your program should also support negative shift
values so that it can be used both to encode messages and decode messages.

# When you have done the code, try to decrypt the following:
ldl ndj zcdl wdl id iwxcz ndj wpkt xbegdkts ndjg eniwdc hzxaah rdcvgpijapixdch
"""


def caesar_cipher(message, shift):
    encoded_message = []

    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26  # Shift value wrapped around the alphabet
            if char.islower():
                shifted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                shifted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encoded_message.append(shifted_char)
        else:
            encoded_message.append(char)  # Non-alphabetic characters are not shifted

    return ''.join(encoded_message)


# Main function to get input from the user and display the result
if __name__ == "__main__":
    message = input("Enter the message: ")
    shift = int(input("Enter the shift amount: "))
    result = caesar_cipher(message, shift)
    print("The shifted message is:", result)

# Decrypting the given encrypted message
encrypted_message = "ldl ndj zcdl wdl id iwxcz ndj wpkt xbegdkts ndjg eniwdc hzxaah rdcvgpijapixdch"
shift_for_decryption = -11  # Try different shifts to find the correct one
decrypted_message = caesar_cipher(encrypted_message, shift_for_decryption)
print("Decrypted message:", decrypted_message)


