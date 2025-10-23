def PourcentageIndices (n) : 
    L = [0,0,0,0]
    for k in range (n) : 
        L[ int( (IndiceRisqueAvalanche() ) - 1 ) ] += 1 
    for k in range (len(L)) : 
        L[k] = (100 * L[k]) / n
    return L 