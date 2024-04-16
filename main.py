from sorting import *
import threading
import random

# Générer une liste de nombres aléatoire
liste_nombres = []
for i in range(1, 1001):
    liste_nombres.append(i)
random.shuffle(liste_nombres)

# Créer des threads pour calculer le temps d'exécution de chaque algorithme de tri
threads = [
    threading.Thread(target=calculer_temps_execution, args=(tri_par_selection, liste_nombres.copy())),
    threading.Thread(target=calculer_temps_execution, args=(tri_a_bulles, liste_nombres.copy())),
    threading.Thread(target=calculer_temps_execution, args=(tri_insertion, liste_nombres.copy())),
    threading.Thread(target=calculer_temps_execution, args=(tri_fusion, liste_nombres.copy())),
    threading.Thread(target=calculer_temps_execution, args=(tri_par_tas, liste_nombres.copy())),
    threading.Thread(target=calculer_temps_execution, args=(tri_rapide, liste_nombres.copy())),
    threading.Thread(target=calculer_temps_execution, args=(tri_peigne, liste_nombres.copy())),
]

# Démarrer tous les threads
for thread in threads:
    thread.start()

# Attendre la fin de tous les threads
for thread in threads:
    thread.join()

# Générer une nouvelle liste aléatoire pour l'affichage graphique
liste_graphique = liste_aleatoire(180)
# Créer et exécuter l'interface graphique
roue = TriGraphique(liste_graphique)
roue.run()
