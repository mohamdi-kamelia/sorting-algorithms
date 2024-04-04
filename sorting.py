"""from random import randrange
SIZE =  20

def InsertionSort(lst):
    for step in range(1, len(lst)):
        key = lst[step]
        i = step-1
        while (i >=0) and (key < lst[i]):
                lst[i+1] = lst[i]
                i = i - 1
        lst[i+1] = key
    
# Create a random array    
l = []
for i in range(SIZE):
    l.append(randrange(100))
# Display it
print("Unsorted array :")
for i in range(len(l)):
    print (l[i], end=', ')
# Sort 
InsertionSort(l)
# Display result
print()
print ("Sorted array :")
for i in range(len(l)):
    print (l[i],end=', ')
print()"""
def tri_selection(tableau):
    pass
def tri_bulles(tableau):
    pass
def tri_fusion(tableau):
    pass
def tri_par_tas(tableau):
    pass
def tri_a_peigne(tableau):
    pass
def tri_insertion(tableau):
    pass
def tri_rapide(tableau):
    pass