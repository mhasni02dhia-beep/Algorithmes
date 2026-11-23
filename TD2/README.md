Exercice 3 — Problème du voyageur de commerce

Données du problème

- Nombre de villes : 8
- Circuit initial : 1-2-3-4-5-6-7-8-1
- Les distances entre les villes sont représentées par une matrice.
- Les liaisons inexistantes dans le tableau sont représentées par une grande valeur (999).

  1. Recherche Taboue
 
- Solution initiale : 1-2-3-4-5-6-7-8-1
- Voisinage : échange de deux villes.
- Liste taboue de taille 5.
- Nombre d'itérations : 100.
- Conservation du meilleur circuit trouvé.

 2. Recuit Simulé

- Solution initiale : circuit de départ.
- Nombre d'itérations : 5.
- Température initiale : T = 100.
- Variation empirique de la température : T = T × 0.8.
- Acceptation des solutions meilleures et possibilité d'accepter des solutions moins bonnes selon une probabilité.

  3. Algorithme Génétique
 
- Population initiale : 50 circuits.
- Nombre de générations : 100.
- Sélection des parents parmi les 20 meilleurs individus.
- Croisement entre deux parents.
- Mutation par échange de deux villes.
- Probabilité de mutation : 20 %.
- Conservation des 5 meilleurs individus.
