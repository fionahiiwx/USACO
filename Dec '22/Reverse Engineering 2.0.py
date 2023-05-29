the_list = input().split("\n")

def test(B):
    for b in range(len(B)):
        if (int(B[1]) == 1):
            return 1
        elif (int(B[0]) == 0):
            return 0
        else:
            return 1

def test_1(B):
    if B == 0:
        return 0
    else:
        return 1

for i in range(the_list[0]):
    n_k = the_list[i][0].split(" ")
    for k in range(int(n_k[-1])):
        inp = input(": ").split(" ")
        if int(n_k[0]) > 1:
            b = inp[0]
            M = test(inp[0])
        else:
            M = test_1(int(inp[0]))
        if M != int(inp[-1]):
            print("LIE")
            break
        elif k == int(n_k[-1])-1:
            print("OK")