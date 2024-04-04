from sorting import *

def afficher_tableau(tableau):
    print("Tableau trié :", tableau)

def demander_tri():
    print("Choisissez un algorithme de tri :")
    print("1. Tri par sélection")
    print("2. Tri à bulles")
    print("3. Tri par insertion")
    print("4. Tri fusion")
    print("5. Tri rapide")
    print("6. Tri par tas")
    print("7. Tri à peigne")
    choix = int(input("Entrez votre choix : "))

    return choix

def main():
    tableau = [int(x) for x in input("Entrez les éléments du tableau séparés par des espaces : ").split()]
    choix = demander_tri()

    if choix == 1:
        tri_selection(tableau)
    elif choix == 2:
        tri_bulles(tableau)
    elif choix == 3:
        tri_insertion(tableau)
    elif choix == 4:
        tri_fusion(tableau)
    elif choix == 5:
        tableau = tri_rapide(tableau)
    elif choix == 6:
        tri_par_tas(tableau)
    elif choix == 7:
        tri_a_peigne(tableau)
    else:
        print("Choix invalide")

    afficher_tableau(tableau)

if __name__ == "__main__":
    main()
