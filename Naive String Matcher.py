def naiveStringMatcher(T, P):
    n = len(T)
    m = len(P)

    for s in range(n - m + 1):
        if P[0:m] == T[s : s + m]:
            print("Pattern Found with shift", s)
           
        


T = "thequickbrownfoxjumpsoverthelazydogover"
P = "over"

naiveStringMatcher(T, P)




