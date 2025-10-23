import numpy as np
import matplotlib.pyplot as plt 

def CompareMeteo() : 
    L = DataMeteoListe()
    X = []
    Y = []
    P = []
    Z = []
    for k in range ( len (L)) :
        X.append( L[k][0] )
    for k in range ( len (L) ):
        for i in range (1, len(L[0]) ) :
            P.append( L[k][i] ) 
        Y.append( IndiceRisqueAvalanche(P) )
        P = []
    for k in range (len(L)) : 
        Z.append(k+1)
    x = np.array(X)
    y = np.array(Y)
    z = np.array(Z)
    plt.plot(z, x, "g:o" , label="estimations MeteoFrance")
    plt.plot(z, y ,    "b:o"  ,label="Mes estimations")
    
    plt.ylabel("Indice Risque Avalanche")
    plt.xlabel("Essai n°")


    plt.legend()

    plt.title("Comparaison résultats/réalité ")

    
    plt.show()
