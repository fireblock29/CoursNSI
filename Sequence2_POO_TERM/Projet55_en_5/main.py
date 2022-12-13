#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:13:19 2020

@author: Lucas
"""

# import des modules nécessaires et ceux
# créés précédemment
from tkinter import *
from functools import partial
import joueurs
import des
from random import randint


# affiche les résultats du lancer de dés sous forme graphique
def maj_affichage(valeurs):
    global des1, des2, des3
    val1, val2, val3, prenom, points, coups=valeurs
    if points>=score_cible and coups<=nbre_coups:
        affiche.set(prenom+" gagne la partie")
        fin=True
    elif coups<=0: #Si le nombre de coups est inférieur ou égal à 0, mais que l'objectif de points n'est pas atteint, le joueur a perdu
        affiche.set("Vous avez perdu "+prenom)
        fin=True
    else:
        affiche.set("Score du joueur "+prenom)
        fin=False
    score.set(str(points))
    des1 = PhotoImage(file='./Images/face_'+str(val1)+'.png', master=Jeu)
    des2 = PhotoImage(file='./Images/face_'+str(val2)+'.png', master=Jeu)
    des3 = PhotoImage(file='./Images/face_'+str(val3)+'.png', master=Jeu)
    zone_dessin.itemconfigure(id1, image=des1)
    zone_dessin.itemconfigure(id2, image=des2)
    zone_dessin.itemconfigure(id3, image=des3)
    return fin


# fonction appelée lorsque le joueur appuie sur son bouton
def joueur_joue(j):
    global fini1, fini2
    if j==1: #Joueur 1
        btnJoueur1.config(state=DISABLED)
        lancer_joueur=joueur1.lance(de1,de2,de3)
        etat=maj_affichage(lancer_joueur)
        if fini1!=True:
            btnJoueur2.config(state=NORMAL)
        if etat==True:
            btnJoueur1.config(state=DISABLED)
            fini1=True

    else: #Joueur 2
        btnJoueur2.config(state=DISABLED)
        lancer_joueur=joueur2.lance(de1,de2,de3)
        etat=maj_affichage(lancer_joueur)
        if fini2!=True:
            btnJoueur1.config(state=NORMAL)
        if etat==True:
            btnJoueur2.config(state=DISABLED)
            fini2=True

    if fini1==True and fini2==True: #Si les 2 joueurs ont fini, on désactive les 2 boutons
        btnJoueur1.config(state=DISABLED)
        btnJoueur2.config(state=DISABLED)

   
# initialise les valeurs des 3 dés pour afficher une image
def init():
    return randint(1,6),randint(1,6),randint(1,6)


#Programme principal

# tirage àléatoire de 3 valeurs entre 1 et 6 incluses
# récupération des prénoms des joueurs
val1, val2, val3 = init()
nbre_coups=5
score_cible=55

# création des 3 objets "dés"
de1=des.De("D1")
de2=des.De("D2")
de3=des.De("D3")

# Création des 2 objets "joueurs "
joueur1=joueurs.Joueur("Alice")
joueur2=joueurs.Joueur("Bobby")

#Etat des joueurs
fini1=False
fini2=False

# Création de l'interface graphique
Jeu = Tk()

monCadre = Frame(Jeu,  bd=1, relief=RIDGE)
monCadre.pack(padx=5, pady=5)

Jeu.title('55 en 5 coups')
Jeu.geometry('700x600')
Jeu.resizable(width=False, height=False)
Jeu['bg'] = 'white'

affiche = StringVar()
affiche.set('À vous de jouer !')
message = Label(Jeu, textvariable = affiche)
message.pack(padx=5, pady=5)


score = StringVar()
affiche_score = Label(Jeu, textvariable=score)
affiche_score.pack(padx=5, pady=5)

zone_dessin = Canvas(Jeu, bg='white', height=400, width=600)
zone_dessin.pack()

des1 = PhotoImage(file='./Images/face_'+str(val1)+'.png', master=Jeu)
des2 = PhotoImage(file='./Images/face_'+str(val2)+'.png', master=Jeu)
des3 = PhotoImage(file='./Images/face_'+str(val3)+'.png', master=Jeu)

id1=zone_dessin.create_image(100,200, image=des1)
id2=zone_dessin.create_image(300,200, image=des2)
id3=zone_dessin.create_image(500,200, image=des3)


btnJoueur1 = Button(Jeu, text=joueur1.prenom, command=partial(joueur_joue,1))
btnJoueur1.pack(padx=5, pady=5, side=LEFT)

btnJoueur2 = Button(Jeu, text=joueur2.prenom, command=partial(joueur_joue,2))
btnJoueur2.pack(padx=5, pady=5, side=LEFT)

monBoutonQuitter = Button(Jeu, text='Quitter', command=Jeu.destroy)
monBoutonQuitter.pack(padx=5, pady=5, side=LEFT)


Jeu.mainloop()
