
import math, random

distances = [
    [0, 14, 15, 999, 999, 999, 999, 17],
    [14, 0, 13, 14, 20, 999, 999, 21],
    [15, 13, 0, 11, 21, 17, 9, 9],
    [999, 14, 11, 0, 11, 10, 8, 20],
    [999, 20, 21, 11, 0, 15, 18, 999],
    [999, 999, 17, 10, 15, 0, 9, 999],
    [999, 999, 9, 8, 18, 9, 0, 13],
    [17, 21, 9, 20, 999, 999, 13, 0]
]

def cout(route):
    total = 0
    for i in range(len(route)):
        total += distances[route[i]][route[(i+1) % len(route)]]
    return total

initiale = list(range(8))


# ---------------------------------
# Q1 : RECHERCHE TABOUE
# ---------------------------------
def recherche_taboue(iterations=100, taille_tabou=5):
    courant = initiale[:]
    meilleur = courant[:]
    liste_taboue = []

    for _ in range(iterations):
        meilleur_voisin = None
        meilleur_cout = 999999

        for i in range(1, 8):
            for j in range(i+1, 8):
                voisin = courant[:]
                voisin[i], voisin[j] = voisin[j], voisin[i]

                c = cout(voisin)

                if c < 999 and (i, j) not in liste_taboue:
                    if c < meilleur_cout:
                        meilleur_cout = c
                        meilleur_voisin = voisin
                        mouvement = (i, j)

        if meilleur_voisin is None:
            break

        courant = meilleur_voisin[:]
        liste_taboue.append(mouvement)

        if len(liste_taboue) > taille_tabou:
            liste_taboue.pop(0)

        if cout(courant) < cout(meilleur):
            meilleur = courant[:]

    return meilleur, cout(meilleur)


# ---------------------------------
# Q2 : RECUIT SIMULE (5 iterations)
# ---------------------------------
def recuit_simule(iterations=5, T=100):
    courant = initiale[:]
    meilleur = courant[:]

    for _ in range(iterations):
        i1, i2 = random.sample(range(1, 8), 2)

        voisin = courant[:]
        voisin[i1], voisin[i2] = voisin[i2], voisin[i1]

        delta = cout(voisin) - cout(courant)

        if cout(voisin) < 999:
            if delta < 0 or random.random() < math.exp(-delta/T):
                courant = voisin

        if cout(courant) < cout(meilleur):
            meilleur = courant[:]

        T *= 0.8

    return meilleur, cout(meilleur)


# ---------------------------------
# Q3 : ALGORITHME GENETIQUE
# ---------------------------------

def croisement(parent1, parent2):
    enfant = [None] * 8
    enfant[0] = 0

    debut = random.randint(1, 5)
    fin = random.randint(debut+1, 7)

    for i in range(debut, fin):
        enfant[i] = parent1[i]

    reste = [v for v in parent2 if v not in enfant]

    k = 0
    for i in range(1, 8):
        if enfant[i] is None:
            enfant[i] = reste[k]
            k += 1

    return enfant


def mutation(route):
    nouvelle = route[:]

    i1, i2 = random.sample(range(1, 8), 2)

    nouvelle[i1], nouvelle[i2] = nouvelle[i2], nouvelle[i1]

    return nouvelle


def genetique(population_size=50, generations=100):
    population = [initiale[:]]

    # Creation de la population initiale
    for _ in range(population_size-1):
        route = [0] + random.sample(range(1, 8), 7)
        population.append(route)

    for _ in range(generations):
        population.sort(key=cout)

        nouvelle_population = population[:5]

        while len(nouvelle_population) < population_size:
            parent1 = random.choice(population[:20])
            parent2 = random.choice(population[:20])

            enfant = croisement(parent1, parent2)

            if random.random() < 0.2:
                enfant = mutation(enfant)

            nouvelle_population.append(enfant)

        population = nouvelle_population

    population.sort(key=cout)

    meilleur = population[0]

    return meilleur, cout(meilleur)



random.seed(42)

print("Trajet initial :", [x+1 for x in initiale] + [1])
print("Cout initial :", cout(initiale))

print("\n--- Q1 Recherche Taboue ---")
trajet, c = recherche_taboue()
print("Meilleur trajet :", [x+1 for x in trajet] + [1])
print("Cout :", c)

print("\n--- Q2 Recuit Simule ---")
trajet, c = recuit_simule()
print("Meilleur trajet :", [x+1 for x in trajet] + [1])
print("Cout :", c)

print("\n--- Q3 Algorithme Genetique ---")
trajet, c = genetique()
print("Meilleur trajet :", [x+1 for x in trajet] + [1])
print("Cout :", c)
