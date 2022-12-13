def addition(x:int,y:int=2)->int: # annotations de typage attendu (non traité en l'état par l'interpréteur python)
    """
    Additionne les 2 nombres
    passés en arguments
    """
    return x+y # renvoie la somme de x et y

print(addition(10,5)) # appel de la fonction 'addition' et affichage de la somme
resultat=addition(7,3) # appel de la fonction 'addition' et stockage dans une variable 'resultat'
print(resultat) # affichage de la variable 'resultat'
print(addition(5)) # appel de la fonction 'addition' avec un seul argument, la fonction utilise la valeur de y par défaut