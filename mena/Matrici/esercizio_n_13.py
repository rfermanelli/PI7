def mossa_macchina(matrice):
    combinazioni = [
        [(0,0), (0,1), (0,2)],  # righe
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],

        [(0,0), (1,0), (2,0)],  # colonne
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],

        [(0,0), (1,1), (2,2)],  # diagonali
        [(0,2), (1,1), (2,0)]
    ]

    #  vincere con due "O" e uno spazio vuoto
    for linea in combinazioni:
        valori = [matrice[r][c] for r, c in linea]
        if valori.count("O") == 2 and valori.count(" ") == 1:
            r, c = linea[valori.index(" ")]
            return r, c

    #  bloccare con due "x" e uno spazio vuoto
    for linea in combinazioni:
        valori = [matrice[r][c] for r, c in linea]
        if valori.count("X") == 2 and valori.count(" ") == 1:
            r, c = linea[valori.index(" ")]
            return r, c

    #  segna una "o" in una riga, una colonna o diagonale dove c'è un'altra "o"
    for linea in combinazioni:
        valori = [matrice[r][c] for r, c in linea]
        if valori.count("O") == 1 and valori.count(" ") == 2:
            r, c = linea[valori.index(" ")]
            return r, c

    #  centro
    if matrice[1][1] == " ":
        return 1, 1

    # Angoli
    for r, c in [(0,0), (0,2), (2,0), (2,2)]:
        if matrice[r][c] == " ":
            return r, c

    # Lati
    for r, c in [(0,1), (1,0), (1,2), (2,1)]:
        if matrice[r][c] == " ":
            return r, c

# mossa utente
def mossa_utente(matrice):
    combinazioni = [
        [(0,0), (0,1), (0,2)], #righe
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],

        [(0, 0), (1, 0), (2, 0)],  # colonne
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        [(0, 0), (1, 1), (2, 2)],  # diagonali
        [(0, 2), (1, 1), (2, 0)]
    ]
    r, c = combinazioni[0][0]
    if matrice[r][c] == " ":
        return r, c
    for linea in combinazioni:
        valori = [matrice[r][c] for r, c in linea]
        if valori.count("O") == 2 and valori.count(" ") == 1:
            r, c = linea[valori.index(" ")]
            return r, c
    for linea in combinazioni:
        valori = [matrice[r][c] for r, c in linea]
        if valori.count("X") == 2 and valori.count(" ") == 1:
            r, c = linea[valori.index(" ")]
            return r, c
        if matrice[r][c] == "x":
            return r, c
        stampa = matrice[r][c]
        print("hai vinto")
