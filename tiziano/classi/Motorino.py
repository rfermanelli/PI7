"""
Classe motorino con:
colore
velocità float in kh/h
tipo ossia marca e modello
antifurto booleano di base false
Parametri: colore, tipo, velocità
Metodo getVelocità restituisce la velocità del motorino
Metodo accelera ha come parametro un float che indica i km/h che si vogliono aggiungere alla velocità:
    Se antifurto è false lo fa, altrimenti non fa nulla
Metodo inserisciAntifurto assegna un valore true ad antifurto
"""

class Motorino:

    def __init__(self, col:str, tipo:str, vel:float):
        self.colore = col
        self.tipo = tipo
        self.velocita = vel
        self.antifurto = False

    def getVelocita(self):
         return f"{self.velocita} Km/h"

    def accelera(self, accel: float):
        if self.antifurto:
             print("L'antifurto è attivo, non accelero.")
        else:
            self.velocita += accel
            print(f"Velocità attuale: {self.velocita}")

    def inserisciAntifurto(self):
        self.antifurto = True
        print("Antifurto inserito.")

"""
Scrivere classe MotorinoImmatricolato, sottoclasse di Motorino
2 attributi in più, maxVelocita un float con la velocità massima
    e targa stringa che indica la targa del motorino
Metodo getMax stampa il valore di maxVelocità
ridefinire accelera così che prima di modificare la velocità controlla la maxVelocità
    definisce variabile s di tipo float e ci assegna la somma tra parametro e valore di velocità
    se s è minore di maxVelocità assegna il valore di s a velocità
    altrimenti assegna all'attributo velocità il valore di maxVelocità
"""
class MotorinoImmatricolato(Motorino):
    
    def __init__(self, col:str, tipo:str, vel:float, maxvel:float, targa:str):
        super().__init__(col, tipo, vel)
        self.maxVelocita = maxvel
        self.targa = targa

    def getMax(self):
        return f"{self.maxVelocita} Km/h"

    def accelera(self, accel: float):
        if self.antifurto:
            print("L'antifurto è attivo, non accelero.")
        else:
            s = accel + self.velocita
            if s >= self.maxVelocita:
                self.velocita = self.maxVelocita
            else:
                self.velocita = s
            print(f"Velocità attuale: {self.velocita}")

"""
Scrivere classe UsoMotorino che ha
il metodo main in cui si crea un oggetto motorino di colore grigio metallizzato
    con velocità 40.5 e tip Piaggio Liberty
    richiama getVelocità e memorizza il valore in una variabile
    Poi crea un altro oggetto di tipo MotorinoImmatricolato con colore rosso, velocità 30.5
    e tipo Aprilia Scarabeo, maxVelocita 60 targa CV1234
    e richiama il metodo getMax
    Infine richiama il metodo accelera con parametro pari a 30.7 per entrambi
    e richiamare metodo getVelocita per entrambi
"""

class UsoMotorino:

    def main(self):
        piaggio = Motorino(col="Grigio metallizzato", tipo="Piaggio Liberty", vel=40.5)
        velocita_piaggio = piaggio.getVelocita()

        scarabeo = MotorinoImmatricolato(col="Rosso", tipo="Aprilia Scarabeo", vel=30.5, maxvel=60.0, targa="CV1234")
        maxvel_scarabeo = scarabeo.getMax()

        piaggio.accelera(30.7)
        scarabeo.accelera(30.7)
        velocita_piaggio = piaggio.getVelocita()
        velocita_scarabeo = scarabeo.getVelocita()
        print(velocita_scarabeo, velocita_piaggio)

uso = UsoMotorino()
uso.main()