from collections import Counter
leader_G = False
leader_H = False
tot = 0

def leader(s, e, M):
    global leader_G
    global leader_H
    freq = Counter(M[s:e])
    if freq[M[s]] == M.count(M[s]):
        if M[s] == "G":
            leader_G = s
        else:
            leader_H = s

N = int(input())
M = input().upper()
E = list(map(int, input().split(" ")))

for n in range(N):
    if (leader_H is not False) and (leader_G is not False):
        break
    elif leader_H is not False:
        if M[n] == "H":
            continue
    elif leader_G is not False:
        if M[n] == "G":
            continue
    leader(n, E[n], M)

if leader_H is not False and leader_G is not False:
    tot += 1

for h in [h for h in range(len(M[:leader_H])) if M[h] != "H"]:
    if h < leader_H and leader_H < E[h]:
        tot += 1
for g in [g for g in range(len(M[:leader_G])) if M[g] != "G"]:
    if g < leader_G and leader_G < E[g]:
        tot += 1

print(tot)