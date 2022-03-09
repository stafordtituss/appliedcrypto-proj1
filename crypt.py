import random

# a dictionary containing all characters used in encryption/decryption with its associated value
alphabet = {
    ' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 
    'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 
    'y': 25, 'z': 26
}

def encrypt(message, key, random_substitution):
    
    ciphertext = ''

    # loop over the message, convert each letter to its ascii code + 1 to offset space character
    # return the associated ciphertext
    for char in range(len(message)):

        if message[char] == ' ':
            letter = 0
        
        else:
            letter = ord(message[char]) - ord('a') + 1

        ciphertext += list(alphabet.keys())[list(alphabet.values()).index((letter + key[(char + 1) % random_substitution]) % 27)]

    return ciphertext

def build_distribution(ciphertext):
    
    # initiliazed distribution
    distribution = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for char in ciphertext:

        distribution[alphabet[char]] += 1

    return distribution

def decrypt_helper(plaintext_guess, ciphertext):
    
    success = 0
    key_len = 1
    random_substitution_length = 24
    
    # verify key length

    while key_len < random_substitution_length:
        
        correct = 0
        
        # loop over each character in key append to cipher string and possible_plaintext string
        for letter_index in range(0, key_len):
            
            cipher = ''
            possible_plaintext = ''

            cipher = ' '.join([ciphertext[i] for i in range(letter_index, len(ciphertext), key_len)])

            possible_plaintext = ' '.join([plaintext_guess[i] for i in range(letter_index, len(plaintext_guess), key_len)])

            # compare frequencies of characters in cipher and possible_plaintext in order to find the mapped letter in ciphertext
            # must sort distributions of letters so that they can be mapped by frequency
            if sorted(build_distribution(cipher)) == sorted(build_distribution(possible_plaintext)):
                correct += 1

        key_len += 1

        success = max(success, correct)

    return success

def decrypt(ciphertext, plaintext_dict):

    success = 0
    correct_index = 0

    # loop through dictionary keys and values, call helper function to determine the most correct guess in decrypting ciphertext
    for key, value in plaintext_dict.items():
        
        current = decrypt_helper(value, ciphertext)
        
        if current > success:
            
            correct_index = key
            success = current
    
    return plaintext_dict[correct_index]

def main():

    file_contents = {}
    
    # open dictionary 1 reading just the plaintext, storing in a dictionary called file_contents
    with open('dictionary_1.txt', 'r') as f:
        contents = f.readlines()[4::4]

        for key, value in enumerate(contents, 0):
            file_contents[key] = value.strip()

    # select plaintext randomly
    random_substitution = random.choice(range(1 ,24))
    plaintext_sample = random.choice(range(0, 4))
    message = file_contents[plaintext_sample]

    key = [random.choice(range(0 ,26)) for i in range(random_substitution)]

    # print('plaintext is: ', message)
    
    # Generating cipher from plaintext
    test_cipher = encrypt(message, key, random_substitution)
    # print('cipher is: ')
    # print(test_cipher)

    cipher = input('Enter the ciphertext: ')
    print('Original plaintext is: ')
    print(decrypt(cipher, file_contents))

    f.close()

main()