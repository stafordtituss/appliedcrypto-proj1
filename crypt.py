import ast
from ctypes import sizeof

def ciphertext_to_plaintext(ciphertext_dict, plaintext_dict):

    plaintext = ""

    for letter in ciphertext_dict.keys():

        letter_freq = ciphertext_dict.get(letter)

        for plaintext_key, plaintext_freq in plaintext_dict.items():
            if plaintext_freq == letter_freq:
                print(plaintext_key + ' -----> ' + str(plaintext_freq))
                break

    return plaintext


def main():
    inp = input()

    result =''
    ciphertext = {}
    s = {}
    for i in inp:
        if i in ciphertext:
            ciphertext[i] += 1
        else:
            ciphertext[i] = 1 
    # print(ciphertext)
    # print(sorted(ciphertext))
    frequency = ciphertext.values()
    nfreq = list(frequency)
    # print (nkeys)
    f = open("freq.txt", "r")
    plaintext_frequency = f.readlines()
    for line in plaintext_frequency:
        plaintext_line = ast.literal_eval(line)
        print(plaintext_line)
        # print(nk)
        # if nkeys == nk:
        #     for l in inp:
        #         print(l.replace(str(ciphertext.keys), str(s.keys)))
        #     print("The plaintext is: ")
        # else:
        #     print("Nahh")

        result += ciphertext_to_plaintext(ciphertext, plaintext_line)

    print(result)

    f.close()

main()