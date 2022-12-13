def karatsuba(x:int, y:int)->int:
    """
    Implémente l'algorithme de Karatsuba
    Prend en arguments, 2 entiers à multiplier, et
    renvoie le produit des ces deux entiers
    >>> karatsuba(1237,2587)
    3200119
    >>> karatsuba(278141237,2545887)
    708116159442219
    """
    assert type(x)==int and type(y)==int,'Les nombres doivent être des entiers'
    
    # Cas de terminaison
    if x < 10 and y < 10:
        return x * y

    #n est déjà divisé par 2
    n = max(len(str(abs(x))), len(str(abs(y))))//2 

    # divise en 2 parties
    a = x//(10**n)
    b = x%(10**n)
    # divise en 2 parties
    c = y//(10**n)
    d = y%(10**n)

    s1 = karatsuba(a,c)
    s2 = karatsuba(b,d)
    s3 = karatsuba(a-b,c-d)
    s4 = s1 + s2 - s3
   
    return s1*10**(2*n)+(s4*10**n)+s2

#Programme principal
if __name__=='__main__':
    from doctest import testmod
    testmod()
    assert karatsuba(14570000,895567)==14570000*895567
    print('résultat: ', karatsuba(11, 201))
    print(11 * 201)
