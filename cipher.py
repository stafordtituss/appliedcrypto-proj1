import random

alphabets = [' '] + [chr(i + ord('a')) for i in range(26)]
print(alphabets)

alphabets_map = {}
for i in range(len(alphabets)):
    alphabets_map[alphabets[i]] = i
print(alphabets_map)

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

def generate_plaintext():
    plaintext = ""
    while len(plaintext) <= 500:
        new_word = random.choice(dictionary_2)
        if len(new_word) + len(plaintext) >= 500:

            while len(plaintext) < 500:
                plaintext += ' '
            break
        else:
            plaintext += new_word + ' '
    print("Task 2 plaintext:", '"'+plaintext+'"', len(plaintext))
    return plaintext

def generate_keys1():
    keys = []
    for key in range(len(dictionary_1) - 1):
        keys.append(random.sample(alphabets, len(alphabets)))
    print(keys)
    return keys

def encrypt(message, keys):
    prob_of_random_ciphertext = [0, 1]
    ciphertext = ''
    for i in range(len(dictionary_1) - 1):
        for char in range(len(message)):
            coin_choice = random.choice(prob_of_random_ciphertext)
            # print(coin_choice)
            while coin_choice == 0:
                ciphertext += random.sample(alphabets, k=1)
            if message[char] == ' ':
                letter = 0
            else:
                letter = ord(message[char]) - ord('a') + 1
            # print(alphabets[(letter - 1) % 27])
            ciphertext += keys[letter]
    return ciphertext

def build_distribution(ciphertext):
    distribution = [0 for i in range(len(alphabets))]
    for c in ciphertext:
        distribution[alphabets_map[c]] += 1
    return distribution



def main():
    keys = generate_keys1()
    encrypt(dictionary_1[1], keys)
main()
