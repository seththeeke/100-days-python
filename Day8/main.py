"""
Day 8 - Functions with Parameters

Positional vs Keyword Arguments
 - If you want to specify the keyword for an argument, you can ignore positional location, e.g. greet(a, b) can be called as greet(b = "hello", a = "world")

"""

# Prime Number Checker
# def is_prime(number):
#     div = number - 1
#     while number % div != 0 and div > 1:
#         div -= 1
#
#     return div == 1
#
#
# num = int(input("Enter a number between 1 and 100: "))
# print(f"{num} is prime? {is_prime(num)}")


# Day 8 - Caesar Cipher - Take either an encoding or decoding property. Either encode by an index or decode a word by
# that same index.

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


# def encode(msg, shift):
#     encoded_msg = ""
#     for index in range(len(msg)):
#         if msg[index] != ' ':
#             encode_index = (alphabet.index(msg[index]) + shift) % len(alphabet)
#             encoded_msg += alphabet[encode_index]
#         else:
#             encoded_msg += ' '
#     return encoded_msg
#
#
# def decode(msg, shift):
#     decoded_msg = ""
#     for index in range(len(msg)):
#         if msg[index] != ' ':
#             decode_index = (alphabet.index(msg[index]) - shift) % len(alphabet)
#             decoded_msg += alphabet[decode_index]
#         else:
#             decoded_msg += ' '
#     return decoded_msg


def caesar(msg, shift, cmd):
    if cmd == "decode":
        shift *= -1
    new_msg = ""
    for index in range(len(msg)):
        if msg[index] != ' ':
            new_letter_index = (alphabet.index(msg[index]) + shift) % len(alphabet)
            new_msg += alphabet[new_letter_index]
        else:
            new_msg += ' '
    return new_msg


cmd = input("Enter either encode or decode: ")
msg = input("Enter your message: ").lower()
shift = int(input("Enter your shift value: "))
print(caesar(msg, shift, cmd))
