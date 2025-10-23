#Le but de cet algorithme est de génerer un bulletin météo réaliste.
#Pour cela il génerera un 5-uplet pour 6 jours consécutifs : [Temps(Soleil,Pluie) , Température(°C), Vent(km/h), Sens du vent({0,1,2,3}), Enneigement(cm)].
#Pour notre étude nous supposerons le temps, la température, le vent, son sens et l'enneigement uniforme sur toute la zone étudiée. 
#On supposera que le vent ne souffle que dans une seule direction à la fois.
def GenereBulletinMeteo () :
    from random import randint 
    Bulletin = []
    #Initialiastion jour 0 :
    Te = 0      
    TC = 0
    V = 0
    dV= 0
    E = 0
    
    if randint(0,1) == 1 :            #Probabilité de 1 chance sur 2
        Te = "Pluie"
    else : 
        Te = "Soleil"
    if Te == "Pluie" : 
        TC = -6 + randint(-3,3)
    else :
        TC = 9 + randint(-3,3)
    if Te == "Pluie" :
        V = 30 + randint(0,20)
    if Te == "Pluie" : 
        dV = randint(0,3)
    E = 125 + randint(-50,50)
    
    Bulletin.append([Te,TC,V,dV,E])
     
    
    for k in range (5) : 
        Te, TC, V, dV, E = 0,0,0,0,0
        #Temps qu'il fait 
        if Bulletin[k][0] == "Pluie" :
            if randint(0,1) == 0 :      #<-- 1 chance sur 2
                Te = "Pluie"
            else :
                Te = "Soleil"
        else : 
            if randint(0,7) == 0:       #<-- 1 chance sur 8
                Te = "Pluie"
            else :
                Te = "Soleil"
                
        #Température
        if Bulletin[k][0] == "Pluie" :
            if Te == "Pluie" :
                TC = Bulletin[k][1] + randint(-5,5)
            if Te == "Soleil" :
                TC = Bulletin[k][1] + randint(-5,5) + 15
        else :
            if Te == "Pluie" :
                TC = Bulletin[k][1] + randint(-5,5) - 15
            if Te == "Soleil" :
                TC = Bulletin[k][1] + randint(-5,5)
                
        #Vent
        if Te == "Pluie" :
            V = 30 + randint(0,20)
        
        #Sens du vent 
        if Bulletin[k][0] == "Pluie" :
            if randint(0,1) == 0 :
                dV = Bulletin[k][3]
        else :
            dV = randint(0,3)
            
        #Enneigement 
        
        if Te == "Pluie" :
            E = Bulletin[k][4] + randint(-3,3) + 10
        else :
            E = Bulletin[k][4] + randint(-2,2) - 5 
            
        Bulletin.append([Te,TC,V,dV,E])
    return Bulletin
     