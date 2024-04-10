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

def tri_peigne(liste):
    def trier_peigne(liste):
        interval = len(liste)
        while interval > 1:
            interval = max(1, int(interval / 1.25))
            for i in range(len(liste) - interval):
                if liste[i] > liste[i + interval]:
                    liste[i], liste[i + interval] = liste[i + interval], liste[i]
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
        
        self.create_buttons()


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

    def update(self, liste):
        self.canvas.delete("all")
        self.couleurs = self.generer_couleurs(liste)
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
    
    def tri_fusion(self, liste, start_index=0, end_index=None):
        if end_index is None:
            end_index = len(liste)

        if end_index - start_index > 1:
            mid = (start_index + end_index) // 2

            self.tri_fusion(liste, start_index, mid)
            self.tri_fusion(liste, mid, end_index)

            # Merge the sublists
            left = liste[start_index:mid]
            right = liste[mid:end_index]

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    liste[start_index + k] = left[i]
                    i += 1
                else:
                    liste[start_index + k] = right[j]
                    j += 1
                k += 1

            # Fill in remaining elements from left sublist
            while i < len(left):
                liste[start_index + k] = left[i]
                i += 1
                k += 1

            # Fill in remaining elements from right sublist
            while j < len(right):
                liste[start_index + k] = right[j]
                j += 1
                k += 1

        # Update the visualization of the entire list after each merge operation
        self.update(liste)
        self.fenetre.update()

        return liste
    
    def tri_rapide(self, liste, start_index=0, end_index=None):
        if end_index is None:
            end_index = len(liste) - 1

        if start_index < end_index:
            pivot = liste[end_index]
            pivot_index = start_index - 1

            for i in range(start_index, end_index):
                if liste[i] <= pivot:
                    pivot_index += 1
                    liste[pivot_index], liste[i] = liste[i], liste[pivot_index]
                    self.update(liste)
                    self.fenetre.update()

            pivot_index += 1
            liste[pivot_index], liste[end_index] = liste[end_index], liste[pivot_index]

            # Recursively sort the elements before and after the pivot
            self.tri_rapide(liste, start_index, pivot_index - 1)
            self.tri_rapide(liste, pivot_index + 1, end_index)

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
            self.update(self.liste)
            self.fenetre.update()

        for i in range(n-1, 0, -1):
            self.liste[i], self.liste[0] = self.liste[0], self.liste[i]
            tamiser(self.liste, i, 0)
            self.update(self.liste)
            self.fenetre.update()

        return self.liste
    
    def tri_peigne(self):
        def trier_peigne(liste):
            interval = len(liste)
            while interval > 1:
                interval = max(1, int(interval / 1.25))
                for i in range(len(liste) - interval):
                    if liste[i] > liste[i + interval]:
                        liste[i], liste[i + interval] = liste[i + interval], liste[i]
                        self.update(liste)
                        self.fenetre.update()
            return liste

        return trier_peigne(self.liste)
    
    
    def create_buttons(self):
        selection_button = tk.Button(self.fenetre, text="Tri par sélection", command=self.tri_par_selection)
        selection_button.pack()

        bubble_button = tk.Button(self.fenetre, text="Tri à bulles", command=self.tri_a_bulles)
        bubble_button.pack()

        insertion_button = tk.Button(self.fenetre, text="Tri par insertion", command=self.tri_insertion)
        insertion_button.pack()

        merge_button = tk.Button(self.fenetre, text="Tri fusion", command=lambda: self.tri_fusion(self.liste))
        merge_button.pack()

        quick_button = tk.Button(self.fenetre, text="Tri rapide", command=lambda: self.tri_rapide(self.liste))
        quick_button.pack()

        heap_button = tk.Button(self.fenetre, text="Tri par tas", command=self.tri_par_tas)
        heap_button.pack()

        comb_button = tk.Button(self.fenetre, text="Tri peigne", command=self.tri_peigne)
        comb_button.pack()

        shuffle_button = tk.Button(self.fenetre, width=20,height=5,bg="red", text="Mélanger", command=self.shuffle)
        shuffle_button.place(x=340, y=80)

    def shuffle(self):
        random.shuffle(self.liste)
        self.update(self.liste)
        self.fenetre.update()


    def run(self):
        self.fenetre.mainloop()


