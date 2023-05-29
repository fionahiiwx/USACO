# NOPE
# 5 5
# 1 4 9 18 21
# Don't work

def watch_moo(NK, watch_day):
    if NK[0] == 2:
        if (watch_day[-1] - watch_day[0] + 1) <= NK[-1]:
            return print((watch_day[-1] - watch_day[0] + 1)+NK[-1])
        else:
            return print(NK[0]*(1+NK[-1]))
    tot = 0
    count = 0
    for i in range(1, NK[0]+1):
        if (i != NK[0]) and watch_day[i] - watch_day[i-1] == 1:
            count += 1
            continue
        elif ((i == NK[0]) or watch_day[i] - watch_day[i-1] != 1) and count > 0:
            tot += count + 1 + NK[-1]
            count = 0
            if i == NK[0]-1:
                tot += 1+NK[-1]
            else:
                continue
        if (i < NK[0]):
            between = (watch_day[i] - watch_day[i - 1] + 1)
            if between <= NK[-1]:
                tot += between + NK[-1]
            else:
                tot += (1 + NK[-1])
    dumb = watch_day[-1] - watch_day[0] + 1 + NK[-1]
    return print(min(tot,dumb))

NK = list(map(int, input().split(" ")))
watch_day = list(map(int, input().split(" ")))
watch_moo(NK, watch_day)