def count_hay(NT, hays):
    hay = 0
    tot = 0
    count = 0
    for t in range(NT[1]):
        if count < NT[0]:
            for h in range(len(hays)):
                if hays[h][0] == (t+1):
                    if hay == 0:
                        hay = hays[h][1]
                    else:
                        hay += hays[h][1]
                    count += 1
        elif count == NT[0]:
            remain = NT[-1] - t+1
            if hay > remain:
                tot += remain
            else:
                tot += hay
            break
        if hay > 0:
            hay -= 1
            tot += 1
    print(tot)

NT = list(map(int, input().split(" ")))
hays = []

for n in range(NT[0]):
    a = list(map(int, input().split(" ")))
    hays.append(a)

count_hay(NT, hays)