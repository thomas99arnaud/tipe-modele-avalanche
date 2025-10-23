def GenereProfil (n) :
    from random import randint
    hmax = 10
    hmin = 2
    G = GenereGrille (n) 
    x = 0
    y = 0 
    for k in range (n//5) : 
        x = randint(0,n-1) 
        y = randint(0,n-1)
        if G[x][y] == 0 :
            G[x][y] = hmax + randint(-3,3)
    return G
        