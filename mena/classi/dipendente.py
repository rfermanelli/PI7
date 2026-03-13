class Dipendente:
    def __init__(self, matricola, stipendio,straordinario):       # con il costruttore inizializzo gli attributi dell'oggetto
        self.matricola = matricola
        self.stipendio = stipendio
        self.straordinario = straordinario

    #d1 = Dipendente("00309", 1000.00, "7.50")       # creo il primo dipendente

    def getStipendio(self):         # metodo che restituisce lo stipendio
            return self.stipendio

    def paga(self, ore):
        # metodo che calcola stipendio più straordinario
        totale_paga = self.stipendio + (ore * self.straordinario)
        return totale_paga

    def stampa(self):
        # stampo i dati del Dipendente
        print("matricola:", self.matricola)
        print("stipendio:", self.stipendio)
        print("straordinario:", self.straordinario)

class DipendenteA(Dipendente):              #classe che eredita da Dipendente
    def __init__(self, matricola, stipendio, straordinario, malattia):  # inizializzo gli attributi di DipendenteA
        super().__init__(matricola, stipendio, straordinario)           # super() chiama il costruttore della classe padre
        self.malattia = malattia

        #dipendente2 = DipendenteA("00201", 1500.00, "8.50", 0)       # creo il secondo dipendente

    def prendiMalattia(self, giorni):
            self.malattia = self.malattia + giorni                             # aumento dei giorni di malattia

    def paga(self, ore):                        # override
            p = super().paga(ore)                   # calcolo lo stipendio usando il metodo paga della classe padre

            if self.malattia == 0:                   # se non ci sono giorni di malattia
                return p
            else:
                return p - 15 * self.malattia     # altrimenti si detraggono

    def stampaMalattia(self):
            print("giorni di malattia:", self.malattia)


class CalcolaStipendi:

    def Main(self):                                 # programma principale
        d1 = Dipendente("00309", 1000.00, 7.50)
        d1.paga(10)                                 # paga con 10 ore di straordinario
        print(d1.getStipendio())

        dA = DipendenteA("00201", 1500.00, 8.50, 0)
        dA.prendiMalattia(5)                            # il dA prende 5 giorni di malattia
        stipendio1 = dA.paga(3)                         # paga con tre ore di straordinario
        print("stipendio1:", stipendio1)

        dA.stampaMalattia()

CalcolaStipendi().Main()                      # avvio del programma
