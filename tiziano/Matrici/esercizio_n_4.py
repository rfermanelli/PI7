def esercizio_4():
    """Funzione che, data una matrice quadrata di ordine n,
    restituisce una matrice che è la rotazione di 90 gradi
    in senso orario della matrice data."""
    n = int(input("Inserisci il valore di n: "))
    mat =[0] * n
    valore = 1
    for i in range(n):
        riga = [0] * n
        for j in range(n):
            riga[j] = valore
            valore += 1
        mat[i] = riga
    print("Matrice originale:")
    for riga in mat:
        print(riga)
    new_mat = [0] * n
    for i in range(n):
        new_riga = [0] * n
        for j in range(n):
            new_riga[j] = mat[n - 1 - j][i]
        new_mat[i] = new_riga
    print("Matrice ruotata di 90 gradi:")
    for new_riga in new_mat:
        print(new_riga)

esercizio_4()
