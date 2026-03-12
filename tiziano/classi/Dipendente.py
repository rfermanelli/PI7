"""
Scrivere la classe dipendente che ha
matricola stringa con numero
stipendio float con stipendio base
straordinario un float con importo dovuto per ciascuna ora di straordinario
costruttore prende i parametri
Metodo getStipendio restituisce il valore di stipendio
Metodo paga ha parametro int ore di straordinario
    restituisce somma tra stipendio e (parametro * straordinario)
Metodo stampa che stampa gli attributi della classe
"""

class Dipendente:

    def __init__(self, mat: str, stip: float, extra: float):
        self.matricola = mat
        self.stipendio = stip
        self.straordinario = extra

    def getStipendio(self):
        return self.stipendio

    def paga(self, ore: int):
        return self.stipendio + ore * self.straordinario

    def stampa(self):
        print(f"Matricola: {self.matricola}\n"
              f"Stipendio base: {self.stipendio}\n"
              f"Paga per ora di straordinario: {self.straordinario}")

"""
Sottoclasse DipendenteA che ha in più malattia, int con giorni che inizia a 0
Metodo prendiMalattia con parametro un int con i giorni
    modifica malattia sommando il parametro
Ridefinire paga: definisci p = paga della superclasse, se malattia == 0 restituisce p
    altrimenti restituisce p - (malattia * 15.0)
Metodo stampaMalattia stampa malattia
"""

class DipendenteA(Dipendente):

    def __init__(self, mat: str, stip: float, extra: float):
        super().__init__(mat, stip, extra)
        self.malattia = 0

    def prendiMalattia(self, giorni):
        self.malattia += giorni
        print(f"Aggiunti {giorni} giorni presi di malattia al dipendente.")

    def paga(self, ore):
        p = super().paga(ore)
        if self.malattia > 0:
            p -= self.malattia * 15.0
        return p

    def stampaMalattia(self):
        print(f"Giorni di malattia presi dal dipendente: {self.malattia}")

"""
Classe CalcolaStipendi con metodo main che:
    crea dipendente matricola 00309 stipendio 1000.0 straordinario 7.5
    richiama paga parametro 10
    stampa richiamando getStipendio
    crea dipendenteA matricola 00201 stipendio 1500.0 straordinario 8.5
    richiama metodo prendiMalattia parametro 5
    richiama metodo paga parametro 3
    richiama stampaMalattia
"""

class CalcolaStipendi:

    def main(self):
        dip1 = Dipendente(mat="00309", stip=1000.0, extra=7.5)
        print(f"Paga spettata: {dip1.paga(10)}")
        print(dip1.getStipendio())
        dip2 = DipendenteA(mat="00201", stip=1500.0, extra=8.5)
        dip2.prendiMalattia(5)
        print(f"Paga spettata: {dip2.paga(3)}")
        dip2.stampaMalattia()

calcolo = CalcolaStipendi()
calcolo.main()