import random
import math
from collections import Counter

# a dictionary containing all characters used in encryption/decryption with its associated value
alphabet = {
    ' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 
    'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 
    'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 
    'y': 25, 'z': 26
}

key_vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

dictionary_1 = {

    # 0: 'error',
    0: 'underwaists wayfarings fluty analgia refuels transcribing nibbled okra buttonholer venalness hamlet praus apprisers presifted cubital walloper dissembler bunting wizardries squirrel preselect befitted licensee encumbrances proliferations tinkerer egrets recourse churl kolinskies ionospheric docents unnatural scuffler muches petulant acorns subconscious xyster tunelessly boners slag amazement intercapillary manse unsay embezzle stuccoer dissembles batwing valediction iceboxes ketchups phonily con',
    1: 'rhomb subrents brasiers render avg tote lesbian dibbers jeopardy struggling urogram furrowed hydrargyrum advertizing cheroots goons congratulation assaulters ictuses indurates wingovers relishes briskly livelihoods inflatable serialized lockboxes cowers holster conciliating parentage yowing restores conformities marted barrettes graphically overdevelop sublimely chokey chinches abstracts rights hockshops bourgeoisie coalition translucent fiascoes panzer mucus capacitated stereotyper omahas produ',
    2: 'yorkers peccaries agenda beshrews outboxing biding herons liturgies nonconciliatory elliptical confidants concealable teacups chairmanning proems ecclesiastically shafting nonpossessively doughboy inclusion linden zebroid parabolic misadventures fanciers grovelers requiters catmints hyped necklace rootstock rigorously indissolubility universally burrowers underproduced disillusionment wrestling yellowbellied sherpa unburnt jewelry grange dicker overheats daphnia arteriosclerotic landsat jongleur',
    3: 'cygnets chatterers pauline passive expounders cordwains caravel antidisestablishmentarianism syllabubs purled hangdogs clonic murmurers admirable subdialects lockjaws unpatentable jagging negotiated impersonates mammons chumminess semi pinner comprised managership conus turned netherlands temporariness languishers aerate sadists chemistry migraine froggiest sounding rapidly shelving maligning shriek faeries misogynist clarities oversight doylies remodeler tauruses prostrated frugging comestible ',
    4: 'ovulatory geriatric hijack nonintoxicants prophylactic nonprotective skyhook warehouser paganized brigading european sassier antipasti tallyho warmer portables selling scheming amirate flanker photosensitizer multistage utile paralyzes indexer backrests tarmac doles siphoned casavas mudslinging nonverbal weevil arbitral painted vespertine plexiglass tanker seaworthiness uninterested anathematizing conduces terbiums wheelbarrow kabalas stagnation briskets counterclockwise hearthsides spuriously s'
}

expected_letter_frequency = {
                ' ': 0.127,
                'e':0.127,
                't':0.091,
                'a':0.082,
                'o':0.075,
                'i':0.07,
                'n':0.067,
                's':0.063,
                'h':0.061,
                'r':0.06,
                'd':0.043,
                'l':0.04,
                'u':0.028,
                'c':0.028,
                'm':0.024,
                'w':0.024,
                'f':0.022,
                'y':0.02,
                'g':0.02,
                'p':0.019,
                'b':0.015,
                'v':0.01,
                'k':0.008,
                'x':0.002,
                'j':0.002,
                'q':0.001,
                'z':0.001,

}

def build_distribution(ciphertext):
    
    # initiliazed distribution
    distribution = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    # python sorts space character before 'a' so keep that in mind
    for char in ciphertext:

        distribution[alphabet[char]] += 1

    return distribution

def generate_key(plaintext):
    
    key = []

    for char in plaintext:
        key = random.sample(key_vals, len(key_vals))

    return key

def find_char(c, key):

    if c == ' ':
        letter = 0
    else:
        letter = ord(c) - ord('a') + 1

    final = key[letter]

    if final == 0:
        char = ' '
    else:
        char = list(alphabet.keys())[final]
    
    last = char
    
    return last

def encrypt(message, key):

    ciphr_ptr = 0 
    msg_ptr = 0
    num_rand_characters = 0
    L = 500
    ciphertext = []

    probabilities = [0, 0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75]

    prob_of_random_ciphertext = random.choice(probabilities)

    # print('KEY: ', key)


    while ciphr_ptr < L + num_rand_characters:
        # coin_generation_algorithm(ciphertext_pointer,L)
        coin_value = random.uniform(0,1)

        if prob_of_random_ciphertext < coin_value and coin_value <= 1:
            j = message[msg_ptr]
            char = find_char(j, key)
            # print(char)

            ciphertext.append(char)
            msg_ptr += 1

        if 0 <= coin_value and coin_value <= prob_of_random_ciphertext:
            random_char = random.choice(list(alphabet.keys()))
            ciphertext.append(random_char)
            num_rand_characters += 1

        ciphr_ptr += 1

    # print('plaintext: ', message, 'Length: ', len(message))

    # print('\nciphertext: ', ciphertext, 'Length: ', len(ciphertext))

    return ''.join(ciphertext)

