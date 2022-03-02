import ast
from ctypes import sizeof

inp = input()


all_freq = {}
s = {}
for i in inp:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1 
print(sorted(all_freq))
keys = all_freq.values()
nkeys = list(keys)
print (nkeys)
f = open("freq.txt", "r")
new_freq = f.readlines()
for j in new_freq:
    s = ast.literal_eval(j)
    k = s.values()
    # print(k)
    nk = list(k)
    print(nk)
    # if nkeys == nk:
    #     for l in inp:
    #         print(l.replace(str(all_freq.keys), str(s.keys)))
    #     print("The plaintext is: ")
    # else:
    #     print("Nahh")