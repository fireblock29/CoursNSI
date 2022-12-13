import requests

def requete(num):
    return requests.get(f'https://geo.api.gouv.fr/departements/{num}/communes').json()

def dpt(num):
    response=requete(num)
    return [elt["nom"] for elt in response]

def commune_max(num):
    response=requete(num)
    p={elt["nom"]:elt["population"] for elt in response}
    k=maxi(p.values())
    return get_key(k,p),k


def commune_min(num):
    response=requete(num)
    p={elt["nom"]:elt["population"] for elt in response}
    k=mini(p.values())
    return get_key(k,p),k

def tot_hab(num):
    response=requete(num)
    return somme([elt["population"] for elt in response])


def get_key(val,p):
        for key, value in p.items():
             if val == value: 
                return key
        return "La clé n'existe pas"
    
def maxi(liste):
    maxi=0
    for elt in liste:
        if elt>maxi:
            maxi=elt
    return maxi

def mini(liste):
    mini=float("inf")
    for elt in liste:
        if elt<mini:
            mini=elt
    return mini

def somme(liste):
    k=0
    for elt in liste:
        k+=elt
    return k
    
    
if __name__=='__main__':
    #dpt("67")
    print(commune_max("29"))
    print(commune_min("29"))
    print(tot_hab("29"))
