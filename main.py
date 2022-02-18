f = open('ans_list.txt', 'r')
wordList = f.readlines()
f.close()
wordList = [word[:5] for word in wordList]
ans = [-1, -1, -1, -1, -1]
res = []
non = []

while True:
    a = input("input answer:")
    k = input("input result:")
    
    if k == "ggggg":
        print("Congratulations!")
        break

    for i in range(5):
        if k[i] == "g":
            ans[i] = a[i]
    for i in range(5):
        if k[i] == "y":
            res.append(a[i])
    for i in range(5):
        if k[i] != "g" and k[i] != "y":
            non.append(a[i])

    kouho = []
    for word in wordList:
        flag = True
        for i in range(5):
            if ans[i] != -1:
                if ans[i] != word[i]:
                    flag = False
                    break
        for symbol in res:
            if symbol not in word:
                flag = False
                break
        for symbol in non:
            if symbol in word:
                flag = False
                break
        if flag:
            kouho.append(word)
    print(kouho)