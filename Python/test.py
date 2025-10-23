fichier = open("C:/Users/thomas/Pictures/TIPE Avalanches/Programmes/relou.txt")
L = []
for ligne in fichier :
    L.append ( ligne ) 
for k in range (len (L) ) :
    L[k].split(";")
fichier.close()