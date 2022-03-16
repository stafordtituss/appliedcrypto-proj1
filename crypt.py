import random
import math

# a dictionary containing all characters used in encryption/decryption with its associated value
alphabet = {
    ' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 
    'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 
    'y': 25, 'z': 26
}

dictionary_1 = {

    0: 'error',
    1: 'underwaists wayfarings fluty analgia refuels transcribing nibbled okra buttonholer venalness hamlet praus apprisers presifted cubital walloper dissembler bunting wizardries squirrel preselect befitted licensee encumbrances proliferations tinkerer egrets recourse churl kolinskies ionospheric docents unnatural scuffler muches petulant acorns subconscious xyster tunelessly boners slag amazement intercapillary manse unsay embezzle stuccoer dissembles batwing valediction iceboxes ketchups phonily con',
    2: 'rhomb subrents brasiers render avg tote lesbian dibbers jeopardy struggling urogram furrowed hydrargyrum advertizing cheroots goons congratulation assaulters ictuses indurates wingovers relishes briskly livelihoods inflatable serialized lockboxes cowers holster conciliating parentage yowing restores conformities marted barrettes graphically overdevelop sublimely chokey chinches abstracts rights hockshops bourgeoisie coalition translucent fiascoes panzer mucus capacitated stereotyper omahas produ',
    3: 'yorkers peccaries agenda beshrews outboxing biding herons liturgies nonconciliatory elliptical confidants concealable teacups chairmanning proems ecclesiastically shafting nonpossessively doughboy inclusion linden zebroid parabolic misadventures fanciers grovelers requiters catmints hyped necklace rootstock rigorously indissolubility universally burrowers underproduced disillusionment wrestling yellowbellied sherpa unburnt jewelry grange dicker overheats daphnia arteriosclerotic landsat jongleur',
    4: 'cygnets chatterers pauline passive expounders cordwains caravel antidisestablishmentarianism syllabubs purled hangdogs clonic murmurers admirable subdialects lockjaws unpatentable jagging negotiated impersonates mammons chumminess semi pinner comprised managership conus turned netherlands temporariness languishers aerate sadists chemistry migraine froggiest sounding rapidly shelving maligning shriek faeries misogynist clarities oversight doylies remodeler tauruses prostrated frugging comestible ',
    5: 'ovulatory geriatric hijack nonintoxicants prophylactic nonprotective skyhook warehouser paganized brigading european sassier antipasti tallyho warmer portables selling scheming amirate flanker photosensitizer multistage utile paralyzes indexer backrests tarmac doles siphoned casavas mudslinging nonverbal weevil arbitral painted vespertine plexiglass tanker seaworthiness uninterested anathematizing conduces terbiums wheelbarrow kabalas stagnation briskets counterclockwise hearthsides spuriously s'
}

def build_distribution(ciphertext):
    
    # initiliazed distribution
    distribution = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for char in ciphertext:

        distribution[alphabet[char]] += 1

    return distribution

def generate_keys(dictionary_1):
    keys = []
    for key in range(len(dictionary_1) - 1):
        keys.append(random.sample(alphabet.keys(), len(alphabet)))
    print(keys)
    return keys

def find_char(c, i, keys):
    print(keys[i])
    if c == ' ':
        letter = 0
    else:
        letter = ord(c) - ord('a') + 1
    final = keys[i][letter]
    return final



def encrypt(message, key):

    ciphr_ptr = 1 
    msg_ptr = 0
    num_rand_characters = 0
    L = 500
    ciphertext = []
    final = []

    probabilities = [0, 0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75]

    for i in range(len(dictionary_1) - 1):

        prob_of_random_ciphertext = random.choice(probabilities)
        coin_value = random.random()
        while msg_ptr < len(message):
            # while len(ciphertext) <= len(message) + num_rand_characters:
            # coin_generation_algorithm(ciphertext_pointer,L)

            if prob_of_random_ciphertext < coin_value <= 1:
                print(msg_ptr)
                j = message[msg_ptr]
                print(j)
                char = find_char(j, i, key)
                ciphertext.append(char)
                print(ciphertext)
                msg_ptr += 1

            if 0 <= coin_value <= prob_of_random_ciphertext:

                random_char = random.choice(list(alphabet.keys()))
                ciphertext.append(random_char)
                num_rand_characters += 1

                # ciphr_ptr += 1
        final.append(''.join(ciphertext))
        prob_of_random_ciphertext = 1
    return final


