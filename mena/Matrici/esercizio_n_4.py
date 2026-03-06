def ruota_90_orario(matrice):

    n = len(matrice)
    nuova = [ ]

    for j in range (n):
        riga = [ ]
        for i in range(n-1, -1, -1):
            riga.append(matrice[i][j])
        nuova.append(riga)

    return nuova

print(ruota_90_orario([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
