import random
import time
import colorsys
import tkinter as tk
from math import sin, radians, cos, pi

def tri_par_selection(liste):
    for i in range(len(liste)):
        index_min = i
        for j in range(i+1, len(liste)):
            if liste[j] < liste[index_min]:
                index_min = j
        liste[i], liste[index_min] = liste[index_min], liste[i]
    return liste

def tri_a_bulles(liste):
    for i in range(len(liste)):
        for j in range(0, len(liste)-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

def tri_insertion(liste):
    for i in range(1, len(liste)):
        clé = liste[i]
        j = i-1
        while j >= 0 and clé < liste[j]:
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = clé
    return liste

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

def calculer_temps_execution(tri, liste):
    debut = time.time()
    tri(liste)
    fin = time.time()
    print(f"Temps d'exécution pour {tri.__name__}: {fin - debut} secondes")
    return fin - debut


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
        self.canvas = tk.Canvas(self.fenetre, width=800, height=700)
        self.canvas.pack()

        self.couleurs = self.generer_couleurs(self.liste)
        self.roue = self.creer_roue(self.canvas, self.couleurs)
        
        self.creer_boutons()


    def generer_couleurs(self,liste):
        hsv = [(x/len(liste), 1, 1) for x in liste]
        rgb = [colorsys.hsv_to_rgb(*x) for x in hsv]
        return rgb

    def creer_roue(self, canvas, liste):
        x = 400
        y = 400
        r = 200
        for i in range(len(liste)):
            angle = radians(i/len(liste) * 360)
            x1 = x + r * cos(angle)
            y1 = y + r * sin(angle)
            x2 = x + r * cos(angle + 2 * pi / len(liste))
            y2 = y + r * sin(angle + 2 * pi / len(liste))
            canvas.create_polygon(x, y, x1, y1, x2, y2, fill=f"#{int(liste[i][0]*255):02x}{int(liste[i][1]*255):02x}{int(liste[i][2]*255):02x}")

        return canvas

    def mise_a_jour(self, liste):
        self.canvas.delete("all")
        self.couleurs = self.generer_couleurs(liste)
        self.roue = self.creer_roue(self.canvas, self.couleurs)
        self.fenetre.update()

    def tri_par_selection(self):
        for i in range(len(self.liste)):
            index_min = i
            for j in range(i+1, len(self.liste)):
                if self.liste[j] < self.liste[index_min]:
                    index_min = j
            self.liste[i], self.liste[index_min] = self.liste[index_min], self.liste[i]
            self.mise_a_jour(self.liste)
            self.fenetre.update()
        return self.liste
    
    def tri_a_bulles(self):
        for i in range(len(self.liste)):
            for j in range(0, len(self.liste)-i-1):
                if self.liste[j] > self.liste[j+1]:
                    self.liste[j], self.liste[j+1] = self.liste[j+1], self.liste[j]
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
            self.liste[j+1] = clé
            self.mise_a_jour(self.liste)
            self.fenetre.update()
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
                if gauche[i] < droite[j]:
                    liste[index_debut + k] = gauche[i]
                    i += 1
                else:
                    liste[index_debut + k] = droite[j]
                    j += 1
                k += 1

            while i < len(gauche):
                liste[index_debut + k] = gauche[i]
                i += 1
                k += 1

            while j < len(droite):
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
                if liste[i] <= pivot:
                    pivot_index += 1
                    liste[pivot_index], liste[i] = liste[i], liste[pivot_index]
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

            if gauche < n and liste[i] < liste[gauche]:
                plus_grand = gauche

            if droite < n and liste[plus_grand] < liste[droite]:
                plus_grand = droite

            if plus_grand != i:
                liste[i], liste[plus_grand] = liste[plus_grand], liste[i]
                tamiser(liste, n, plus_grand)

        n = len(self.liste)

        for i in range(n, -1, -1):
            tamiser(self.liste, n, i)
            self.mise_a_jour(self.liste)
            self.fenetre.update()

        for i in range(n-1, 0, -1):
            self.liste[i], self.liste[0] = self.liste[0], self.liste[i]
            tamiser(self.liste, i, 0)
            self.mise_a_jour(self.liste)
            self.fenetre.update()

        return self.liste
    
    def tri_peigne(self):
        def trier_peigne(liste):
            intervale = len(liste)
            while intervale > 1:
                intervale = max(1, int(intervale / 1.25))
                for i in range(len(liste) - intervale):
                    if liste[i] > liste[i + intervale]:
                        liste[i], liste[i + intervale] = liste[i + intervale], liste[i]
                        self.mise_a_jour(liste)
                        self.fenetre.update()
            return liste

        return trier_peigne(self.liste)
    
    
    def creer_boutons(self):
        bouton_selection = tk.Button(self.fenetre, text="Tri par sélection", command=self.cliquer_selection)
        bouton_selection.place(x=10, y=0)

        bouton_bulles = tk.Button(self.fenetre, text="Tri à bulles", command=self.cliquer_bulles)
        bouton_bulles.place(x=10, y=40)

        bouton_insertion = tk.Button(self.fenetre, text="Tri par insertion", command=self.cliquer_insertion)
        bouton_insertion.place(x=10, y=80)

        bouton_fusion = tk.Button(self.fenetre, text="Tri fusion", command=lambda: self.cliquer_fusion(self.liste.copy()))
        bouton_fusion.place(x=10, y=120)

        bouton_rapide = tk.Button(self.fenetre, text="Tri rapide", command=lambda: self.cliquer_rapide(self.liste.copy()))
        bouton_rapide.place(x=10, y=160)

        bouton_tas = tk.Button(self.fenetre, text="Tri par tas", command=self.cliquer_tas)
        bouton_tas.place(x=10, y=200)

        bouton_peigne = tk.Button(self.fenetre, text="Tri peigne", command=self.cliquer_peigne)
        bouton_peigne.place(x=10, y=240)

        bouton_melanger = tk.Button(self.fenetre, width=20,height=5,bg="red", text="Mélanger", command=self.melanger)
        bouton_melanger.place(x=340, y=80)

    def cliquer_selection(self):
        self.melanger()
        self.tri_par_selection()

    def cliquer_bulles(self):
        self.melanger()
        self.tri_a_bulles()
    
    def cliquer_insertion(self):
        self.melanger()
        self.tri_insertion()
    
    def cliquer_fusion(self, liste):
        self.melanger()
        self.tri_fusion(liste)

    def cliquer_rapide(self, liste):
        self.melanger()
        self.tri_rapide(liste)

    def cliquer_tas(self):
        self.melanger()
        self.tri_par_tas()

    def cliquer_peigne(self):
        self.melanger()
        self.tri_peigne()

    def melanger(self):
        random.shuffle(self.liste)
        self.mise_a_jour(self.liste)
        self.fenetre.update()


    def run(self):
        self.fenetre.mainloop()


