from sorting import *
import threading
import random

liste_nombres = []
for i in range(1, 1001):
    liste_nombres.append(i)
random.shuffle(liste_nombres)

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


liste = liste_aleatoire(180)
roue = TriGraphique(liste)
roue.run()
