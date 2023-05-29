N = int(input())
cows = list(map(int, input().split(" ")))
vals = [[sum(1 for j in cows if j >= i)*(i), i] for i in cows]
vals.sort(key=lambda x: (x[0], -x[1]))
print(" ".join(list(map(str, vals[-1]))))