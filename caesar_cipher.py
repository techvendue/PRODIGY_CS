# PRODIGY INFOTECH - CYBER SECURITY
# TRACK CODE: CS
# TASK-01: CAESAR CIPHER IMPLEMENTATION

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts a given text using the Caesar Cipher algorithm.

    Args:
        text (str): The input string to be processed.
        shift (int): The number of positions to shift the letters.
        mode (str): 'encrypt' or 'decrypt' to determine the operation.

    Returns:
        str: The processed (encrypted or decrypted) string.
    """
    result = ""
    
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Determine the starting ASCII value based on case (uppercase or lowercase)
            start = ord('A') if char.isupper() else ord('a')
            
            # Calculate the shifted position
            # 1. Find the character's position in the alphabet (0-25)
            # 2. Add the shift value
            # 3. Use modulo 26 to wrap around the alphabet
            # 4. Add the starting ASCII value to get the new character's code
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            
            # Convert the new ASCII code back to a character
            result += chr(shifted_char_code)
        else:
            # If the character is not a letter, keep it unchanged
            result += char
            
    return result

def main():
    """
    Main function to get user input and run the Caesar Cipher.
    """
    print("--- Caesar Cipher Program ---")
    print("A simple tool for encrypting and decrypting text.\n")

    while True:
        # Get user's choice: encrypt or decrypt
        choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        if choice in ['e', 'd']:
            break
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

    # Get the message from the user
    message = input("Enter your message: ")

    # Get the shift value from the user
    while True:
        try:
            key = int(input("Enter the shift value (a whole number): "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for the shift value.")

    # Perform encryption or decryption based on user's choice
    if choice == 'e':
        encrypted_message = caesar_cipher(message, key, 'encrypt')
        print("\n--- Encryption Complete ---")
        print(f"Original Message:  {message}")
        print(f"Encrypted Message: {encrypted_message}")
    else: # choice == 'd'
        decrypted_message = caesar_cipher(message, key, 'decrypt')
        print("\n--- Decryption Complete ---")
        print(f"Encrypted Message: {message}")
        print(f"Decrypted Message: {decrypted_message}")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
