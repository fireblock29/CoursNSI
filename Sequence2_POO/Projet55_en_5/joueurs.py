from des import *
class Joueur:
    
    def __init__(self,prenom:str=None, score:int=0, nb_coups:int=5):
        """
        Constructeur
        Initialisation des 3 attributs de classe :
            prenom (chaine de caractères)
            score (nombre entier ; par défaut 0)
            nb_coups (nombre entier ; par défaut 0)
        """
        self.prenom=prenom
        self.score=score
        self.nb_coups=nb_coups
        
    def lance(self,de1, de2, de3)-> tuple:
        """
        Méthode lançant les 3 dés passés en paramètres
        Nécessite l'import de la classe "des"
        Retourne un tuple de format :
            valeur du dé 1, valeur du dé 2, valeur du dé 3, prénom, score, nombre de coups
        """
        val1, val2, val3=de1.hasard(), de2.hasard(), de3.hasard()
        self.score += de1.valeur+de2.valeur+de3.valeur
        self.de1, self.de2, self.de3 = de1, de2, de3
        self.nb_coups -= 1 #Décrémentation du nombre de coups
        return (de1.valeur, de2.valeur, de3.valeur, self.prenom, self.score, self.nb_coups)

    def __repr__(self)-> str:
        """
        Méthode d'affichage des caractéristiques du dé demandé (associé à self)
        """
        return f'Valeur du dé D1 : {self.de1}, Valeur du dé D2 : {self.de2}, Valeur du dé D3 : {self.de3}'


#Programme principal
if __name__ == '__main__':
    Perdant=Joueur("Tim")
    de1=De("D1")
    de2=De("D2")
    de3=De("D3")
    assert isinstance(de1, De)
    k=Perdant.lance(de1, de2, de3)
    assert Perdant.prenom=="Tim"
