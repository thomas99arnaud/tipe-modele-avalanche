def IndiceRisqueAvalanche(L) : 
    
    I = 0
    IV = 0
    IE = 0
    IM = 0
    B = L
    #On considère le jour J comme le jour 6 du bulletin (position 5)
    #1 : Indicie de risque lié au vent :
    if B[5][2] < 30 :
        IV = 1
    if B[5][2] > 30 and B[5][3] < 40  :
        IV = 2
    if B[5][2] > 40 and B[5][3] < 50  :
        IV = 3
    if B[5][2] > 50 :
        IV = 4
        
    #2 : Indice de risque lié à l'enneigement :
    if B[5][4] < 50 :
        IE = 1
    if B[5][4] > 50 and B[5][4] < 100 :
        IE = 2  
    if B[5][4] > 100 and B[5][4] < 150 :
        IE = 3  
    if B[5][4] > 150 :
        IE = 4  
    
    #3 : Indice de risque lié à la météo :
    #3.1 : Patterns risques 4 :
    if B[5][0] == "Soleil" and B[4][0] == "Soleil" and B[3][0] == "Pluie" and B[3][1]<0 and B[2][0] == "Soleil" and B[1][0] == "Soleil" : 
        IM = 4
    elif B[4][0] == "Soleil" and B[3][0] == "Soleil" and B[2][0] == "Pluie" and B[2][1]<0 and B[1][0] == "Soleil" and B[0][0] == "Soleil" : 
        IM = 4
    elif B[5][0] == "Soleil" and B[4][2] > 30  and B[3][1] < 0 and B[2][1] < 0 and B[1][0] == "Pluie" and B[1][1] < 0 :
        IM = 4
    elif B[5][0] == "Pluie" and B[5][1] > 0 and B[4][0] == "Pluie" and B[4][1] > 0 and B[3][0] == "Pluie" and B[3][1] < 0 and B[2][1] < 0 :
        Im = 4
    
    #3.2 : Patterns de risque 3 :
    if IM == 0 :
        for k in range (2) : 
            if B[k][0] == "Soleil" and B[k+1][0] == "Soleil" and B[k+2][0] == "Pluie" and B[k+2][1] < 0 and B[k+3][0] == "Soleil" :
                IM = 3
        for k in range (2) : 
            if B[k][0] == "Soleil" and B[k+2][0] == "Soleil" and B[k+1][0] == "Pluie" and B[k+1][1] < 0 and B[k+3][0] == "Soleil" :
                IM = 3
        if B[5][0] == "Soleil" and B[4][2] > 30 and B[3][2] < 0 and B[2][0] == "Pluie" and B[2][1] < 0 :
            IM = 3
        elif B[5][0] == "Soleil" and B[4][2] > 30 and  B[3][0] == "Pluie" and B[3][1] < 0 :
            IM = 3
        elif B[5][2] > 30 and B[4][1] < 0 and B[3][1] < 0 and B[2][1] < 0 and B[2][0] == "Pluie" :
            IM = 3
    
    #3.3 : Patterns de risque 2:
    if IM == 0 :
        for k in range (3) :
            if B[k][0] == "Soleil" and B[k+1][0] == "Pluie" and B[k+1][1] < 0 and B[k+2][0] == "Soleil" :
                IM = 2 
        for k in range (4) :
            if B[k][1]<0 and B[k+1][2] > 30 :
                IM = 2
            elif B[k][2] > 30 and B[k+1][0] ==  "Soleil" :
                IM = 2
            elif B[k+1][0] == "Pluie" and B[k+1][1]<0 and B[k][1] < 0 :
                IM = 2
        
    #3.4 : Patterns de risque 1 :
    
    if IM == 0 :
        IM = 1
        
    I = round( ( (IM + IV + IE ) / 3) , 0)
    
    return( int(I) )
            
        
        
    
    