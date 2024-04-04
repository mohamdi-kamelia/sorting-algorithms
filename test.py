import tkinter as tk
from colorsys import hsv_to_rgb
from math import sin, radians  # Importation de sin et radians depuis la bibliothèque math
import random

# Fonction pour générer toutes les couleurs possibles avec des teintes variées
def generate_colors(num_colors):
    colors = []
    for hue in range(0, 360, int(360/num_colors)):
        rgb = hsv_to_rgb(hue / 360, 1.0, 1.0)
        hex_color = "#{:02x}{:02x}{:02x}".format(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
        colors.extend([hex_color] * 10)  # Répéter chaque couleur 10 fois
    return colors

# Fonction pour afficher le cercle initial avec les couleurs générées
def display_initial_circle(colors):
    angle = 0
    angle_increment = 360 / len(colors)
    for color in colors:
        start_x = center_x + radius * sin(radians(angle))  # Utilisation de la fonction sin de math
        start_y = center_y - radius * sin(radians(angle))
        end_x = center_x + radius * sin(radians(angle + angle_increment))  # Utilisation de la fonction radians de math
        end_y = center_y - radius * sin(radians(angle + angle_increment))
        canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                          start=angle, extent=angle_increment, fill=color, outline=color)
        angle += angle_increment

# Fonction pour réorganiser les couleurs en fonction d'un algorithme de tri spécifié
def rearrange_colors(colors, algo_name):
    # Effectue le tri des couleurs en fonction du nom de l'algorithme
    if algo_name == "Tri à bulles":
        tri_bulle(colors)
    else:
        print("Tri non reconnu. Les couleurs ne seront pas réorganisées.")

# Fonction pour afficher le cercle réorganisé avec les couleurs triées
def display_rearranged_circle(colors):
    angle = 0
    angle_increment = 360 / len(colors)
    for color in colors:
        start_x = center_x + radius * sin(radians(angle))  # Utilisation de la fonction sin de math
        start_y = center_y - radius * sin(radians(angle))
        end_x = center_x + radius * sin(radians(angle + angle_increment))  # Utilisation de la fonction radians de math
        end_y = center_y - radius * sin(radians(angle + angle_increment))
        canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                          start=angle, extent=angle_increment, fill=color, outline=color)
        angle += angle_increment

# Fonction pour démarrer le tri et réorganiser les couleurs
def start_sorting():
    global colors
    algo_name = algorithm_selection.get()
    rearrange_colors(colors, algo_name)
    display_rearranged_circle(colors)

# Paramètres du cercle
center_x = 250
center_y = 250
radius = 200

# Création de la fenêtre principale
root = tk.Tk()
root.title("Tri de couleurs avec Tkinter")

# Création du canevas
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Génération de couleurs avec des teintes variées
colors = generate_colors(36)  # 36 couleurs différentes

# Affichage du cercle initial avec les couleurs générées
display_initial_circle(colors)

# Choix de l'algorithme de tri
algorithm_selection = tk.StringVar(root)
algorithm_selection.set("Tri à bulles")
algorithm_menu = tk.OptionMenu(root, algorithm_selection, "Tri à bulles")
algorithm_menu.pack()

# Bouton pour démarrer le tri
start_button = tk.Button(root, text="Démarrer le tri", command=start_sorting)
start_button.pack()

root.mainloop()