def find_key(input_dict, value):

    return next((k for k, v in input_dict.items() if v == value), None)


def decrypt(ciphertext, plaintext_dictionary):

    dictionary_distribution_mapping = {}

    cipher_count = len(ciphertext)
    # print("Input Ciphertext Length: " + str(cipher_count))
    plaintext_count = len(plaintext_dictionary[1])

    for index, plaintext in enumerate(plaintext_dictionary):

        dictionary_distribution_mapping[plaintext_dictionary[index]] = sorted(build_distribution(plaintext))

    ciphertext_distribution = sorted(build_distribution(ciphertext))

    possible_plaintexts = plaintext_dictionary

    if cipher_count == plaintext_count:

        for i in range(len(dictionary_distribution_mapping)):

            if ciphertext_distribution == list(dictionary_distribution_mapping.values())[i]:

                return plaintext_dictionary[i]

    else:
        # determine max letter frequency for each character in the plaintexts, to figure out how many characters i can delete
        max_freq = [max(i) for i in zip(*dictionary_distribution_mapping.values())]

        # print('max freq: ',max_freq)

        for i in range(len(alphabet)):
            
            if ciphertext_distribution[i] > max_freq[i]:
                cipher_count -= (ciphertext_distribution[i] - max_freq[i])
                ciphertext_distribution[i] = max_freq[i]  

        # print(list(dictionary_distribution_mapping.values())[0], '\n',
        #     list(dictionary_distribution_mapping.values())[1], '\n',
        #     list(dictionary_distribution_mapping.values())[2], '\n',
        #     list(dictionary_distribution_mapping.values())[3], '\n',
        #     list(dictionary_distribution_mapping.values())[4], '\n')

        # print('Updated ciphertext count: ', cipher_count, '\n')
        # print('\nciphertext_distribution: ', ciphertext_distribution)

        for plaintext_distribution in dictionary_distribution_mapping.values():

            for i in range(len(alphabet) - 1, -1, -1):

                if ciphertext_distribution[i] < plaintext_distribution[i]:
                    # print(ciphertext_distribution[i], plaintext_distribution[i])

                    y=find_key(dictionary_distribution_mapping, plaintext_distribution)

                    # print('ITEM TO DELETE: ', y, '\n')

                    x = possible_plaintexts.remove(find_key(dictionary_distribution_mapping, plaintext_distribution))
                    break

        # possible_plaintexts might be a string of multiple plaintexts if we are not sure which one it could be
        if len(possible_plaintexts) == 1:
            # print("STEP 1")
            return ''.join(possible_plaintexts)
        elif len(possible_plaintexts) == 0:
            error_code = "Unable to find Plaintext!"
            return error_code
        else:

            chi_square_statistic = {}

            for index, plaintext in enumerate(possible_plaintexts):

                dictionary_distribution_mapping[possible_plaintexts[index]] = build_distribution(plaintext)

            # print('HOLLLALALA: ',dictionary_distribution_mapping)

            for plaintext_distribution in dictionary_distribution_mapping.values():

                chi = 0

                for index, letter in enumerate(alphabet.keys()):

                    expected_letters = len(ciphertext) * expected_letter_frequency[letter]

                    diff = pow((expected_letters - plaintext_distribution[index]), 2)

                    if plaintext_distribution[index] == 0:
                        chi += 0

                    else:
                        chi += diff / plaintext_distribution[index]

                
                chi_square_statistic[chi] = plaintext_distribution

            # print(chi_square_statistic)

            chi_square_statistic_sorted = sorted(list(chi_square_statistic.keys()))

            # print(chi_square_statistic_sorted)


            min_chi_val = chi_square_statistic_sorted[0]

            # print(min_chi_val)

            result = find_key(dictionary_distribution_mapping, chi_square_statistic[min_chi_val])

            return result

            # print('plaintext guess is: ', result)
                    



# def calculate_chi_square(ciphertext, possible_plaintexts, expected_frequency):


#     for letter in alphabet.keys():

#         expected_letters = len(ciphertext) * expected_frequency[letter]

#         diff = expected_letters - 




# calculate_chi_square('abcd', 'abcd', expected_letter_frequency)

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


############################################################  MAIN FUNCTION ###################################################

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

    dict_1 = list(dictionary_1.values())

    plaintext_sample = random.choice(range(5))

    key = generate_key(dict_1[plaintext_sample])
    # print("New Key:" + str(key))

    # test_encrypt = encrypt(dict_1[plaintext_sample], key)

    # print('\n Original plaintext: ' + dict_1[plaintext_sample] + '\n')

    # print('\n Generated Ciphertext: ' + '"' + test_encrypt + '"' + '\n')

    user_ciphertext = input("\nPlease enter the ciphertext: \n")

    test_decrypt = decrypt(user_ciphertext, dict_1)

    print('\n Plaintext guess is:\n', test_decrypt)

main()