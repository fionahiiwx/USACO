def MOO_operation(word):
    tot = 0
    if word == "MOO":
        return 0
    if "MOO" in word:
        new = word.replace("MOO", "", 1)
    elif "OOO" in word:
        new = word.replace("OOO", "", 1)
        tot += 1
    elif "MOM" in word:
        new = word.replace("MOM", "", 1)
        tot += 1
    elif "OOM" in word:
        new = word.replace("OOM", "", 1)
        tot += 2
    else:
        return -1
    tot += len(new)
    return tot

N = int(input())
for i in range(N):
    word = input().upper()
    print(MOO_operation(word))