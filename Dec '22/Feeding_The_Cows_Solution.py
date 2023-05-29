# (Analysis by Mythreya Dharani)
# Let's start by defining a cow as covered if there is a patch feeding its breed within a distance of K. 
# The problem is asking us to cover all cows with the minimum number of patches.

# Consider each cow i from 1…N in that order, placing patches whenever necessary. 
# First of all, if the current cow is already covered, then we don't need to place another patch, and we can just move on. 
# Otherwise, we need to place a new patch for this cow, so where would we place it? Consider what happens if we place the patch at position i+K. 
# Not only will cow i be covered but any cows after it which are within K distance of that patch will also be covered. 
# In fact, placing it at this location maximizes the number of potential cows that can be covered.

# Thus, we can just implement this strategy starting at cow 1. 
# Keep in mind that if there is a cow i which needs to be fed and i+K>N, we can just place our new patch at position i since all remaining same-breed cows can feed off that patch. 
# This solution runs in O(N) time since we are just doing a single pass over the N cows.

# There is actually one edge case; what if when we try to place a patch at position i but there is already a patch there? 
# In this case, we can place the patch at i−1 instead, as it may be proven that there can't already be patches at both i−1 and i. 
# As i−1+K≥N, this patch covers all cows from i to N of the same breed as cow i.

# Nick Wu's Python code:

def solve():
    n, k = (int(x) for x in input().split())
    patches = ['.'] * n
    gCover = -1
    hCover = -1
    s = input()
    for idx, ch in enumerate(s):
        if ch == 'G' and gCover < idx:
            if idx + k >= len(patches):
                if patches[idx] != '.':
                    patches[idx-1] = 'G'
                else:
                    patches[idx] = 'G'
                gCover = n
            else:
                patches[idx+k] = 'G'
                gCover = idx + 2*k
        elif ch == 'H' and hCover < idx:
            if idx + k >= len(patches):
                if patches[idx] != '.':
                    patches[idx-1] = 'H'
                else:
                    patches[idx] = 'H'
                hCover = idx + k
            else:
                patches[idx+k] = 'H'
                hCover = idx + 2*k
    print(n - patches.count('.'))
    print("".join(patches))
 
t = int(input())
for _ in range(t): solve()
