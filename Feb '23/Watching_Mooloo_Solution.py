# (Analysis by Spencer Compton)
# As our goal is to determine when Bessie should be subscribing to Mooloo, we begin by thinking about what optimal time periods for subscribing might look like.
# Our solution must involve Bessie subscribing for contiguous segments of days, as well as ranges where Bessie is unsubscribed in between these subscription segments.

# Let us consider the gap between any two days di and di+1 where Bessie must watch Mooloo. Bessie essentially has two choices:

# Bessie continues her subscription from di to di+1. 
# This means she will additionally pay di+1−di−1 moonies for the days in between.
# Bessie will cancel her subscription after di and restart on day di+1. 
# The cost of restarting a new subscription will be an additional K moonies for Bessie.
# Accordingly, Bessie can compare these two costs and choose the smaller one. Meaning, if the cost of the first option is smaller, she will continue her subscription between di and di+1.
# Otherwise, she will cancel her subscription after day di and restart on day di+1.

# Given this strategy, we can iterate through the days and determine the total cost for Bessie in O(n) time.
  
# Benjamin Qi's Python code:

N, K = map(int, input().split())
days = [int(x) for x in input().split()]
print(K + days[-1] - days[0] + 1 + sum(min(K - (d1 - d0 - 1), 0) for d0, d1 in zip(days, days[1:])))
Spencer Compton's Python code:

N, K = map(int, input().split())
days = [int(x) for x in input().split()]
ans = 0
for i in range(N):
    if i == 0:
        # It is the first day, I must start a new subscription
        ans += K + 1
    else:
        # Decide whether to extend a subscription, or end it and start a new one
        extendCost = days[i] - days[i-1]
        newCost = K + 1
        ans += min(extendCost, newCost)
print(ans)