# def encrypt(message, key, shift):
    
#     ciphertext = ''

#     # loop over the message, convert each letter to its ascii code + 1 to offset space character
#     # return the associated ciphertext
#     for char in range(len(message)):

#         if message[char] == ' ':
#             letter = 0
        
#         else:
#             letter = ord(message[char]) - ord('a') + 1

#         ciphertext += list(alphabet.keys())[list(alphabet.values()).index((letter + key[(char + 1) % shift]) % len(alphabet))]

#     return ciphertext

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
    key_length = 1
    shift_length = 24
    
    # verify key length

    while key_length < shift_length:
        
        correct = 0
        
        # loop over each character in key append to cipher string and possible_plaintext string
        for letter_index in range(0, key_length):
            
            cipher = ''
            possible_plaintext = ''

            cipher = ' '.join([ciphertext[i] for i in range(letter_index, len(ciphertext), key_length)])

            possible_plaintext = ' '.join([plaintext_guess[i] for i in range(letter_index, len(plaintext_guess), key_length)])

            # compare frequencies of characters in cipher and possible_plaintext in order to find the mapped letter in ciphertext
            # must sort distributions of letters so that they can be mapped by frequency
            if sorted(build_distribution(cipher)) == sorted(build_distribution(possible_plaintext)):
                correct += 1

        key_length += 1

        success = max(success, correct)

    return success

################################ TASK 2 FUNCTIONS #######################################

def generate_subkeys(cipher, shift_length):

    # function to generate subkeys
    # first loop for the shift length and build list of empty strings
    # then loop over the ciphertext and add combinations of substrings while maintaining the shift length

    subkeys = []
    i = 0

    while i < shift_length:

        subkeys.append('')
        i += 1

    for i in range(len(cipher)):

        subkeys[i % shift_length] += cipher[i]

    return subkeys

#Using Index of Coincidence approach
def incidence_of_coinkidinks(key_guess):

    # use the index of coincidence approach in order to determine the amount of identical letters appearing in the same index.

    # first, construct the distribution
    # loop through the frequencies and determine an upperbound and lowerbound
    # return the result by dividing them

    distribution = build_distribution(key_guess)
    
    upperbound = 0

    for freq in distribution:
        upperbound += freq * freq - 1

    key_length = len(key_guess)

    lowerbound = key_length * (key_length - 1)

    result = upperbound / lowerbound
    
    return result
    
def determine_key_length(ciphertext):

    # function to determine the key length

    key_length = 0
    minimum_length = 1
    max_length = 24
    coincidence = 2 / 30 # found through frequency analysis

    # loop through the possible key lengths and generate subkeys from ciphertext
    # determine the difference using the incidence of coincidence

    for i in range(2, max_length):
        
        subkeys = generate_subkeys(ciphertext, i)

        list_of_differences = []

        for key_guess in subkeys:

            list_of_differences.append(abs(coincidence - incidence_of_coinkidinks(key_guess)))

        difference = sum(list_of_differences) / len(subkeys)
        
        # if the difference is less than the minimum key length, then set the key length, and minimum key length and continue
        if difference < minimum_length:
            
            key_length = i
            minimum_length = difference
    
    return key_length

# def loop_through():

#These are for brute forcing the key once you know the key length
def bruteforce(message, key):

    # once the key length is known, we are able to brute force the key

    ciphertext = ""

    # for each character in the message build ciphertext by applying shift
    for char in message:
        ciphertext += list(alphabet.keys())[(alphabet[char] + key) % len(alphabet)]

    return ciphertext

def chi_square_distribution(cipher, e):

    return sum([pow((cipher[i] - e[i]), 2) / e[i] for i in range(len(cipher))])

