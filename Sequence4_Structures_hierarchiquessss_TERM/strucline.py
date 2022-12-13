class File():
    def __init__(self):
        '''
        Constructeur permettant la création d'une pile vide
        '''
        self.file=[]

    def est_vide(self) -> bool:
        '''
        Méthode permettant de tester si la pile est vide
        et renvoie True si la pile est vide, False sinon
        '''
        return len(self.file)==0

    def enfiler(self, donnee):
        '''
        Méthode permettant d'empiler "donnee" au sommet de la pile
        argument donnee : donnée à empiler
        '''
        self.file.append(donnee)

    def defiler(self):
        '''
        Méthode permettant de dépiler l'élément au sommet de la pile
        et renvoie la donnée au sommet de la pile
        '''
        assert not(self.est_vide())
        """if self.est_vide():
            return Opération Impossible"""
        return self.file.pop(0)
        
    def __repr__(self):
        return f'{self.file}'
        """for elt in self.file[0:-1]:
            print(f"|{elt}|", end="-->")
        print(f'|{self.file[-1]}|')
        return ""
        """
    
if __name__=="__main__":
    JeanFile=File()
    #JeanPile.depiler()
    print(JeanFile.est_vide())
    JeanFile.enfiler(55)
    JeanFile.enfiler(98)
    JeanFile.enfiler(1500)
    JeanFile.enfiler(985)
    print(JeanFile)
    JeanFile.defiler()
    print(JeanFile)  



class Pile():
    def __init__(self):
        '''
        Constructeur permettant la création d'une pile vide
        '''
        self.pile=[]

    def est_vide(self) -> bool:
        '''
        Méthode permettant de tester si la pile est vide
        et renvoie True si la pile est vide, False sinon
        '''
        return len(self.pile)==0

    def empiler(self, donnee):
        '''
        Méthode permettant d'empiler "donnee" au sommet de la pile
        argument donnee : donnée à empiler
        '''
        self.pile.append(donnee)

    def depiler(self):
        '''
        Méthode permettant de dépiler l'élément au sommet de la pile
        et renvoie la donnée au sommet de la pile
        '''
        assert not(self.est_vide())
        """if self.est_vide():
            return Opération Impossible"""
        elt=self.pile[-1]
        #self.pile.pop(-1)
        return self.pile.pop()
        
    def __repr__(self):
        print("======")
        for elt in self.pile:
            if elt<100:
                print(f"| {elt} |")
            elif elt>999:
                print(f"|{elt}|")
            else:
                print(f"|{elt} |")
            print("======")
        return ""
    
if __name__=="__main__":
    JeanPile=Pile()
    #JeanPile.depiler()
    print(JeanPile.est_vide())
    JeanPile.empiler(55)
    JeanPile.empiler(98)
    JeanPile.empiler(1500)
    JeanPile.empiler(985)
    print(JeanPile)
    JeanPile.depiler()
    print(JeanPile)