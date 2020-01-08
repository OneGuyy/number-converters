#Ce programme permet de convertir des nombres décimaux (base 10) en nombres binaires (base 2) et vice-versa
#Ce programme utilise la librairie Tkinter afin de créer des fenêtres

import tkinter #librarie de céation de fenêtres

def binToDeci(num):
	'''Convertir les binaires en décimaux'''
	for i in str(num):
		if(i != "0" and i != "1"):
			return "Erreur"
	if (num <= 0):
		return 0
	else:
		numString = list(str(num))
		count = 0
		result = 0
		for i in reversed(numString):
			if(i == "1"):
				result += 2**count
			count += 1
		return result

def deciToBin(x):
	#convertir les décimaux en binaires
    compteur = 0 
    while x >= 2 ** compteur:
        compteur += 1
     
    resultat = ''
    
    for i in range(compteur):
        puissanceDeux = 2 ** (compteur - 1 - i)
        if x >= puissanceDeux:
            resultat += '1'
            x -= puissanceDeux
        else:
            resultat += '0'
    return "0b"  + resultat #On ajoute "0b" afin de spécifier qu'il s'agit de nombres binaires (0b1101 != 1101)

def check():
	'''Fonction vérifie quel mode de conversion a été choisis'''
	result = tkinter.Label(win, text="			  ") #Ligne pour "effacer" le dernier résultat (fonctionne pour une fenetre de 180x200 pixels !)
	result.grid(row=6, column=1)
	if(nConvert.get().isdigit()):
		number = int(nConvert.get())
		if(varGr.get()=="0"):
			result = tkinter.Label(win, text="Réponse : " + str(binToDeci(number)))
			result.grid(row=6, column=1)
		elif(varGr.get()=="1"):
			result = tkinter.Label(win, text="Réponse : " + deciToBin(number))
			result.grid(row=6, column=1)
	else:
		result = tkinter.Label(win, text="Réponse : Erreur")
		result.grid(row=6, column=1)


def printV():
	print(varGr.get())

win = tkinter.Tk()
win.title("CONVERTISSEUR BIDECIMAL")
win.minsize(180, 200)

choice = tkinter.Label(win, text="Choisissez un mode de conversion")
choice.grid(row=0, column=1)

vals = [False, True]
etiqs = ["BINAIRE -> DECIMAL", "DECIMAL -> BINAIRE"]
varGr = tkinter.StringVar()
varGr.set(vals[1])
for i in range(2):
	b = tkinter.Radiobutton(win, variable=varGr, text=etiqs[i], value=vals[i], command=printV)
	b.grid(row=i+1 ,column=1)

text = tkinter.Label(win, text="Nombre à Convertir")
text.grid(row=3, column=1)
nConvert = tkinter.StringVar()
toConvert = tkinter.Entry(win, textvariable=nConvert)
toConvert.grid(row=4,column=1)
button = tkinter.Button(win, text="Convertir", command=check)
button.grid(row=5, column=1)


win.mainloop() #Fin du programme !