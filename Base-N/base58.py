alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def encrypt(input):
    output_text = ""
    bits = 0
    bits_count = 0

    for char in input:
        bits <<= 8
        bits += ord(char)
        bits_count += 8

        while bits_count >= 5:
            index = (bits >> (bits_count - 5)) & 31
            output_text += alphabet[index]
            bits_count -= 5
            bits &= (1 << bits_count) - 1

    if bits_count > 0:
        bits <<= 5 - bits_count
        index = bits & 31
        output_text += alphabet[index]

    return output_text

def decrypt(input):
    output_text = ""
    bits = 0
    bits_count = 0

    for char in input:
        if char not in alphabet:
            break

        index = alphabet.index(char)
        bits <<= 5
        bits += index
        bits_count += 5

        while bits_count >= 8:
            byte = (bits >> (bits_count - 8)) & 255
            output_text += chr(byte)
            bits_count -= 8
            bits &= (1 << bits_count) - 1

    return output_text