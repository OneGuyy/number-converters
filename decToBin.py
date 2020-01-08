def convert(x):
		compteur = 0 #Le compteur pour 2^y
		puissanceDeux = 1
		while(x > puissanceDeux): #Tant que x est plus petit que la fonction 2^y, la boucle tourne
			puissanceDeux *= 2	  #2^(y+1)
			if(x < puissanceDeux):	#2ème vérification pour éviter que le compteur compte trop
				puissanceDeux /= 2
				break			  	#Si x est plus petit que la fonction, alors on arrête la boucle
			compteur += 1         #On ajoute 1 au compteur, celui ci servira pour calculer le nombre en binaire
		resultat = 0 #Variable qui stockera la valeur convertie
		ajout = puissanceDeux
		while(compteur != 0):
			if(x >= puissanceDeux):
				resultat += 10**compteur
			else:
				puissanceDeux -= ajout
			ajout = ajout/2
			puissanceDeux += ajout
			compteur -= 1
		if(x%2==1):
			return resultat+1
		return resultat

def convert2(x):
    compteur = 0 
    while x >= 2 ** compteur:
        compteur += 1
    # 
    resultat = ''
    #
    for i in range(compteur):
        puissanceDeux = 2 ** (compteur - 1 - i)
        if x >= puissanceDeux:
            resultat += '1'
            x -= puissanceDeux
        else:
            resultat += '0'
    return "0b"  + resultat

def convert3(x):
	quotien, reste = -1, 0
	resultat = ''

	while(x != 0):
		reste = x % 2
		x = x // 2
		resultat += str(reste)
	return '0b' + resultat[::-1]

def convert4(x, resultat = ''):
	if x == 0: return "0b" + resultat[::-1]
	else: return convert4(x//2, resultat + str(x%2)) 
 


#toBin = int(input("Number to convert : "))
print(convert(121), " - ", convert2(121), " - ", convert3(121), " - ", convert4(121)) #-> 1101
