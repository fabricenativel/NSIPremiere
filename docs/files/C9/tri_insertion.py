from random import randint


def insere(liste,elt,indice):
    while indice>0 and liste[indice]<liste[indice-1]:
        liste[indice],liste[indice-1] = liste[indice-1],liste[indice]
        indice -= 1

# Tri par insertion
def tri_insertion(liste):
    for ind in range(len(liste)):
        # insere permet d'insérer au bon emplacement entre les indices 0 et ind
        insere(liste,liste[ind],ind)


ex_liste = [randint(1,100) for _ in range(50)]
tri_insertion(ex_liste)
print(ex_liste)