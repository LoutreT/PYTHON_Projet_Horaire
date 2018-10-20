###### IMPORTATION DES MODULES REQUIS ######
from Tkinter import *			
from time import gmtime, strftime, sleep
#####################################

#Creation de la fenetre principale
root = Tk()
root.resizable(width=False, height=False) # Fenetre non resizable
root.geometry("130x40+0+0")
root.overrideredirect(1) #Masquer la decoration de fenetre
root.config(bg="red") # Couleur de fond : Rouge
Label_Heure = Label(root, font=('', 20, 'bold'), bg='green') # Label qui contient l'heure
Label_Heure.pack()
###### FONCTION D'AFFICHAGE DE L'HEURE ######
def Heure():
	Label_Heure.config(text=strftime('%H:%M:%S'))
	Label_Heure.after(200, Heure) #Rafrichissement du Label qui contient l'heure#

Heure()
root.mainloop()





## COMMENT : ##
## Cette source affiche l'heure dans une fenêtre Tkinter sans décoration de fenête. ##
## Cette source n'est certainement pas très utile, mais elle a le mérite d'être bien codée, et elle peut servir de base pour d'autres. ##
## Le principe : ##
## 1)Création de la fenêtre. ##
## 2)Mettre l'heure dans le Label. ##
## 3)Réactualiser le Label toutes les 1 seconde. ##
## Elle n'a pas été testée sous Linux, mais elle devrait fonctionnée. ##
