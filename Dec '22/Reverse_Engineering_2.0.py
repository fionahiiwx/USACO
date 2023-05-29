T = int(input())

def test(B):
    cases = []
    results = True
    for b in range(len(B)):
        opp = []
        if len(cases) == 0:
            cases.append(B[b])
        for c in cases:
            if B[b][0] == c[0] and B[b][-1] != c[-1]:
                results = False
                break
            elif B[b][0] not in c[0]:
                cases.append(B[b])
        for i in range(len(B[b])):
            if B[b][i] == "0":
                opp.append("1")
            else:
                opp.append("0")
        if opp[0][0] not in cases:
            cases.append(opp)
        elif opp[0][0] in cases:
            results = False
    return cases, results

for i in range(T):
    new_case = input()
    n_k = input().split(" ")
    inp = []
    for k in range(int(n_k[-1])):
        inp.append(input().split(" "))
    cases, results = test(inp)
    if results == False:
        print("LIE")
    else:
        print("OK")
