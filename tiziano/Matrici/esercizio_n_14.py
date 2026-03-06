# Funzione che restituisce il gioco del campo minato per una matrice 4x4 con cinque mine.
import random

MINE = 5
DIMENSIONE = 4

def visualizza_partita(matrice):
    """Stampa la tabella di gioco."""
    print("Stato della partita:")
    print("     0     1     2     3")
    print("  -------------------------")
    for i in range(4):
        print(f"{i} |", end="")
        for j in range(4):
            print(f" {matrice[i][j]} |", end="")
        print("\n  -------------------------")

def genera_mine(numero_mine, matrice, righe, colonne):
    conta_mine = 0
    while conta_mine < numero_mine:
        i = random.randint(0, righe - 1)
        j = random.randint(0, colonne - 1)
        if matrice[i][j] == 0:
            matrice[i][j] = -1
            conta_mine += 1

def conta_mine_adiacenti(matrice, i, j, righe, colonne):
    posizioni = [
        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),  # riga sopra
        (i, j - 1), (i, j + 1),               # sinistra e destra
        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)   # riga sotto
    ]
    numero_visualizzato = 0
    for r, c in posizioni:
        if 0 <= r < righe and 0 <= c < colonne:
            if matrice[r][c] == -1:
                numero_visualizzato += 1
    return numero_visualizzato

def genera_numeri_adiacenti_a_mine(matrice, righe, colonne):
    for i in range(righe):
        for j in range(colonne):
            if matrice[i][j] != -1:
                matrice[i][j] = conta_mine_adiacenti(matrice, i, j, righe, colonne)

def controllo_vittoria(matrice, righe, colonne, conta_mine):
    conta_celle_coperte = 0
    for i in range(righe):
        for j in range(colonne):
            if matrice[i][j] == "   ":
                conta_celle_coperte += 1

    if conta_celle_coperte == conta_mine:
        return True
    return False


print("Benvenuto a Campo Minato!")
print(f"Numero mine: {MINE}")
matrice_gioco = [[0] * DIMENSIONE for _ in range(DIMENSIONE)]
matrice_vista = [["   "] * DIMENSIONE for _ in range(DIMENSIONE)]
numero_righe = (len(matrice_gioco))
numero_colonne = (len(matrice_gioco[0]))
genera_mine(MINE, matrice_gioco, numero_righe,  numero_colonne)
genera_numeri_adiacenti_a_mine(matrice_gioco, numero_righe, numero_colonne)
visualizza_partita(matrice_vista)
game_over = False

while not game_over:
    while True:
        try:
            coordinate = input(f"Inserisci riga (sinistra) e colonna (destra) (Da 0 a {DIMENSIONE - 1}, es. '0 0'): ").split()
            if len(coordinate) != 2:
                raise ValueError("Per favore, riprova. Assicurati di aver digitato correttamente le coordinate.")
            a = int(coordinate[0])
            b = int(coordinate[1])
            if a < 0 or a > 3 or b < 0 or b > 3:
                raise ValueError("Le coordinate devono essere tra 0 e 3.")
            if matrice_vista[a][b] != "   ":
                raise ValueError("La cella è già scoperta! Scegli un'altra posizione.")
            if matrice_vista[a][b] == "   ":
                if matrice_gioco[a][b] != -1:
                    matrice_vista[a][b] = " " + str(matrice_gioco[a][b]) + " "
                    break
                else:
                    game_over = True
                    matrice_vista[a][b] = "!!!"
                    print("Hai perso...")
                    break
        except ValueError as e:
            print(f"Errore: {e}")
    visualizza_partita(matrice_vista)
    if not game_over:
        if controllo_vittoria(matrice_vista, numero_righe, numero_colonne, MINE):
            print("Hai vinto!")
            break
if game_over:
    print("Game over!")