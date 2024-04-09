import pygame
import random
import math
import time

# Définition des constantes
LARGEUR = 800
HAUTEUR = 600
TAILLE = 180
RETARD = 500  # 5 secondes de retard
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)

# Initialisation de pygame
pygame.init()
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
horloge = pygame.time.Clock()

# Initialisation de la liste et des paramètres de tri
liste = []
etapes = []
echanges = 0
comparaisons = 0
en_cours = False
melange = False

# Initialisation de la liste avec des valeurs triées
def initialiser():
    global liste
    liste = [i for i in range(TAILLE)]

# Réinitialisation de l'animation et mélange de la liste
def reinitialiser():
    global en_cours, melange, echanges, comparaisons
    en_cours = False
    echanges = 0
    comparaisons = 0
    etapes.clear()
    if not melange:
        initialiser()
        random.shuffle(liste)
    melange = True

# Affichage de la liste sous forme graphique
def dessiner_rosette(x, y, r):
    arc = 2 * math.pi / TAILLE
    nb_cotes = 50  # Nombre de côtés des polygones
    for i in range(TAILLE):
        angle_depart = i * arc
        angle_fin = (i + 1) * arc
        couleur = pygame.Color("black")
        if liste[i] != -1:
            teinte = int(liste[i] * 360 / TAILLE)
            couleur.hsla = (teinte, 100, 50, 100)
        # Dessiner un polygone dans chaque secteur du cercle
        for j in range(nb_cotes):
            angle1 = angle_depart + (j / nb_cotes) * arc
            angle2 = angle_depart + ((j + 1) / nb_cotes) * arc
            px1 = x + r * math.cos(angle1)
            py1 = y + r * math.sin(angle1)
            px2 = x + r * math.cos(angle2)
            py2 = y + r * math.sin(angle2)
            pygame.draw.polygon(ecran, couleur, [(int(x), int(y)), (int(px1), int(py1)), (int(px2), int(py2))])

# Fonction de fusion pour le tri fusion
def fusion(arr, gauche, milieu, droite):
    global echanges, comparaisons
    n1 = milieu - gauche + 1
    n2 = droite - milieu

    gauche_arr = [arr[gauche + i] for i in range(n1)]
    droite_arr = [arr[milieu + 1 + i] for i in range(n2)]

    i = j = 0
    k = gauche

    while i < n1 and j < n2:
        comparaisons += 1
        if gauche_arr[i] <= droite_arr[j]:
            arr[k] = gauche_arr[i]
            i += 1
        else:
            arr[k] = droite_arr[j]
            j += 1
            echanges += 1
        k += 1

    while i < n1:
        arr[k] = gauche_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = droite_arr[j]
        j += 1
        k += 1

# Fonction de tri fusion
def tri_fusion(arr, gauche, droite):
    if gauche < droite:
        milieu = (gauche + droite) // 2

        tri_fusion(arr, gauche, milieu)
        tri_fusion(arr, milieu + 1, droite)

        fusion(arr, gauche, milieu, droite)

        etapes.append(arr.copy())  # Enregistre chaque étape du tri

# Création du bouton
def dessiner_bouton():
    pygame.draw.rect(ecran, VERT, (LARGEUR // 2 - 50, HAUTEUR - 100, 100, 50))
    police = pygame.font.Font(None, 36)
    texte = police.render("Trier", True, BLANC)
    rect_texte = texte.get_rect(center=(LARGEUR // 2, HAUTEUR - 75))
    ecran.blit(texte, rect_texte)

# Vérification si le clic est sur le bouton
def est_clic_sur_bouton(pos):
    rect_bouton = pygame.Rect(LARGEUR // 2 - 50, HAUTEUR - 100, 100, 50)
    return rect_bouton.collidepoint(pos)
# Ajoute cette fonction pour dessiner les informations à l'écran
def dessiner_infos():
    police = pygame.font.Font(None, 24)
    texte_echanges = police.render("Échanges: {}".format(echanges), True, BLANC)
    texte_comparaisons = police.render("Comparaisons: {}".format(comparaisons), True, BLANC)
    ecran.blit(texte_echanges, (10, 10))
    ecran.blit(texte_comparaisons, (10, 30))

def mise_a_jour_infos():
    pygame.display.flip()  # Met à jour l'affichage pour chaque étape
    dessiner_infos()

# Animation des étapes de tri
def afficher_tri(type_tri):
    global en_cours
    i = 0
    while en_cours and i < len(etapes):
        idx = i
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        liste[:] = etapes[idx]
        i += 1
        mise_a_jour_infos()  # Appelle la fonction pour mettre à jour les informations de tri
        pygame.display.flip()  # Met à jour l'affichage pour chaque étape
        time.sleep(0.5)  # Attendre 0.5 secondes entre chaque étape du tri
    # Une fois que toutes les étapes ont été chargées, déclenche le tri spécifié
    if type_tri == 'Tri Fusion':
        tri_fusion(liste, 0, len(liste) - 1)
# Boucle principale
def principal():
    global en_cours, echanges, comparaisons
    initialiser()
    reinitialiser()
    types_tri = ['Tri Fusion']
    tri_actuel = 'Tri Fusion'
    while True:
        ecran.fill(NOIR)
        dessiner_rosette(LARGEUR / 2, HAUTEUR / 2, min(LARGEUR, HAUTEUR) / 3)
        dessiner_bouton()
        dessiner_infos() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and est_clic_sur_bouton(event.pos):
                    if not en_cours:
                        en_cours = True
                        afficher_tri(tri_actuel) 
        if len(etapes) == TAILLE - 1 and not en_cours:
            break
        pygame.display.flip()
        horloge.tick(120)


if __name__ == "__main__":
    principal()
