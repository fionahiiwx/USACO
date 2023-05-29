import numpy as np

N = int(input())
cows = np.array(list(map(int, input().split(" "))))
vals = []

def condition(x, i):
    return x >= i

for i in range(1, max(cows)):
    bool_arr = condition(cows, i)
    pay_cow = np.where(bool_arr)
    print(pay_cow.tolist())

print(list(val))
vals.sort(key=lambda x: (x[0], -x[1]))
print(" ".join(list(map(str, vals[-1]))))