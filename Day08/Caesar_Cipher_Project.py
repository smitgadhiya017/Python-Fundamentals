
import Caesar_Cipher_Art
print(Caesar_Cipher_Art.logo)

alphabet = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]

# def encrypt(original_text, shift_amount):
#     ciper_text = ""
#
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         ciper_text += alphabet[shifted_position % len(alphabet)]
#
#     print(f"Here's the encoded result : {ciper_text}")
#
# def decrypt(original_text, shift_amount):
#     ciper_text = ""
#
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         ciper_text += alphabet[shifted_position % len(alphabet)]
#
#     print(f"Here's the encoded result : {ciper_text}")

# encrypt and decrypt both functionality in one function
def caesar(original_text, shift_amount, encode_or_decode):
    ciper_text = ""
    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            ciper_text += letter
        else:

            shifted_position = alphabet.index(letter) + shift_amount
            ciper_text += alphabet[shifted_position % len(alphabet)]

    print(f"Here's the {encode_or_decode}d result : {ciper_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt : \n")
    text = input("Type your message :\n").lower()
    shift = int(input("Type the shift number :\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "yes":
        should_continue = True
    elif restart == "no":
        should_continue = False
        print("Goodbye")
    else:
        should_continue = False
        print("Invalid Input")