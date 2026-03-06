def stampa_matrice(mat, messaggio):
    """Stampa una matrice."""
    num = 0
    for riga in mat:
        print(num, riga)
        num += 1
    print(messaggio)

def esercizio_13():
    """Funzione che restituisce il gioco del tris (tic-tac-toe) seguendo le regole specificate per la macchina
     e per l’utente."""
    def visualizza_partita(matrice):
        """Stampa la tabella di gioco."""
        game_mat = [riga[:] for riga in matrice]
        for i in range(3):
            for j in range(3):
                if game_mat[i][j] == 0:
                    game_mat[i][j] = " "
                elif game_mat[i][j] == 1:
                    game_mat[i][j] = "X"
                elif game_mat[i][j] == 2:
                    game_mat[i][j] = "O"
        print("    0    1    2")
        stampa_matrice(game_mat, "Stato della partita:")

    def controllo_vittoria(matrice, simbolo):
        """Controlla se un giocatore ha vinto."""
        for i in range(3):
            if matrice[i][0] == simbolo and matrice[i][1] == simbolo and matrice[i][2] == simbolo:
                return True
        for j in range(3):
            if matrice[0][j] == simbolo and matrice[1][j] == simbolo and matrice[2][j] == simbolo:
                return True
        if matrice[0][0] == simbolo and matrice[1][1] == simbolo and matrice[2][2] == simbolo:
                return True
        if matrice[0][2] == simbolo and matrice[1][1] == simbolo and matrice[2][0] == simbolo:
                return True
        return False

    def controllo_pareggio(matrice):
        """Controlla se c'è un pareggio."""
        conta_zeri = 0
        for riga in matrice:
            for j in riga:
                if riga[j] == 0:
                    conta_zeri += 1
        return conta_zeri


    def ricerca_spazi_in_righe(matrice, simbolo, totale_simboli):
        """Individua la mossa da fare a seconda degli spazi nelle righe."""
        indice = 0
        while indice < 3:
            conta_simboli = 0
            conta_zeri = 0
            for i in range(3):
                if matrice[indice][i] == simbolo:
                    conta_simboli += 1
                elif matrice[indice][i] == 0:
                    conta_zeri += 1
            for i in range(3):
                if totale_simboli == conta_simboli and conta_zeri > 0 and matrice[indice][i] == 0:
                    return indice, i
            indice += 1
        return None

    def ricerca_spazi_in_colonne(matrice, simbolo, totale_simboli):
        """Individua la mossa da fare a seconda degli spazi nelle colonne."""
        indice = 0
        while indice < 3:
            conta_simboli = 0
            conta_zeri = 0
            for i in range(3):
                if matrice[i][indice] == simbolo:
                    conta_simboli += 1
                elif matrice[i][indice] == 0:
                    conta_zeri += 1
            for i in range(3):
                if totale_simboli == conta_simboli and conta_zeri > 0 and matrice[i][indice] == 0:
                    return i, indice
            indice += 1
        return None

    def ricerca_spazi_in_diagonali(matrice, simbolo, totale_simboli):
        """Individua la mossa da fare a seconda degli spazi nelle due diagonali."""
        conta_simboli = 0
        conta_zeri = 0
        for i in range(3):
            if matrice[i][i] == simbolo:
                conta_simboli += 1
            elif matrice[i][i] == 0:
                conta_zeri += 1
        if totale_simboli == conta_simboli and conta_zeri > 0:
            for i in range(3):
                if matrice[i][i] == 0:
                    return i, i
        conta_simboli = 0
        conta_zeri = 0
        for i in range(3):
            j = 2 - i
            if matrice[i][j] == simbolo:
                conta_simboli += 1
            elif matrice[i][j] == 0:
                conta_zeri += 1
        if totale_simboli == conta_simboli and conta_zeri > 0:
            for i in range(3):
                j = 2 - i
                if matrice[i][j] == 0:
                    return i, j
        return None

    def cervello_cpu(matrice, simbolo_cpu, simbolo_utente):
        """Calcola la mossa ottimale per il computer."""
        angoli = [(0, 0), (0, 2), (2, 0), (2, 2)]
        mossa = ricerca_spazi_in_righe(matrice, simbolo_cpu, 2)
        if mossa:
            return mossa
        mossa = ricerca_spazi_in_colonne(matrice, simbolo_cpu, 2)
        if mossa:
            return mossa
        mossa = ricerca_spazi_in_diagonali(matrice,simbolo_cpu, 2)
        if mossa:
            return mossa
        mossa = ricerca_spazi_in_righe(matrice, simbolo_utente, 2)
        if mossa:
            return mossa
        mossa = ricerca_spazi_in_colonne(matrice, simbolo_utente, 2)
        if mossa:
            return mossa
        mossa = ricerca_spazi_in_diagonali(matrice,simbolo_utente, 2)
        if mossa:
            return mossa
        mossa = ricerca_spazi_in_righe(matrice, simbolo_cpu, 1)
        if mossa:
            return mossa
        mossa = ricerca_spazi_in_colonne(matrice, simbolo_cpu, 1)
        if mossa:
            return mossa
        mossa = ricerca_spazi_in_diagonali(matrice,simbolo_cpu, 1)
        if mossa:
            return mossa
        if matrice[1][1] == 0:
            return 1, 1
        for i, j in angoli:
            if matrice[i][j] == 0:
                return i, j
        return None

    is_looping = True
    print("Benvenuto a Tris!")
    while is_looping:
        print("Tu utilizzerai la 'X', il computer utilizzerà il 'O'.")
        mat = [[0] * 3 for _ in range(3)]
        visualizza_partita(mat)
        while True:
            while True:
                try:
                    coordinate = input("Inserisci riga (sinistra) e colonna (destra) (Da 0 a 2, es. '1 1'): ").split()
                    if len(coordinate) != 2:
                        raise ValueError("Per favore, riprova. Assicurati di aver digitato correttamente le coordinate.")
                    r = int(coordinate[0])
                    c = int(coordinate[1])
                    if r < 0 or r > 2 or c < 0 or c > 2:
                        raise ValueError("Le coordinate devono essere tra 0 e 2.")
                    if mat[r][c] != 0:
                        raise ValueError("La cella è già occupata! Scegli un'altra posizione.")
                    if mat[r][c] == 0:
                        mat[r][c] = 1
                        break
                except ValueError as e:
                    print(f"Errore: {e}")
            visualizza_partita(mat)
            if controllo_vittoria(mat, 1):
                print("Hai vinto!")
                break
            patta = controllo_pareggio(mat)
            if patta == 0:
                print("Pareggio!")
                break
            coordinate = cervello_cpu(mat, 2, 1)
            if len(coordinate) == 2:
                r = int(coordinate[0])
                c = int(coordinate[1])
                mat[r][c] = 2
                print(f"Mossa del computer: {r} {c}")
            visualizza_partita(mat)
            if controllo_vittoria(mat, 2):
                print("Hai perso...")
                break
            patta = controllo_pareggio(mat)
            if patta == 0:
                print("Pareggio!")
                break
        rigioca = input("Vuoi giocare ancora? Rispondi 's' o 'n': ").lower()
        if rigioca == "n":
            is_looping = False
            print("Alla prossima!")


esercizio_13()