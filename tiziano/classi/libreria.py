"""Scrivere uno script per la realizzazione di una libreria virtuale.

 la libreria è composta da libri e riviste.

 I libri hanno i seguenti attributi: titolo, autore, anno di pubblicazione
e genere;

 le riviste hanno i seguenti attributi: titolo, numero, anno di
pubblicazione e direttore;

 la libreria ha i seguenti comportamenti: aggiungere un elemento (o
libro o rivista), eliminare un elemento (o libro o rivista), eliminare
tutti gli elementi, elencare tutti gli elementi."""

class Libro:

    def __init__(self, titolo, autore, anno, genere):
        self.titolo = titolo
        self.autore = autore
        self.data = anno
        self.genere = genere


class Rivista:

    def __init__(self, titolo, numero, anno, direttore):
        self.titolo = titolo
        self.numero = numero
        self.data = anno
        self.direttore = direttore



class Libreria:

    def __init__(self):
        self.elementi = []

    def aggiungi_elemento(self):
        tipo = input("Cosa vuoi aggiungere, rivista o libro?: ").lower()
        if tipo == "rivista":
            ttl = input("Inserisci un titolo: ")
            n = input("Inserisci un numero: ")
            d = input("Inserisci l'anno di pubblicazione: ")
            dir = input("Inserisci il direttore: ")
            nuova_rivista = Rivista(ttl, n, d, dir)
            self.elementi.append(nuova_rivista)
        elif tipo == "libro":
            ttl = input("Inserisci un titolo: ")
            a = input("Inserisci l'autore: ")
            d = input("Inserisci l'anno di pubblicazione: ")
            g = input("Inserisci il genere: ")
            nuovo_libro = Libro(ttl, a, d, g)
            self.elementi.append(nuovo_libro)
        else:
            print("Errore, assicurati di aver digitato 'libro' oppure 'rivista'.")

    def rimuovi_elemento(self, titolo):
        for elemento in self.elementi:
            if elemento.titolo == titolo:
                conferma = input(f"Sei sicuro di voler eliminare '{titolo}'? s/n: ").lower()
                if conferma == "s":
                    self.elementi.remove(elemento)
                    print(f"'{titolo}' eliminato dalla libreria.")
                return
        print(f"'{titolo}' non trovato.")

    def elenca(self):
        for elemento in self.elementi:
            tipo = "Libro" if isinstance(elemento, Libro) else "Rivista"
            print(f"[{tipo}] {elemento.__dict__}")

    def clear_all(self):
        conferma = input("Attenzione: così si rimuoveranno TUTTI i libri e TUTTE le riviste dalla libreria. Sei sicuro? s/n: ").lower()
        if conferma == "s":
            self.elementi.clear()
            print("Libreria ripristinata.")


libreria = Libreria()


libreria.aggiungi_elemento()
libreria.elenca()