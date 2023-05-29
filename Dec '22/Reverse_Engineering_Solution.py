# (Analysis by Nick Wu)
# To solve the subtask where N=2, we can brute force all possible programs that Elsie could have written and see if any of those programs could have given the observed output.

# To solve the subtask where M=2, we can prove that the only time when Elsie must be lying is when the two inputs are equal and the two outputs are not equal. 
# Obviously, in this situation Elsie must be lying. If the two inputs and outputs are equal, then this is equivalent to the case where M=1 and the answer when M=1 is always OK. 
# Otherwise, pick some variable where the two inputs vary and return the correct result based on the value of that variable.

# To fully solve the problem, let us assume that Elsie is not lying, and consider the first if statement that Elsie has in her program. 
# If we take that variable v and desired value x and look at all input/output pairs where v takes on value x, those outputs must all be equal to the return value from the first if statement.

# Therefore, let us construct Elsie's program from top to bottom as follows: identify some variable v and value x where all given inputs that match share the same output value. 
# Delete all such input/output pairs. Repeat this process until we have at most one input/output pair, then the answer is OK. 
# If we cannot find such a variable/value pair at any point, then the answer is LIE.

# If this procedure outputs OK, then we have constructed a valid program and we have correctly printed out OK. 
# Therefore, it remains to prove that if Elsie was lying, this procedure will properly detect it. 
# The concern here is that perhaps the order in which we write the if statements matters, and if we can order them differently, we might be able to get a valid program.

# The reason that this concern does not matter is that, the moment we can add an if statement of the form that variable v takes on value x, 
# we can always write this if statement in the future and it will not exclude additional inputs. Therefore, there is no benefit to rearranging if statements.

# My Python code:

def solve():
    nvars, ninputs = (int(x) for x in input().split())
    inputs = []
    results = []
    for _ in range(ninputs):
        data = input().split()
        inputs.append(data[0])
        results.append(data[1])
    programs = [i for i in range(ninputs)]
    while True:
        updated = False
        for i in range(nvars):
            if updated:
                break
            offvals = set()
            offinputs = []
            onvals = set()
            oninputs = []
            for j in programs:
                if inputs[j][i] == '1':
                    onvals.add(results[j])
                    oninputs.append(j)
                else:
                    offvals.add(results[j])
                    offinputs.append(j)
            if len(offvals) <= 1 and len(onvals) <= 1:
                print("OK")
                return
            if len(offvals) == 0 or len(onvals) == 0:
                continue
            if len(offvals) == 2 and len(onvals) == 2:
                continue
            if len(offvals) == 1:
                updated = True
                programs = oninputs
            elif len(onvals) == 1:
                updated = True
                programs = offinputs
            else:
                assert False
        if not updated:
            print("LIE")
            return
 
t = int(input())
for _ in range(t):
    input()
    solve()
