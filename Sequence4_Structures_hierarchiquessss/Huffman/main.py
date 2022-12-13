import bisect
import json
class ArbreHuffman():
    def __init__(self,lettre,nbocc,g=None,d=None):
        self.lettre=lettre
        self.nbocc=nbocc
        self.gauche=g
        self.droite=d
    def est_feuille(self)->bool:
        return not(self.gauche) and not(self.droite)
    def __lt__(self,other):
        return self.nbocc>other.nbocc
    
def parcours(arbre, chemin_en_cours,dico):
    if not arbre:
        return
    if arbre.est_feuille():
        dico[arbre.lettre]=chemin_en_cours
    else:
        parcours(arbre.gauche, chemin_en_cours + [0], dico)
        parcours(arbre.droite, chemin_en_cours + [1], dico)
        
def fusionne(gauche,droite):
    nbocc_total=gauche.nbocc+droite.nbocc
    return ArbreHuffman(None,nbocc_total,gauche,droite)

def compte_occurences(texte:str)->dict:
    occ=dict()
    for car in texte:
        if car not in occ:
            occ[f"{car}"]=0
        occ[f"{car}"]=occ[f"{car}"]+1
    return occ

def construit_liste_arbres(texte:str)->list:
    dic_occurences=compte_occurences(texte)
    liste_arbres=[]
    for lettre,occ in dic_occurences.items():
        liste_arbres.append(ArbreHuffman(lettre,occ))
    return liste_arbres

def codage_huffman(texte:str)->dict:
    liste_arbres=construit_liste_arbres(texte)
    liste_arbres.sort()
    while len(liste_arbres)>1:
        droite=liste_arbres.pop()
        gauche=liste_arbres.pop()
        new_arbre=fusionne(gauche, droite)
        bisect.insort(liste_arbres, new_arbre)
    arbre_huffman=liste_arbres.pop()
    dico={}
    parcours(arbre_huffman,[],dico)
    encode_message(dico,texte)
    return dico

def lire_fichier(texte) :
    with open(texte, 'r') as txt:
        lignes = txt.read()
        return lignes

def encode_message(dico,texte)->str:
    encoded=""
    for car in texte:
        for val in dico[car]:
            encoded=encoded+f"{val}"
    sauvegarde(encoded,dico)
    return encoded

def sauvegarde(encoded,dico):
    file=open("huffman.txt",mode="w")
    file.write(encoded)
    file.close()
    dic=open("decodage.txt",mode="w")
    dic.write(json.dumps(dico))
    dic.close()

def decrypte(textfile, codefile):
    decrypted,current=[],""
    with open(textfile) as txt:
        texte=txt.read()
    with open(codefile) as dic:
        dictionnaire = dic.read()
    dico = dictionnaire.replace("'", '"') 
    dico = json.loads(dico)
    reverse_code = dict(zip(["".join([str(y) for y in v]) for v in dico.values()], dico.keys()))
    for c in texte:
        current += c
        if current in reverse_code:
            decrypted.append(reverse_code[current])
            current = ""
    return "".join(decrypted)



if __name__=='__main__':
    texte=lire_fichier("txt.txt")
    dico=codage_huffman(texte)
    #print(dico)
    print(compte_occurences(texte))
    print(decrypte("huffman.txt","decodage.txt"))
    #print(compte_occurences(texte))
