def moo_op(word):
    if "MOO" in word:
        new = word.replace("MOO","",1)
        return len(new)
    elif

n = int(input())
for _ in range(n):
    w = input()
    print(moo_op(w))