T = int(input())
def test(B):
    if "1" in B:
        return 1
    else:
        return 0
for i in range(T):
    new_case = input()
    n_k = input().split(" ")
    for k in range(int(n_k[-1])):
        inp = input().split(" ")
        M = test(inp[0])
        if M != int(inp[-1]):
            print("LIE")
            for l in range(k+1, int(n_k[-1])):
                a = input()
            break
        elif k == int(n_k[-1])-1:
            print("OK")