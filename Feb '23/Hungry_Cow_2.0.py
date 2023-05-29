def count_hay(NT, hays):
    tot = 0
    hay = 0
    if NT[0] == 1:
        if NT[-1] > hays[0][-1]:
            return print(hays[0][-1])
    for day in range(1, int(NT[0])+1):
        hay += hays[day-1][-1]
        if day == int(NT[0]):
            if NT[-1] > hays[day-1][0]:
                if hay > (NT[-1] - hays[day-1][0] + 1):
                    return print((tot+NT[-1]-hays[day-1][0]+1))
                else:
                    return print(tot+hay)
            else:
                if hay != 0:
                    return print(tot+1)
                else:
                    return print(tot)
        elif hays[day][0] > hay:
            tot += hay
            hay = 0
        else:
            b = hays[day][0] - hays[day-1][0]
            hay -= b
            tot += b
    return print(tot)

NT = list(map(int, input().split(" ")))
hays = []

for n in range(NT[0]):
    a = list(map(int, input().split(" ")))
    hays.append(a)

count_hay(NT, hays)