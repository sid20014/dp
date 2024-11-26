import math

def rotate_right(value, bits):
    return ((value >> bits) | (value << (32 - bits))) & 0xFFFFFFFF

def generate_constants():
    # Generate the first 64 prime numbers for K
    K = []
    for i in range(2, 312):  # Considering primes for 64 constants
        if len(K) == 64:
            break
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            K.append(int((math.sin(len(K) + 1) % 1) * 2**32) & 0xFFFFFFFF)
    
    # Generate the square roots of the first 8 primes for H
    H = []
    for i in range(2, 20):
        if len(H) == 8:
            break
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            H.append(int((math.sqrt(i) % 1) * 2**32) & 0xFFFFFFFF)
    
    return H, K

def sha256(message):
    H, K = generate_constants()

    binary_message = ''.join(f'{ord(char):08b}' for char in message)
    original_length = len(binary_message)
    binary_message += '1'
    while (len(binary_message) + 64) % 512 != 0:
        binary_message += '0'
    binary_message += f'{original_length:064b}'

    for i in range(0, len(binary_message), 512):
        chunk = binary_message[i:i + 512]
        words = [int(chunk[j:j + 32], 2) for j in range(0, 512, 32)]

        for j in range(16, 64):
            s0 = rotate_right(words[j - 15], 7) ^ rotate_right(words[j - 15], 18) ^ (words[j - 15] >> 3)
            s1 = rotate_right(words[j - 2], 17) ^ rotate_right(words[j - 2], 19) ^ (words[j - 2] >> 10)
            words.append((words[j - 16] + s0 + words[j - 7] + s1) & 0xFFFFFFFF)

        a, b, c, d, e, f, g, h = H

        for j in range(64):
            S1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25)
            ch = (e & f) ^ ((~e) & g)
            temp1 = (h + S1 + ch + K[j] + words[j]) & 0xFFFFFFFF
            S0 = rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        H = [
            (H[0] + a) & 0xFFFFFFFF, (H[1] + b) & 0xFFFFFFFF, (H[2] + c) & 0xFFFFFFFF,
            (H[3] + d) & 0xFFFFFFFF, (H[4] + e) & 0xFFFFFFFF, (H[5] + f) & 0xFFFFFFFF,
            (H[6] + g) & 0xFFFFFFFF, (H[7] + h) & 0xFFFFFFFF
        ]

    return ''.join(f'{value:08x}' for value in H)

password = input("Enter a password: ")
hashed_password = sha256(password)
print(f"SHA-256 Hash: {hashed_password}")
