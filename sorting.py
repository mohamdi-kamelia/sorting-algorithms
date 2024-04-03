def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divise la liste en deux moitiés
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Récursivement trie les deux moitiés
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Fusionne les moitiés triées
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    
    # Fusionne les deux listes triées
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Ajoute les éléments restants
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    
    return result

# Fonction pour afficher le résultat du tri fusion
def print_merge_sort_result(arr):
    print("Liste originale :", arr)
    sorted_arr = merge_sort(arr)
    print("Liste triée :", sorted_arr)

# Exemple d'utilisation
if __name__ == "__main__":
    # Vous pouvez remplacer cette liste par n'importe quelle liste de nombres réels
    liste_a_trier = [12, 5, 6, 10, 3, 7, 8, 1, 15, 9]
    print_merge_sort_result(liste_a_trier)
