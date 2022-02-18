import random
import copy

f = open('list.txt', 'r')
g = open('ans_list.txt', 'r')
wordList = f.readlines()
ansList = g.readlines()
f.close()
g.close()
wordList = [word[:5] for word in wordList]
ansList = [word[:5] for word in ansList]

n = random.randint(1,len(ansList))
ans = ansList[n]
SYMBOLS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
SYMBOLS_display = copy.copy(SYMBOLS)

while True:
    for i in range(len(SYMBOLS)):
        print(SYMBOLS_display[i], end = '')
    a = input("\ninput answer:")

    if a == ans:
        print("Congratulations!")
        break

    if a not in wordList:
        print('This word not in list.')
        continue

    for i in range(5):
        if a[i] == ans[i]:
            print('\033[32m' + '■' + '\033[0m', end = '')
            SYMBOLS_display[SYMBOLS.index(a[i].upper())] = '\033[32m' + a[i].upper() + '\033[0m'
        elif a[i] in ans:
            print('\033[33m' + '■' + '\033[0m', end = '')
            if SYMBOLS_display[SYMBOLS.index(a[i].upper())] != '\033[32m' + a[i].upper() + '\033[0m':
                SYMBOLS_display[SYMBOLS.index(a[i].upper())] = '\033[33m' + a[i].upper() + '\033[0m'
        else:
            print('■', end = '')
            SYMBOLS_display[SYMBOLS.index(a[i].upper())] = '\033[30m' + a[i].upper() + '\033[0m'
    print()