import random

#list of letters in the message space
alphabet = [' '] + [chr(i + ord('a')) for i in range(26)]
#mapping of each letter to its number
alphabet_map = {}
for i in range(len(alphabet)):
    alphabet_map[alphabet[i]] = i

def create_ciphertext(m, k, t):
    test_cipher = ""

    for i in range(len(m)):
        alpha = ord(m[i]) - ord('a') + 1
        if m[i] == ' ':
            alpha = 0
        test_cipher += alphabet[(alpha + k[(1 + i) % t]) % 27 ]

    # print(k, len(k))
    # print(test_cipher)
    return test_cipher

def get_distribution(cipher):
    dist = [0 for i in range(len(alphabet))]
    for c in cipher:
        dist[alphabet_map[c]] += 1
    return dist

#New f(x)s for task 2
def subkey(cipher, t):
    subkeys = ["" for poss_t in range(t)]
    for i in range(len(cipher)):
        subkeys[i % t] += cipher[i]
    return subkeys

#Using Index of Coincidence approach
def coincidence(poss_key):
    num = get_distribution(poss_key)
    upper = sum([x * (x - 1) for x in num])
    lower = len(poss_key) * (len(poss_key) - 1)
    return upper / lower
    
def find_key_length(cipher):
    key_len = 0
    min_key_len = 1
    for i in range(2, 24):
        subkeys = subkey(cipher, i)
        diff = sum([abs(0.0667 - coincidence(poss_key)) for poss_key in subkeys]) / len(subkeys)
        if diff < min_key_len:
            key_len = i
            min_key_len = diff
    
    return key_len

#These are for brute forcing the key once you know the key length
def monoalpha(m, k):
    cipher = ""
    for c in m:
        cipher += alphabet[(alphabet_map[c] + k) % 27]
    return cipher

def chi_square(cipher, e):
    return sum([((cipher[i] - e[i])**2)/e[i] for i in range(len(cipher))])

#This will attempt to invert the ciphertext based on the guessed key
def attempt_invert_cipher2(cipher, k):
    cipher_lst = list(cipher)
    for i in range(len(cipher)):
        cipher_lst[i] = alphabet[(alphabet_map[cipher[i]] + k[i % len(k)]) % 27]
    return "".join(cipher_lst)

#This will attempt to guess the values of the key once the key length is known
def break_down(cipher, t, eng_let_freq):
    attempt = subkey(cipher, t)
    key = []
    for i in range(len(attempt)):
        min_i = 0
        shift_min = 10000000
        for j in range(26):
            shift = monoalpha(attempt[i], j)
            curr = chi_square(get_distribution(shift), eng_let_freq)
            if curr < shift_min:
                shift_min = curr
                min_i = j
        key.append(min_i)
    return key

def main():
    ### TASK 2 ###
    #Generating plaintext
    with open("dictionary_2.txt") as test2:
        # dictionary_2 = [line.strip() for line in test2.readlines()]
        dictionary_2 = {
        0: 'lacrosses',
        1: 'protectional',
        2: 'blistered',
        3: 'leaseback',
        4: 'assurers',
        5: 'frizzlers',
        6: 'submerse',
        7: 'rankness',
        8: 'moonset',
        9: 'farcer',
        10: 'brickyard',
        11: 'stolonic',
        12: 'trimmings',
        13: 'glottic',
        14: 'rotates',
        15: 'twirlier',
        16: 'stuffer',
        17: 'publishable',
        18: 'invalided',
        19: 'harshens',
        20: 'tortoni',
        21: 'unlikely',
        22: 'alefs',
        23: 'gladding',
        24: 'favouring',
        25: 'particulate',
        26: 'baldpates',
        27: 'changeover',
        28: 'lingua',
        29: 'proctological',
        30: 'freaking',
        31: 'outflanked',
        32: 'amulets',
        33: 'imagist',
        34: 'hyped',
        35: 'pilfers',
        36: 'overachiever',
        37: 'clarence',
        38: 'outdates',
        39: 'smeltery'
    }
        task2_plaintext = ""
        while len(task2_plaintext) <= 500:
            new_word = random.choice(dictionary_2)
            if len(new_word) + len(task2_plaintext) >= 500:
                if len(task2_plaintext) < 500:
                    task2_plaintext += ' '
                break
            else:
                task2_plaintext += new_word + ' '
    print("Task 2 plaintext: ", task2_plaintext, len(task2_plaintext))

    #Generating ciphertext from plaintext
    t2 = random.randint(1, 24)
    k2 = [random.randint(0,26) for i in range(t2)]
    print("cipher for task 2: ", create_ciphertext(task2_plaintext, k2, t2))
    
    c2 = input("Enter ciphertext for task 2: ")
    # print("key len: ", k2, len(k2))
    # print("key len guess: ", find_key_length(c2))

    #Taken from: http://www.macfreek.nl/memory/Letter_Distribution
    eng_let_freq_dict = {   ' ': 0.1831686, 'a': 0.0655307, 'b': 0.0127070, 'c': 0.0226508, 'd': 0.0335227, 'e': 0.1021788,
                            'f': 0.0197180, 'g': 0.0163587, 'h': 0.0486220, 'i': 0.0573425, 'j': 0.0011440, 'k': 0.0056916,
                            'l': 0.0335616, 'm': 0.0201727, 'n': 0.0570308, 'o': 0.0620055, 'p': 0.0150311, 'q': 0.0008809,
                            'r' :0.0497199, 's': 0.0532626, 't': 0.0750999, 'u': 0.0229520, 'v': 0.0078804, 'w': 0.0168961,
                            'x': 0.0014980, 'y': 0.0146995, 'z': 0.0005979
                        }
    
    eng_let_freq = [0.1831686, 0.0655307, 0.0127070, 0.0226508, 0.0335227, 0.1021788, 0.0197180, 0.0163587, 0.0486220, 
                    0.0573425, 0.0011440, 0.0056916, 0.0335616, 0.0201727, 0.0570308, 0.0620055, 0.0150311, 0.0008809,
                    0.0497199, 0.0532626, 0.0750999, 0.0229520, 0.0078804, 0.0168961, 0.0014980, 0.0146995, 0.0005979
                ]

    test = break_down(c2, find_key_length(c2), list(eng_let_freq_dict.values()))
    p2 = attempt_invert_cipher2(c2, test)
    print("The original plaintext is most likely: ")
    print(p2)

main()