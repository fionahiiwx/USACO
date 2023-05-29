# NOPE

def watch_moo(NK, watch_day):
    if NK[0] == 2:
        if (watch_day[-1] - watch_day[0] + 1) <= NK[-1]:
            return print((watch_day[-1] - watch_day[0] + 1)+NK[-1])
        else:
            return print(NK[0]*(1+NK[-1]))
    tot = 0
    for i in range(1, NK[0]):
        between = (watch_day[i] - watch_day[i-1] + 1)
        if between <= NK[-1]:
            tot += between+NK[-1]
        else:
            tot += (1+NK[-1])
    return print(tot)

NK = list(map(int, input().split(" ")))
watch_day = list(map(int, input().split(" ")))
watch_moo(NK, watch_day)