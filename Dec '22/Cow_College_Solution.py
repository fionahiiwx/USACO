# (Analysis by Freddie Tang and Nick Wu)
# It can be proven that the optimal tuition Bessie should charge will always be one of the ci values 
# (for if not, you could always increase tuition slightly without changing the set of cows who pay). 
# So all we have to do is iterate over these values and see how much money each one makes. 
# To do this, we must first sort these ci values to determine how many cows will be willing to pay, and then iterate from the lowest to the highest, 
# keeping a count of the number of cows willing to pay, (after a ci value is visited, the cow with this value will no longer be able to pay the tuition so the count will be decremented). 
# Remember to use long long's because the answer could be up to 105⋅106=1011.

# There is an alternate solution that does not involve sorting the cows. For each pi, we can maintain the number of cows that are willing to pay up to pi. 
# If we loop over tuition values going from 106 down to 1, 
# we can maintain a running total of how many cows are willing to pay that much tuition and track the maximum amount of money that Bessie can make.

# Nick Wu's Python code:

MAX_TUITION = 1000000
n = int(input())
tuitionToCow = [0] * (MAX_TUITION + 1)
for x in input().split():
    tuitionToCow[int(x)] += 1
maxMoney = 0
bestTuition = 0
currentCows = 0
for tuition in range(MAX_TUITION, 0, -1):
    currentCows += tuitionToCow[tuition]
    if tuition * currentCows >= maxMoney:
        maxMoney = tuition * currentCows
        bestTuition = tuition
print(maxMoney, bestTuition)
