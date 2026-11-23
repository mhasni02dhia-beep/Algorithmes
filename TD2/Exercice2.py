

demandes = [4, 5, 8]

couts = [
    [5, 3, 4],  # D1
    [6, 7, 2]   # D2
]

def calculer_cout(sol):
    total = 0
    for i in range(2):
        for j in range(3):
            total += sol[i][j] * couts[i][j]
    return total

def generer_voisins(sol):
    voisins = []

    for i in range(3):
        for j in range(3):
            if i != j and sol[0][i] > 0:
                nouvelle = [sol[0][:], sol[1][:]]

                nouvelle[0][i] -= 1
                nouvelle[0][j] += 1

                for k in range(3):
                    nouvelle[1][k] = demandes[k] - nouvelle[0][k]

                voisins.append((nouvelle, (i, j)))

    return voisins

solution = [[2, 3, 3], [2, 2, 5]]
meilleure = [solution[0][:], solution[1][:]]

liste_taboue = []

for iteration in range(100):

    voisins = generer_voisins(solution)
    voisins.sort(key=lambda x: calculer_cout(x[0]))

    for voisin, mouvement in voisins:

        if mouvement not in liste_taboue:
            solution = voisin

            liste_taboue.append(mouvement)

            if len(liste_taboue) > 5:
                liste_taboue.pop(0)

            if calculer_cout(solution) < calculer_cout(meilleure):
                meilleure = [solution[0][:], solution[1][:]]

            break

print("Meilleure solution :")
print(meilleure)

print("Coût total :")
print(calculer_cout(meilleure))