#This will attempt to invert the ciphertext based on the guessed key
def invert_cipher(ciphertext, key):

    print('\nCIPHERTEXT: ',ciphertext, '\n')

    ciphers = list(ciphertext)

    print('\nCIPHERS: ',ciphers, '\n')

    ciphers = ''

    for i in range(len(ciphertext)):

        ciphers.append(list(alphabet.keys())[(alphabet[ciphertext[i]] + key[i % len(key)]) % len(alphabet)])

    return "".join(ciphers)

#This will attempt to guess the values of the key once the key length is known
def guess_key(cipher, shift, frequency):

    attempt = generate_subkeys(cipher, shift)
    key = []
    key_length = 26
    
    for i in range(len(attempt)):
        
        min_i = 0
        shift_min = 10000000
        
        for j in range(key_length):
            
            shift = bruteforce(attempt[i], j)
            curr = chi_square_distribution(build_distribution(shift), frequency)
            
            if curr < shift_min:
                shift_min = curr
                min_i = j

        key.append(min_i)

    return key



def decrypt_task2(dictionary_2):

    plaintext = ""

    max_length = 500
    condition_met = 501

    count = 0
    
    while count <= max_length:

        word = random.choice(dictionary_2)

        if count + len(word) + len(' ') <= max_length:

            plaintext += word + ' '
            count += len(word) + len(' ')

        elif count or count + len(word) or count + len(word) + len(' ') > max_length:
            count = condition_met


    print("Task 2 plaintext: ", plaintext, len(plaintext))

    #Generating ciphertext from plaintext
    shift = random.choice(range(1, 24))
    key = [random.choice(range(0 ,26)) for i in range(shift)]
    print("cipher for task 2: ", encrypt(plaintext, key, shift))
    
    ciphertext = input("Enter ciphertext for task 2: ")
    # print("key len: ", k2, len(k2))
    # print("key len guess: ", determine_key_len(c2))

    #Taken from: http://www.macfreek.nl/memory/Letter_Distribution
    frequency_of_letters = {   ' ': 0.1831686, 'a': 0.0655307, 'b': 0.0127070, 'c': 0.0226508, 'd': 0.0335227, 'e': 0.1021788,
                            'f': 0.0197180, 'g': 0.0163587, 'h': 0.0486220, 'i': 0.0573425, 'j': 0.0011440, 'k': 0.0056916,
                            'l': 0.0335616, 'm': 0.0201727, 'n': 0.0570308, 'o': 0.0620055, 'p': 0.0150311, 'q': 0.0008809,
                            'r' :0.0497199, 's': 0.0532626, 't': 0.0750999, 'u': 0.0229520, 'v': 0.0078804, 'w': 0.0168961,
                            'x': 0.0014980, 'y': 0.0146995, 'z': 0.0005979
                        }

    test = guess_key(ciphertext, determine_key_length(ciphertext), list(frequency_of_letters.values()))
    plaintext_guess = invert_cipher(ciphertext, test)
    print("The original plaintext is most likely: ")
    print(plaintext_guess)

def main():

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


    key = generate_keys(dictionary_1)
    dict_1 = list(dictionary_1.values())
    print(dict_1)
    plaintext_sample = random.choice(range(1,4))

    test = encrypt(dict_1[plaintext_sample], key)

    # print("Final CipherText: \n" + str(''.join(test)))
    print("Final: " + str(test))

    # select plaintext randomly
    # shift = random.choice(range(1 ,24))
    
    # message = dictionary_1[plaintext_sample]

    # key = [random.choice(range(0 ,26)) for i in range(shift)]

    # print('plaintext is: ', message)
    
    # Generating cipher from plaintext
    # test_cipher = encrypt(message, key, shift)
    # print('cipher is: ')
    # print(test_cipher)

    # cipher = input('Enter the ciphertext: ')
    # print('Original plaintext is: ')
    # checker = decrypt(cipher, dictionary_1)
    
    # if checker == "error":
    #     decrypt_task2(dictionary_2)
    # else:
    #     print(checker)

main()