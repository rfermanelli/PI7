import random
print("=== GIOCO DEL TRIS ===")
print("Le posizioni sono numerate da 1 a 9:\n")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")
board = [" " for _ in range(9)]
user = []
computer = []
# Condizioni di vittoria (insiemi di 3 elementi)
win_conditions = [
{1, 2, 3},
{4, 5, 6},
{7, 8, 9},
{1, 4, 7},
{2, 5, 8},
{3, 6, 9},
{1, 5, 9},
{3, 5, 7}
]
def stampa_scacchiera():
print("\n")
print(f" {board[0]} | {board[1]} | {board[2]} ")
print("---+---+---")
print(f" {board[3]} | {board[4]} | {board[5]} ")
print("---+---+---")
print(f" {board[6]} | {board[7]} | {board[8]} ")
print("\n")
def verifica_vittoria(mosse):
mosse_set = set(mosse)
for condizione in win_conditions:
if condizione.issubset(mosse_set):
return True
return False
def mossa_utente():
while True:
try:
scelta = int(input("Scegli una posizione (1-9): "))
if scelta < 1 or scelta > 9:
print("Inserisci un numero tra 1 e 9.")
elif board[scelta - 1] != " ":
print("Posizione già occupata.")
else:
board[scelta - 1] = "X"
user.append(scelta)
break
except ValueError:
print("Inserisci un numero valido.")
def mossa_computer():
libere = [i for i in range(1, 10) if board[i - 1] == " "]
scelta = random.choice(libere)
board[scelta - 1] = "O"
computer.append(scelta)
print(f"Il computer sceglie la posizione {scelta}")
stampa_scacchiera()
turno = random.choice(["utente", "computer"])
while True:
if turno == "utente":
# Turno utente
mossa_utente()
stampa_scacchiera()
if verifica_vittoria(user):
print("🎉 Hai vinto!")
break
turno = "computer"
else:
# Turno computer
mossa_computer()
stampa_scacchiera()
if verifica_vittoria(computer):
print("💻 Il computer ha vinto!")
break
turno = "utente"
# Controllo pareggio (vale per entrambi)
if len(user) + len(computer) == 9:
print("🤝 Pareggio!")
break