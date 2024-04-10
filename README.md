# sorting-algorithms


Ce projet vise à créer une interface graphique interactive pour illustrer le fonctionnement de différents algorithmes de tri en Python. L'objectif est de rendre les concepts des algorithmes de tri plus accessibles en les présentant de manière visuelle.

## Algorithmes Utilisés

### 1. Tri par Sélection
- **Idée simple**: À chaque étape, trouvez le plus petit élément de la liste non triée et placez-le à la fin de la partie triée.
- **Analogie**: Comme trier des cartes en sélectionnant à chaque fois la carte avec la valeur la plus basse et la plaçant à la bonne position.
  
### 2. Tri à Bulles
- **Idée simple**: Parcourez la liste et échangez les éléments adjacents s'ils ne sont pas dans le bon ordre. Répétez cela jusqu'à ce que la liste soit entièrement triée.
- **Analogie**: Comme faire remonter les bulles dans un verre d'eau gazeuse. Les bulles montent vers le haut jusqu'à ce qu'elles soient toutes alignées.

### 3. Tri par Insertion
- **Idée simple**: Parcourez la liste et insérez chaque élément à sa place correcte dans la partie triée de la liste.
- **Analogie**: Comme trier des cartes en main en les insérant dans la bonne position tout en parcourant la main.

### 4. Tri Fusion
- **Idée simple**: Divisez la liste en deux moitiés, triez chaque moitié séparément, puis fusionnez-les pour obtenir une liste triée.
- **Analogie**: Comme diviser une pile de cartes en deux tas, trier chaque tas individuellement, puis fusionner les tas triés en une seule pile.

### 5. Tri Rapide
- **Idée simple**: Choisissez un élément pivot, partitionnez la liste autour du pivot en plaçant les éléments plus petits à gauche et les éléments plus grands à droite, puis triez récursivement les sous-listes.
- **Analogie**: Comme organiser un groupe de personnes en deux groupes : ceux qui sont plus petits qu'une personne choisie (le pivot) et ceux qui sont plus grands, puis répéter ce processus pour chaque groupe.

### 6. Tri par Tas
- **Idée simple**: Transformez la liste en une structure de données appelée tas, puis extrayez séquentiellement les éléments du tas pour les placer dans la liste triée.
- **Analogie**: Comme organiser un groupe de personnes par taille, en plaçant la plus grande personne à la fin de la file et en déplaçant les personnes plus petites vers l'avant jusqu'à ce que tout le monde soit en ordre.

## Mesures de Performance
Pour évaluer les performances de chaque algorithme, une liste de 1000 nombres est générée aléatoirement et mélangée. Chaque algorithme est ensuite exécuté sur une copie de cette liste dans un thread séparé pour mesurer le temps d'exécution de chaque algorithme.


## Conclusion

Ce projet offre une manière ludique et visuelle d'explorer les différents algorithmes de tri. En utilisant des analogies simples et en fournissant une interface interactive, il rend les concepts des algorithmes de tri plus compréhensibles pour un large public, permettant aux utilisateurs d'appréhender les performances et les comportements de chaque algorithme de manière intuitive. De plus, en mesurant les performances de chaque algorithme sur des ensembles de données réels, les utilisateurs peuvent obtenir des informations concrètes sur la rapidité d'exécution de chaque algorithme, ce qui peut les aider à prendre des décisions éclairées lors du choix de l'algorithme à utiliser dans leurs propres projets.
