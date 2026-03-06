##Matrici_Ecercizi13
##Scrivere una funzione che restituisca il gioco del tris (tic-tac-toe). Le regole che la macchina deve seguire sono le seguenti:
##L’utente segna il simbolo ‘X’;
##La macchina segna il simbolo ‘O’;
##La macchina deve preferire gli spazi vuoti centrali rispetto agli spazi vuoti agli angoli;
##La macchina deve segnare il simbolo ‘O’ in una riga (o colonna o diagonale) dove ci sono già due simboli ‘O’ e uno degli spazi è vuoto.
##La macchina deve segnare il simbolo ‘O’ in una riga (o colonna o diagonale) dove ci sono già due simboli ‘X’ e uno degli spazi è vuoto.
##La macchina deve segnare il simbolo ‘O’ in una riga (o colonna o diagonale) dove c’è già un simbolo ‘O’ e due degli spazi sono vuoti.
def get_lines():
    return [
        [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
    ]


# all for checking

def find_move(board, symbol):
    for line in get_lines():
        values = [board[i][j] for i, j in line]  # To chekc X and O
        if values.count(symbol) == 2 and values.count(" ") == 1:  # 2: O or X, 1: empty
            return line[values.index(" ")]
    return None


def computer_move(board):
    move = find_move(board, "O")  # To win as much as possible
    if not move:
        move = find_move(board, "X")  # protect

    # just place O
    if move:
        i, j = move
        board[i][j] = "O"
        return

    # Place an O in the center if it's empty
    if board[1][1] == " ":
        board[1][1] = "O"
        return

    # if there is one O and two empty places, place an O
    for line in get_lines():
        values = [board[i][j] for i, j in line]
        if values.count("O") == 1 and values.count(" ") == 2:
            i, j = line[values.index(" ")]
            board[i][j] = "O"
            return

        # Use | to make it easier to read


def print_board(board):
    for row in board:
        print("|".join(row))
    print()


# To check the winner
def check_winner(board):
    for line in get_lines():
        values = [board[i][j] for i, j in line]
        if values == ["X", "X", "X"]:
            return "X"
        if values == ["O", "O", "O"]:
            return "O"
    return None


def main():
    print("Esercizio Le matrici n. 13")
    print("Giochiamo tic-tac-toe!")
    while True:
        board = [[" "] * 3 for _ in range(3)]

        while True:
            try:
                print_board(board)
                print("Tocca all'utente di giocare")
                r = int(input("riga (0-2): "))
                c = int(input("colonna (0-2): "))

                if board[r][c] != " ":
                    print("É gia occupato")
                    continue

            except (IndexError, ValueError):
                print("É invalido")
                continue

            board[r][c] = "X"
            if check_winner(board) == "X":
                print_board(board)
                print("Hai vinto tu！")
                break

            computer_move(board)
            if check_winner(board) == "O":
                print_board(board)
                print("Ha vinto il computer！")
                break

            if all(cell != " " for row in board for cell in row):  # all? to check true or false the condition
                print_board(board)
                print("Pareggio")
                break

        again = input("Vuoi giocare di nuovo?(s/n)").lower().strip()
        if again != "s":
            print("Grazie per aver giocato! Ci vediamo!")
            break


if __name__ == "__main__":
    main()