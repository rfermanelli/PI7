"""Esercizio n. 2: libro
Scrivere una funzione che definisca:
a) una classe Libro con attributi titolo, autore, genere e disponibilità (booleano);
b) una classe Biblioteca che contenga una lista di libri e metodi per:
    aggiungere un nuovo libro, prestare un libro a un utente; restituire un libro; stampare l'elenco dei libri disponibili.
"""

class Libro:

    def __init__(self, titolo, autore, genere, disp:bool):
        self.titolo = titolo
        self.autore = autore
        self.genere = genere
        self.is_available = disp

    def __str__(self):
        return f'"{self.titolo}" di {self.autore}'



class Biblioteca:

    def __init__(self):
        self.lista_libri = []

    def aggiungi_libro(self):
        titolo = input("Inserisci un titolo: ")
        autore = input("Inserisci un autore: ")
        genere = input("Inserisci un genere: ")
        is_a = input("Il libro è disponibile? s/n: ").lower()
        is_a = True if is_a == "s" else False
        nuovo_libro = Libro(titolo, autore, genere, is_a)
        self.lista_libri.append(nuovo_libro)
        print("Libro aggiunto al catalogo.")

    def presta_libro(self, utente, titolo):
        for libro in self.lista_libri:
            if libro.nome == titolo:
                if not libro.is_available:
                    print("Libro non disponibile.")
                    return
                libro.is_available = False
                print(f"Il libro {libro} è stato prestato a {utente}.")
                return
        print("Libro non trovato.")

    @staticmethod
    def restituisci_libro(libro:Libro):
        libro.is_available = True
        print(f"{libro} ricevuto, è di nuovo disponibile.")

    def stampa_libri(self):
        for libro in self.lista_libri:
            if libro.is_available:
                print(libro.__dict__)