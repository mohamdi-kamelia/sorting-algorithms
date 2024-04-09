def InsertionSort(lst):
# l'algorithme de tri par insertion en parcourant la liste, en comparant chaque élément avec les éléments précédents
    for step in range(1, len(lst)):
        key = lst[step]
        i = step - 1
        while (i >= 0) and (key < lst[i]):
            lst[i + 1] = lst[i]
            i = i - 1
        lst[i + 1] = key

# Demander à l'utilisateur de saisir une liste de nombres
lst_str = input("Entrez une liste de nombres séparés par des virgules : ")
# Convertir la chaîne d'entrée en une liste de nombres
lst = [int(x) for x in lst_str.split(',')]

# Afficher la liste non triée
print("Liste non triée :")
print(lst)

# Trier la liste
InsertionSort(lst)

# Afficher la liste triée
print("Liste triée :")
print(lst)



"""
def tri_selection(tableau):
    pass
def tri_bulles(tableau):
    pass
def tri_fusion(tableau):
    pass
def tri_par_tas(tableau):
    pass
def tri_a_peigne(tableau):
    pass
def tri_insertion(tableau):
    pass
def tri_rapide(tableau):
    pass"""