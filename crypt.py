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

def build_distribution(ciphertext):
    
    # initiliazed distribution
    distribution = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for char in ciphertext:

        distribution[alphabet[char]] += 1

    return distribution

def encrypt(message, key, shift):
    
    ciphertext = ''

    # loop over the message, convert each letter to its ascii code + 1 to offset space character
    # return the associated ciphertext
    for char in range(len(message)):

        if message[char] == ' ':
            letter = 0
        
        else:
            letter = ord(message[char]) - ord('a') + 1

        ciphertext += list(alphabet.keys())[list(alphabet.values()).index((letter + key[(char + 1) % shift]) % 27)]

    return ciphertext

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

def decrypt_helper(plaintext_guess, ciphertext):
    
    success = 0
    key_len = 1
    shift_length = 24
    
    # verify key length

    while key_len < shift_length:
        
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

################################ TASK 2 FUNCTIONS #######################################

def subkey(cipher, t):
    subkeys = ["" for i in range(t)]

    for i in range(len(cipher)):
        subkeys[i % t] += cipher[i]

    return subkeys

#Using Index of Coincidence approach
def coincidence(poss_key):
    num = build_distribution(poss_key)
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
        cipher += list(alphabet.keys())[(alphabet[c] + k) % 27]
    return cipher

def chi_square(cipher, e):
    return sum([((cipher[i] - e[i])**2)/e[i] for i in range(len(cipher))])

#This will attempt to invert the ciphertext based on the guessed key
def attempt_invert_cipher2(cipher, k):
    cipher_lst = list(cipher)
    for i in range(len(cipher)):
        cipher_lst[i] = list(alphabet.keys())[(alphabet[cipher[i]] + k[i % len(k)]) % 27]
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
            curr = chi_square(build_distribution(shift), eng_let_freq)
            if curr < shift_min:
                shift_min = curr
                min_i = j
        key.append(min_i)
    return key



def decrypt_task2(dictionary_2):
    ### TASK 2 ###
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
    print("cipher for task 2: ", encrypt(task2_plaintext, k2, t2))
    
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

def main():

    dictionary_1 = {

        0: 'error',
        1: 'underwaists wayfarings fluty analgia refuels transcribing nibbled okra buttonholer venalness hamlet praus apprisers presifted cubital walloper dissembler bunting wizardries squirrel preselect befitted licensee encumbrances proliferations tinkerer egrets recourse churl kolinskies ionospheric docents unnatural scuffler muches petulant acorns subconscious xyster tunelessly boners slag amazement intercapillary manse unsay embezzle stuccoer dissembles batwing valediction iceboxes ketchups phonily con',
        2: 'rhomb subrents brasiers render avg tote lesbian dibbers jeopardy struggling urogram furrowed hydrargyrum advertizing cheroots goons congratulation assaulters ictuses indurates wingovers relishes briskly livelihoods inflatable serialized lockboxes cowers holster conciliating parentage yowing restores conformities marted barrettes graphically overdevelop sublimely chokey chinches abstracts rights hockshops bourgeoisie coalition translucent fiascoes panzer mucus capacitated stereotyper omahas produ',
        3: 'yorkers peccaries agenda beshrews outboxing biding herons liturgies nonconciliatory elliptical confidants concealable teacups chairmanning proems ecclesiastically shafting nonpossessively doughboy inclusion linden zebroid parabolic misadventures fanciers grovelers requiters catmints hyped necklace rootstock rigorously indissolubility universally burrowers underproduced disillusionment wrestling yellowbellied sherpa unburnt jewelry grange dicker overheats daphnia arteriosclerotic landsat jongleur',
        4: 'cygnets chatterers pauline passive expounders cordwains caravel antidisestablishmentarianism syllabubs purled hangdogs clonic murmurers admirable subdialects lockjaws unpatentable jagging negotiated impersonates mammons chumminess semi pinner comprised managership conus turned netherlands temporariness languishers aerate sadists chemistry migraine froggiest sounding rapidly shelving maligning shriek faeries misogynist clarities oversight doylies remodeler tauruses prostrated frugging comestible ',
        5: 'ovulatory geriatric hijack nonintoxicants prophylactic nonprotective skyhook warehouser paganized brigading european sassier antipasti tallyho warmer portables selling scheming amirate flanker photosensitizer multistage utile paralyzes indexer backrests tarmac doles siphoned casavas mudslinging nonverbal weevil arbitral painted vespertine plexiglass tanker seaworthiness uninterested anathematizing conduces terbiums wheelbarrow kabalas stagnation briskets counterclockwise hearthsides spuriously s'
    }

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

    # select plaintext randomly
    shift = random.choice(range(1 ,24))
    plaintext_sample = random.choice(range(0, 4))
    message = dictionary_1[plaintext_sample]

    key = [random.choice(range(0 ,26)) for i in range(shift)]

    # print('plaintext is: ', message)
    
    # Generating cipher from plaintext
    # test_cipher = encrypt(message, key, shift)
    # print('cipher is: ')
    # print(test_cipher)

    cipher = input('Enter the ciphertext: ')
    print('Original plaintext is: ')
    checker = decrypt(cipher, dictionary_1)
    if checker == "error":
        decrypt_task2(dictionary_2)
    else:
        print(checker)

main()