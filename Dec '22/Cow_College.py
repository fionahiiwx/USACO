N = int(input())
cows = list(map(int, input().split(" ")))

max_pay = sum(cows)//N
total = 0

for i in range(N):
    if cows[i] >= max_pay:
        total += max_pay

print(total, max_pay)