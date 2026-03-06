##Matrici_Ecercizi14
##Scrivere una funzione che restituisca il gioco del campo minato per una matrice 4x4, con cinque mine.
import random


def create_board(size=4, mines=5):
    print("The board")
    board = [[" " for _ in range(size)] for _ in range(size)]
    mine_positions = random.sample(range(size * size), mines)  # range(size*size): 0-15(4*4=16)
    # random.sample? Prende a caso un certo numero di elementi unici da una lista.
    for pos in mine_positions:
        r = pos // size
        c = pos % size
        # Un calcolo per convertire un indice a una dimensione in coordinate a due dimensioni.
        board[r][c] = "*"  # mines: *
    return board


def print_board(board, revealed):
    # revealed viene definito nel main
    size = len(board)
    print("  " + " ".join(str(i) for i in range(size)))
    for i, row in enumerate(board):
        row_display = []
        for j, cell in enumerate(row):
            if revealed[i][j]:
                if cell == "*":
                    row_display.append("*")
                else:
                    row_display.append(cell)
            else:
                row_display.append(" ")
        print(f"{i} " + " ".join(row_display))
    print()


def count_mines_around(board, r, c):
    size = len(board)
    count = 0
    for i in range(max(0, r - 1), min(size, r + 2)):
        for j in range(max(0, c - 1), min(size, c + 2)):
            if (i, j) != (r, c) and board[i][j] == "*":  # (i,j) = (r,c) : center
                count += 1
    return str(count)


def main():
    size = 4
    mines = 5
    board = create_board(size, mines)
    revealed = [[False] * size for _ in range(size)]  # All'inizio le celle sono nascoste
    safe_cells = size * size - mines
    print("Matrici_Ecercizi14")
    print("Scrivere una funzione che restituisca il gioco del campo minato per una matrice 4x4, con cinque mine.")
    print("₍₍ (ง ˘ω˘ )ว ⁾⁾")
    print("Campo minato 4x4 （5 mine）")

    while True:
        print_board(board, revealed)
        while True:
            # user Input
            try:
                print("Tocca all'utente di giocare")
                r = int(input("Riga (0-3): "))
                c = int(input("Colonna (0-3): "))
                if not (0 <= r < size and 0 <= c < size):
                    print("Inserisci un numero tra 0 e 3")
                    continue
                if revealed[r][c]:
                    print("Quella cella é gia stata scoperta")
                    continue
            except ValueError:
                print("Inserisci un numero")
                continue

            # mines or no
            if board[r][c] == "*":
                print_board(board, [[True] * size for _ in range(size)])
                print("Game over! Hai colpito una mina")
                break
            else:
                revealed[r][c] = True
                board[r][c] = count_mines_around(board, r, c)
                safe_cells -= 1

            # safe cells = 0: Win
            if safe_cells == 0:
                print_board(board, [[True] * size for _ in range(size)])
                print("Congratuzioni！Hai scoperto tutte le celle evitando le mine")
                break
        # again
        again = input("Vuoi giocare di nuovo?(s/n)").lower().strip()
        if again != "s":
            print("Grazie per aver giocato! Ci vediamo!")
            break


if __name__ == "__main__":
    main()