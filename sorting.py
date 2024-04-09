import random
import time
import colorsys
import tkinter as tk
from math import sin, radians, cos, pi

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


def generer_couleurs(liste):
    hsv = [(x/len(liste), 1, 1) for x in liste]
    rgb = [colorsys.hsv_to_rgb(*x) for x in hsv]
    return rgb

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
        self.canvas = tk.Canvas(self.fenetre, width=800, height=800)
        self.canvas.pack()

        self.couleurs = generer_couleurs(self.liste)
        self.roue = self.creer_roue(self.canvas, self.couleurs)    

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

    def update(self, liste):
        self.canvas.delete("all")
        self.couleurs = generer_couleurs(liste)
        self.roue = self.creer_roue(self.canvas, self.couleurs)
        self.fenetre.update()

    def tri_par_selection(self):
        for i in range(len(self.liste)):
            min_index = i
            for j in range(i+1, len(self.liste)):
                if self.liste[j] < self.liste[min_index]:
                    min_index = j
            self.liste[i], self.liste[min_index] = self.liste[min_index], self.liste[i]
            self.update(self.liste)
            self.fenetre.update()
        return self.liste
    
    def tri_a_bulles(self):
        for i in range(len(self.liste)):
            for j in range(0, len(self.liste)-i-1):
                if self.liste[j] > self.liste[j+1]:
                    self.liste[j], self.liste[j+1] = self.liste[j+1], self.liste[j]
                    self.update(self.liste)
                    self.fenetre.update()
        return self.liste
    
    def tri_insertion(self):
        for i in range(1, len(self.liste)):
            key = self.liste[i]
            j = i-1
            while j >= 0 and key < self.liste[j]:
                self.liste[j+1] = self.liste[j]
                j -= 1
            self.liste[j+1] = key
            self.update(self.liste)
            self.fenetre.update()
        return self.liste
    
    def tri_fusion(self, liste):
        if len(liste) > 1:
            mid = len(liste) // 2
            left = liste[:mid]
            right = liste[mid:]

            self.tri_fusion(left)
            self.tri_fusion(right)

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

            self.update(liste)
            self.fenetre.update()

        return liste


    def run(self):
        self.tri_fusion(self.liste)
        self.update(self.liste)
        self.fenetre.mainloop()


liste = liste_aleatoire(1000)
roue = TriGraphique(liste)
roue.run()