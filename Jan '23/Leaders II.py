from collections import Counter

N = 4
queue = "GGH"
E = [2,3,3]
hLeader = False
gLeader = False
total = 0
save = {}
save["H"] = []
save["G"] = []
print(save)
currList = []

def breed(start, end, queue):
    global hLeader
    global gLeader
    cow1 = queue[start]
    freq = Counter(queue[start:end])
    if freq[cow1] == queue.count(cow1):
        if cow1 == "H":
            hLeader = start
        else:
            gLeader = start

for i in range(len(queue)):
    currList = list(range(i,E[i]))
    if gLeader is not False and hLeader is not False:
        break
    elif gLeader is not False:
        for z in save["G"]:
            if hLeader in z:
                print(len(save["G"]) - 1)
                save["G"].pop(0)
                total += 1
        if queue[i] == "G":
            continue
    elif hLeader is not False:
        for z in save["H"]:
            if hLeader in z:
                print(len(save["H"]) - 1)
                save["H"].pop(0)
                total += 1
        if queue[i] == "H":
            continue
    breed(i, E[i], queue)
    save[queue[i]].append(currList)
    print(save)

if gLeader is not False and hLeader is not False:
    total += 1

print(total)