import random
import time
import colorsys
import tkinter as tk
from math import sin, radians, cos, pi

#fonction pour le Tri par sélection
def tri_par_selection(liste):
    for i in range(len(liste)):
        index_min = i
        for j in range(i+1, len(liste)):
            if liste[j] < liste[index_min]:
                index_min = j
        liste[i], liste[index_min] = liste[index_min], liste[i]
    return liste

#fonction pour le tri a bulles
def tri_a_bulles(liste):
    for i in range(len(liste)):
        for j in range(0, len(liste)-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

#Tri par insertion : parcourt la liste
def tri_insertion(liste):
    for i in range(1, len(liste)):
        clé = liste[i]
        j = i-1
        while j >= 0 and clé < liste[j]:
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = clé
    return liste

#fonction pour le tri par fusion 
def tri_fusion(liste):
    if len(liste) > 1:
        milieu = len(liste) // 2
        gauche = liste[:milieu]
        droite = liste[milieu:]

        tri_fusion(gauche)
        tri_fusion(droite)

        i = j = k = 0

        while i < len(gauche) and j < len(droite):
            if gauche[i] < droite[j]:
                liste[k] = gauche[i]
                i += 1
            else:
                liste[k] = droite[j]
                j += 1
            k += 1

        while i < len(gauche):
            liste[k] = gauche[i]
            i += 1
            k += 1

        while j < len(droite):
            liste[k] = droite[j]
            j += 1
            k += 1

    return liste

#Fonction pour le tri rapide 
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

#fonction pour le tri par tas
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
#Fonction pour le tri peigne
def tri_peigne(liste):
    def trier_peigne(liste):
        intervale = len(liste)
        while intervale > 1:
            intervale = max(1, int(intervale / 1.25))
            for i in range(len(liste) - intervale):
                if liste[i] > liste[i + intervale]:
                    liste[i], liste[i + intervale] = liste[i + intervale], liste[i]
        return liste

    return trier_peigne(liste)

# Calcule et affiche le temps d'exécution d'un algorithme de tri sur une liste donnée.
def calculer_temps_execution(tri, liste):
    debut = time.time()
    tri(liste)
    fin = time.time()
    print(f"Temps d'exécution pour {tri.__name__}: {fin - debut} secondes")
    return fin - debut

#Génère une liste aléatoire de taille n.
def liste_aleatoire(n):
    liste = []
    for i in range(1, n+1):
        liste.append(i)
    random.shuffle(liste)
    return liste

class TriGraphique:
    def __init__(self, liste):
        self.liste = liste
        self.fenetre = tk.Tk()
        self.fenetre.configure(bg='black')  
        self.frame = tk.Frame(self.fenetre, bg='black')  
        self.frame.pack(expand=True, fill='both')  
        self.canvas = tk.Canvas(self.frame, width=700, height=600, bg='black')  # Crée un Canvas avec fond noir
        self.canvas.pack(expand=True, fill='both') 
        self.couleurs = self.generer_couleurs(self.liste)
        self.roue = self.creer_roue(self.canvas, self.couleurs)
        self.echanges = 0 
        self.comparaisons = 0  
        self.label_echanges = tk.Label(self.fenetre, text="Échanges: 0")  # Label pour afficher le nombre d'échanges
        self.label_echanges.place(x=560, y=80)
        self.label_comparaisons = tk.Label(self.fenetre, text="Comparaisons: 0")  # Label pour afficher le nombre de comparaisons
        self.label_comparaisons.place(x=560 , y= 40)
        self.label_temps_execution = tk.Label(self.fenetre, text="Temps d'exécution: 0 secondes")  # Label pour afficher le temps d'exécution
        self.label_temps_execution.place(x=250, y=40)
        
        self.creer_boutons()

    def generer_couleurs(self,liste):
        hsv = [(x/len(liste), 1, 1) for x in liste]
        rgb = [colorsys.hsv_to_rgb(*x) for x in hsv]
        return rgb

    def creer_roue(self, canvas, liste):
        width = 700  # Largeur du canevas
        height = 600  # Hauteur du canevas
        x_center = width / 2  # Coordonnée x du centre du canevas
        y_center = height / 2  # Coordonnée y du centre du canevas
        radius = 200  # Rayon du cercle

        for i in range(len(liste)):
            angle = radians(i / len(liste) * 360)
            x1 = x_center + radius * cos(angle)
            y1 = y_center + radius * sin(angle)
            x2 = x_center + radius * cos(angle + 2 * pi / len(liste))
            y2 = y_center + radius * sin(angle + 2 * pi / len(liste))
            canvas.create_polygon(x_center, y_center, x1, y1, x2, y2, fill=f"#{int(liste[i][0] * 255):02x}{int(liste[i][1] * 255):02x}{int(liste[i][2] * 255):02x}")

        return canvas

#Met à jour l'affichage graphique de la liste sur le canvas.
    def mise_a_jour(self, liste):
        self.canvas.delete("all")
        self.couleurs = self.generer_couleurs(liste)
        self.roue = self.creer_roue(self.canvas, self.couleurs)
        self.label_echanges.config(text="Échanges: {}".format(self.echanges))  # Met à jour le label d'échanges
        self.label_comparaisons.config(text="Comparaisons: {}".format(self.comparaisons))  # Met à jour le label de comparaisons
        self.fenetre.update()

#Implémente les tris  et met à jour l'affichage graphique à chaque étape du tri.
    def tri_par_selection(self):
        for i in range(len(self.liste)):
            index_min = i
            for j in range(i+1, len(self.liste)):
                if self.liste[j] < self.liste[index_min]:
                    index_min= j
                self.comparaisons += 1  # Incrémentation du compteur de comparaisons
            self.liste[i], self.liste[index_min] = self.liste[index_min], self.liste[i]
            self.echanges += 1  # Incrémentation du compteur d'échanges
            self.mise_a_jour(self.liste)
            self.fenetre.update()
        return self.liste

    
    def tri_a_bulles(self):
      
        for i in range(len(self.liste)):
            for j in range(0, len(self.liste)-i-1):
                if self.liste[j] > self.liste[j+1]:
                    self.liste[j], self.liste[j+1] = self.liste[j+1], self.liste[j]
                    self.echanges += 1
                self.comparaisons += 1
                self.mise_a_jour(self.liste)
                self.fenetre.update()
        return self.liste
    
    def tri_insertion(self):
        for i in range(1, len(self.liste)):
            clé = self.liste[i]
            j = i-1
            while j >= 0 and clé < self.liste[j]:
                self.liste[j+1] = self.liste[j]
                j -= 1
                self.comparaisons += 1
                self.echanges += 1
                self.mise_a_jour(self.liste)
                self.fenetre.update()
            self.liste[j+1] = clé
        return self.liste

    def tri_fusion(self, liste, index_debut=0, index_fin=None):
        
        if index_fin is None:
            index_fin = len(liste)

        if index_fin - index_debut > 1:
            milieu = (index_debut + index_fin) // 2

            self.tri_fusion(liste, index_debut, milieu)
            self.tri_fusion(liste, milieu, index_fin)


            gauche = liste[index_debut:milieu]
            droite = liste[milieu:index_fin]

            i = j = k = 0

            while i < len(gauche) and j < len(droite):
                self.comparaisons += 1
                if gauche[i] < droite[j]:
                    liste[index_debut + k] = gauche[i]
                    i += 1
                else:
                    liste[index_debut + k] = droite[j]
                    j += 1
                k += 1

            while i < len(gauche):
                self.echanges +=1
                liste[index_debut + k] = gauche[i]
                i += 1
                k += 1

            while j < len(droite):
                self.echanges +=1
                liste[index_debut + k] = droite[j]
                j += 1
                k += 1

        self.mise_a_jour(liste)
        self.fenetre.update()

        return liste
    
    def tri_rapide(self, liste, index_debut=0, index_fin=None):
        if index_fin is None:
            index_fin = len(liste) - 1

        if index_debut < index_fin:
            pivot = liste[index_fin]
            pivot_index = index_debut - 1

            for i in range(index_debut, index_fin):
                self.comparaisons += 1
                if liste[i] <= pivot:
                    pivot_index += 1
                    liste[pivot_index], liste[i] = liste[i], liste[pivot_index]
                    self.echanges += 1
                    self.mise_a_jour(liste)
                    self.fenetre.update()

            pivot_index += 1
            liste[pivot_index], liste[index_fin] = liste[index_fin], liste[pivot_index]

            self.tri_rapide(liste, index_debut, pivot_index - 1)
            self.tri_rapide(liste, pivot_index + 1, index_fin)

        return liste

    def tri_par_tas(self):

        def tamiser(liste, n, i):
            plus_grand = i
            gauche = 2 * i + 1
            droite = 2 * i + 2
            self.comparaisons += 1
            if gauche < n and liste[i] < liste[gauche]:
                plus_grand = gauche

            if droite < n and liste[plus_grand] < liste[droite]:
                plus_grand = droite

            if plus_grand != i:
                liste[i], liste[plus_grand] = liste[plus_grand], liste[i]
                tamiser(liste, n, plus_grand)
                self.echanges += 1
                self.mise_a_jour(self.liste)
                self.fenetre.update()

        n = len(self.liste)

        for i in range(n, -1, -1):
            tamiser(self.liste, n, i)

        for i in range(n-1, 0, -1):
            self.liste[i], self.liste[0] = self.liste[0], self.liste[i]
            tamiser(self.liste, i, 0)
            self.echanges += 1
            self.mise_a_jour(self.liste)
            self.fenetre.update()

        return self.liste

    def tri_peigne(self):
      
        def trier_peigne(liste):
            interval = len(liste)
            while interval > 1:
                interval = max(1, int(interval / 1.25))
                for i in range(len(liste) - interval):
                    self.comparaisons += 1
                    if liste[i] > liste[i + interval]:
                        liste[i], liste[i + interval] = liste[i + interval], liste[i]
                        self.echanges += 1
                        self.mise_a_jour(self.liste)
                        self.fenetre.update()
            return liste
        
        return trier_peigne(self.liste)
    
#Crée les boutons pour lancer les différents algorithmes de tri.    
    def creer_boutons(self):
        bouton_selection = tk.Button(self.fenetre, text="Tri par sélection", command=self.cliquer_selection)
        bouton_selection.place(x=10, y=0)

        bouton_bulles = tk.Button(self.fenetre, text="Tri à bulles", command=self.cliquer_bulles)
        bouton_bulles.place(x=10, y=40)

        bouton_insertion = tk.Button(self.fenetre, text="Tri par insertion", command=self.cliquer_insertion)
        bouton_insertion.place(x=10, y=80)

        bouton_fusion = tk.Button(self.fenetre, text="Tri fusion", command=lambda: self.cliquer_fusion(self.liste))
        bouton_fusion.place(x=10, y=120)

        bouton_rapide = tk.Button(self.fenetre, text="Tri rapide", command=lambda: self.cliquer_rapide(self.liste))
        bouton_rapide.place(x=10, y=160)

        bouton_tas = tk.Button(self.fenetre, text="Tri par tas", command=self.cliquer_tas)
        bouton_tas.place(x=10, y=200)

        bouton_peigne = tk.Button(self.fenetre, text="Tri peigne", command=self.cliquer_peigne)
        bouton_peigne.place(x=10, y=240)

        bouton_melanger = tk.Button(self.fenetre, width=20,height=5,bg="red", text="Mélanger", command=self.melanger)
        bouton_melanger.place(x=280, y=520)

#Événements déclenchés lors du clic sur les boutons des Tris.
    def cliquer_selection(self):
        self.comparaisons = 0
        self.echanges = 0
        self.melanger()
        debut = time.time()
        self.tri_par_selection()
        fin = time.time()
        temps_execution = fin - debut
        self.label_temps_execution.config(text="Temps d'exécution: {:.5f} secondes".format(temps_execution))


    def cliquer_bulles(self):
        self.comparaisons = 0
        self.echanges = 0
        self.melanger()
        debut = time.time()
        self.tri_a_bulles()
        fin = time.time()
        temps_execution = fin - debut
        self.label_temps_execution.config(text="Temps d'exécution: {:.5f} secondes".format(temps_execution))

    
    def cliquer_insertion(self):
        self.comparaisons = 0
        self.echanges = 0
        self.melanger()
        debut = time.time()
        self.tri_insertion()
        fin = time.time()
        temps_execution = fin - debut
        self.label_temps_execution.config(text="Temps d'exécution: {:.5f} secondes".format(temps_execution))

    
    def cliquer_fusion(self, liste):
        self.comparaisons = 0
        self.echanges = 0
        self.melanger()
        debut = time.time()
        self.tri_fusion(liste)
        fin = time.time()
        temps_execution = fin - debut
        self.label_temps_execution.config(text="Temps d'exécution: {:.5f} secondes".format(temps_execution))


    def cliquer_rapide(self, liste):
        self.comparaisons = 0
        self.echanges = 0
        self.melanger()
        debut = time.time()
        self.tri_rapide(liste)
        fin = time.time()
        temps_execution = fin - debut
        self.label_temps_execution.config(text="Temps d'exécution: {:.5f} secondes".format(temps_execution))


    def cliquer_tas(self):
        self.comparaisons = 0
        self.echanges = 0
        self.melanger()
        debut = time.time()
        self.tri_par_tas()
        fin = time.time()
        temps_execution = fin - debut
        self.label_temps_execution.config(text="Temps d'exécution: {:.5f} secondes".format(temps_execution))


    def cliquer_peigne(self):
        self.comparaisons = 0
        self.echanges = 0
        self.melanger()
        debut = time.time()
        self.tri_peigne()
        fin = time.time()
        temps_execution = fin - debut
        self.label_temps_execution.config(text="Temps d'exécution: {:.5f} secondes".format(temps_execution))

# Mélange la liste et met à jour l'affichage graphique.
    def melanger(self):
        self.comparaisons = 0
        self.echanges = 0
        self.label_temps_execution.config(text="Temps d'exécution: 0 secondes") 
        random.shuffle(self.liste)
        self.mise_a_jour(self.liste)
        self.fenetre.update()

# Lance l'interface graphique.
    def run(self):
        self.fenetre.mainloop()


