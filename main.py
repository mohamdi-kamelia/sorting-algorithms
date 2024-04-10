from sorting import *
import threading
import random

number_list = []
for i in range(1,1001):
    number_list.append(i)
random.shuffle(number_list)

threads = [
    threading.Thread(target=calculer_temps_execution, args=(tri_par_selection, number_list.copy())),
    threading.Thread(target=calculer_temps_execution, args=(tri_a_bulles, number_list.copy())),
    threading.Thread(target=calculer_temps_execution, args=(tri_insertion, number_list.copy())),
    threading.Thread(target=calculer_temps_execution, args=(tri_fusion, number_list.copy())),
    threading.Thread(target=calculer_temps_execution, args=(tri_par_tas, number_list.copy())),
    threading.Thread(target=calculer_temps_execution, args=(tri_rapide, number_list.copy())),
    threading.Thread(target=calculer_temps_execution, args=(tri_peigne, number_list.copy())),
]

# Start all threads
for thread in threads:
    thread.start()

# Join all threads
for thread in threads:
    thread.join()


liste = liste_aleatoire(180)
roue = TriGraphique(liste)
roue.run()