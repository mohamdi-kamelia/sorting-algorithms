import random
import time

def tri_par_selection(liste):
    for i in range(len(liste)):
        min_index = i
        for j in range(i+1, len(liste)):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

def tri_a_bulles(liste):
    for i in range(len(liste)):
        for j in range(0, len(liste)-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

def tri_insertion(liste):
    for i in range(1, len(liste)):
        key = liste[i]
        j = i-1
        while j >= 0 and key < liste[j]:
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = key
    return liste

def tri_fusion(liste):
    if len(liste) > 1:
        mid = len(liste) // 2
        left = liste[:mid]
        right = liste[mid:]

        tri_fusion(left)
        tri_fusion(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                liste[k] = left[i]
                i += 1
            else:
                liste[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            liste[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            liste[k] = right[j]
            j += 1
            k += 1

    return liste

def tri_rapide(liste):
    if len(liste) <= 1:
        return liste
    else:
        pivot = liste.pop()

    elements_plus_petits = []
    elements_plus_grands = []

    for element in liste:
        if element <= pivot:
            elements_plus_petits.append(element)
        else:
            elements_plus_grands.append(element)

    return tri_rapide(elements_plus_petits) + [pivot] + tri_rapide(elements_plus_grands)

def tri_par_tas(liste):
    def tamiser(liste, n, i):
        plus_grand = i
        gauche = 2 * i + 1
        droite = 2 * i + 2

        if gauche < n and liste[i] < liste[gauche]:
            plus_grand = gauche

        if droite < n and liste[plus_grand] < liste[droite]:
            plus_grand = droite

        if plus_grand != i:
            liste[i], liste[plus_grand] = liste[plus_grand], liste[i]
            tamiser(liste, n, plus_grand)

    n = len(liste)

    for i in range(n, -1, -1):
        tamiser(liste, n, i)

    for i in range(n-1, 0, -1):
        liste[i], liste[0] = liste[0], liste[i]
        tamiser(liste, i, 0)

    return liste

def calculer_temps_execution(tri, liste):
    debut = time.time()
    tri(liste)
    fin = time.time()
    print(f"Temps d'exécution pour {tri.__name__}: {fin - debut} secondes")
    return fin - debut
