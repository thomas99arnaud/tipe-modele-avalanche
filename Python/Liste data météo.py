def DataMeteoListe () :             # Nord Sud Est Ouest
    L=[]
    #21/12/2021 | Chablais  [ RisqueJJ , [J-6], [J-4], [J-3], [J-2], [J-1],  [J-1], [JJ] ]
    L1 = [ 2 , [ "Soleil" ,1 , 50, 1 , 100] , [ "Soleil", 0 ,25 ,3 ,100 ] , [ "Soleil", 1,30 , 3, 100 ] , ["Soleil",-3 ,30 ,1 , 90] , ["Soleil" ,-3 ,50 ,1 , 85] , ["Soleil", -5, 30 ,2 , 85 ] ]
    
    #06/01/2022  | Chablais
    L2 = [ 3 , [ "Soleil" ,1 , 10, 2 , 60] , [ "Soleil", 1 ,50 ,0 ,50 ] , [ "Pluie", -2,45, 0, 40] , ["Pluie",1 ,80 ,0 , 40] , ["Pluie" ,-3 ,40 ,1 , 55] , ["Soleil", -5, 50 ,0 , 55 ] ] 

    #07/02/2022  | Chablais
    L3 = [ 4 , [ "Pluie" ,-10 , 40, 1 , 80] , [ "Soleil", -8 ,10 ,0 ,80 ] , [ "Soleil", 2,50, 0, 80] , ["Pluie",-4 ,20 ,2 , 80] , ["Soleil" ,-3 ,40 ,0 , 80] , ["Pluie", -3, 50 ,1 , 90 ] ] 
        
    #14/01/2022  | Devoluy
    L4 = [ 2 , [ "Pluie" ,3 , 90, 1 , 65] , [ "Soleil", 3,80 ,1 ,75 ] , [ "Soleil",3,30, 3, 70] , ["Soleil",1 ,30 ,3 , 65] , ["Soleil" ,-2 ,40 ,3 , 65] , ["Soleil", -2, 40 ,3 , 60] ]

    #02/02/2022  | Chartreuse
    L5 = [ 2 , [ "Soleil" ,-1 , 30, 1 , 80] , [ "Soleil", -1,23 ,1 ,80 ] , [ "Soleil",1,25, 1, 80] , ["Pluie",-3 ,25 ,1 , 80] , ["Pluie" ,-3 ,50 ,1 , 80] , ["Pluie", -1, 40 ,1 , 80] ]
    
    #13/01/2022 | Aravis
    L6 = [ 3 , [ "Pluie" ,1 , 0, 0 , 45] , [ "Pluie", 1,53 ,2 ,70 ] , [ "Pluie",1,50, 3, 100] , ["Pluie",1 ,40 ,1 , 110] , ["Soleil" ,0 ,50 ,3 , 105] , ["Soleil", -1, 50 ,3 , 105] ]
    
    L.append (L1)
    L.append (L2)
    L.append (L3)
    L.append (L4)
    L.append (L5)
    L.append (L6)
    
    return L
    
    