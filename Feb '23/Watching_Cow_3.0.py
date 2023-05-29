def watch_moo(NK, watch_day):
    if NK[0] == 2:
        if (watch_day[-1] - watch_day[0] + 1) <= NK[-1]:
            return print((watch_day[-1] - watch_day[0] + 1)+NK[-1])
        else:
            return print(NK[0]*(1+NK[-1]))
    dumb = watch_day[-1] - watch_day[0] + 1 + NK[-1]
    sums = []
    for i in range()

NK = list(map(int, input().split(" ")))
watch_day = list(map(int, input().split(" ")))
watch_moo(NK, watch_day)