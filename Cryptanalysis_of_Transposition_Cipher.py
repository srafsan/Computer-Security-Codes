import enchant
from itertools import permutations, combinations
import random

my_dict = enchant.Dict("en_us")

cipherMat = [
    ['H', 'A', 'K', 'Y'],
    ['T', 'N', 'O', 'U']
]


def checkWordExists(ct):
    allPermutations = [''.join(p) for p in permutations(ct)]
    for x in allPermutations:
        if my_dict.check(x):
            return x
    return False


def allPossibleSubSequences(st):
    combs = []
    new = []
    for r in range(2, len(st) + 1):
        combs.append(list(combinations(st, r)))

    for comb in combs:
        for t in comb:
            new.append(''.join(t))
    return new


def removeSubsequence(st, sub):
    if len(sub) > len(st):
        return False
    ml = len(st)
    sl = len(sub)
    for s in sub:
        if s in st:
            st = st[:st.index(s)] + st[st.index(s) + 1:]
    if ml == len(st) + sl:
        return st
    return False


ans = ""
cipherText = ""
for i in cipherMat:
    for j in i:
        cipherText += j

print('Given Cipher Text: ', cipherText)
allSubsequences = allPossibleSubSequences(cipherText)
checkCipherText = cipherText

ansCipherMat = []

while True:
    if len(checkCipherText) == 0 and len(ans) == len(cipherText):
        break

    ans = ""
    ansCipherMat = []
    checkCipherText = cipherText
    random.shuffle(allSubsequences)

    for i in allSubsequences:
        ok = True
        for j in i:
            if j not in checkCipherText:
                ok = False
                break
        if not ok:
            continue

        word = checkWordExists(i)
        if word and len(word) > 0:
            newCt = removeSubsequence(checkCipherText, word)

            if newCt and len(newCt) >= 0:
                checkCipherText = newCt
                ans += word
                ansCipherMat.append(word)
                if len(checkCipherText) > 1 and my_dict.check(checkCipherText):
                    ans += checkCipherText
                    ansCipherMat.append(checkCipherText)
                    checkCipherText = ""

        if len(checkCipherText) <= 1:
            break

print('Plain Text       : ', ans)

print('Generate Words   : ', end=' ')
for i in ansCipherMat:
    print(i, end=' ')

print(my_dict.check("YUO"))