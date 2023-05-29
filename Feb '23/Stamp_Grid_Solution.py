# (Analysis by Claire Zhang)
# Consider stamping wherever possible - that is, for each position and rotation of the stamp, if stamping here would only paint on black grid cells, stamp here. 
# If there is a sequence of stampings S that produces the grid, then stamping wherever would also produce the grid because it would contain each individual stamping in Sand it will never "overstamp".
# Therefore, it suffices to check at each of (N−K+1)2 positions and under each of 4 rotations whether the K×K region has paint in every cell the stamp has paint.

# To try each position, we can use a nested for loop - one over x and one over y. To account for rotations, we can nest another loop that runs 4times - after each iteration, we rotate our stamp.
# We can rotate our stamp array by setting stamp[i][j] to stamp[j][K−1−i] (0-indexed). 
# See code for implementation details.

# Ben's code:

T = int(input())
for _ in range(T):
    input()
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    K = int(input())
    stamp = [input() for _ in range(K)]
    ans = [['.' for _ in range(N)] for _ in range(N)]
    for rot in range(4):
        for i in range(N-K+1):
            for j in range(N-K+1):
                if all(grid[i+a][j+b] == '*' or stamp[a][b] == '.' for a in range(K) for b in range(K)):
                    for a in range(K):
                        for b in range(K):
                            if stamp[a][b] == '*':
                                ans[i+a][j+b] = '*'
        stamp = [[stamp[j][K-1-i] for j in range(K)] for i in range(K)]
    print("YES" if grid == ans else "NO")
