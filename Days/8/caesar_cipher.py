# This script encrypts, or decrypts messages using Caesar Cipher method

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# --- Encryption/decryption function ------------------------------------------------

def caesar_cipher(user_text, user_shift, cipher_type):
    # Initialize
    cipher_text = ''

    for char in user_text:
        if char in alphabet:
            char_position = alphabet.index(char)
            if cipher_type == 'encode':
                char_position_new = char_position + user_shift
            else:
                char_position_new = char_position - user_shift
            char_position_new %= len(alphabet)
            
            new_char = alphabet[char_position_new]
        else:
            new_char = char
        
        cipher_text += new_char
    
    print(f"The {cipher_type}d text is: {cipher_text}")


continue_program = True

while continue_program:

    # --- User Inputs --------------------------------------------------------------------

    # Encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # If encode or decode are not chosen, Return invalid message and exit the code
    if direction not in ['encode', 'decode']:
        print("Invalid option. Please run again and type either encode or decode.")
        exit()

    # Message to encrypt or decrypt
    text = input("Type your message:\n").lower()

    # Values to shift by
    shift = int(input("Type the shift number:\n"))

    # --- Call function  -----------------------------------------------------------------

    caesar_cipher(user_text = text, user_shift = shift, cipher_type = direction)

    # --- Continue or end the program? ---------------------------------------------------
    yes_or_no = input("Type 'yes' to continue program, 'no' to end program. ").lower()
    if yes_or_no != 'yes':
        continue_program = False


