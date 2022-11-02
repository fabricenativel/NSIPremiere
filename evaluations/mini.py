def indice_minimum(liste):
    indice_minimum = 0
    for indice in range(len(liste)):
        if liste[indice]<liste[indice_minimum]:
            indice_minimum = indice
    return indice_minimum

print(indice_minimum([11,7,4,3,10]))