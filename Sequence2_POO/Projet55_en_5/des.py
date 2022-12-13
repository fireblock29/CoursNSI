import random
class De :
    """
    Classe implémentant un dé
    Nécessite l'import du module random
    """
    nb_des:int=0 #nombre de dé(s) instancié(s)
        
    def __init__(self, nom, couleur:str='red'):
        """
        Constructeur
        Initialisation des 3 attributs de classe :
            nom (chaine de caractères)
            couleur (chaine de caractères, par défaut 'red')
            valeur (1)
        """
        De.nb_des+=1 #incrémentation de la variable de classe
        self.nom=nom
        self.couleur=couleur
        self.valeur=1
        
    def hasard(self):
        """
        Donne une valeur aléatoire entre 1 et 6 au dé 
        """
        self.valeur=random.randint(1,6)
        return self.valeur
    
    def __repr__(self):
        """
        Affiche la valeur dé
        """
        return f'Face du dé : {self.valeur}'
        
    @classmethod
    def nombre(cls):
        """
        affiche le nombre dé(s) instancié(s)
        """
        return cls.nb_des

if __name__=='__main__':
    De1=De('De1')
    assert isinstance(De1, De)
    k=De1.hasard()
    assert k<=6 and k>=1
