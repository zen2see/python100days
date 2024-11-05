alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'\
            'q','r','s','t','u','v','w','x','y','z']
direction = input ("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# cipher_text = ""
# decrypted_text = ""

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")

# def decrypt(coded_text, shift_amount):
#     decrypted_text = ""
#     for letter in coded_text:
#         unshifted_position = alphabet.index(letter) - shift_amount 
#         unshifted_position %= len(alphabet)
#         print(unshifted_position)
#         decrypted_text += alphabet[unshifted_position]
#     print(f"The decrypted text is: {decrypted_text}")

# if direction == 'encode':
#     encrypt(original_text=text, shift_amount=shift)
# else:
#     decrypt(coded_text=text, shift_amount=shift)

def caesar(original_text, shift_amount, direction):
    output_text = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {direction}d result: {output_text}")

caesar(original_text=text, shift_amount=shift, direction=direction)