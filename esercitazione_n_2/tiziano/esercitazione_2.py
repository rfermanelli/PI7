class ErroreLessicale(Exception):
    pass

class ErroreSintattico(Exception):
    pass

class Lexer:

    def __init__(self):
        self.dizionario = {
            "il": "ARTICOLO",
            "un": "ARTICOLO",
            "ha": "VERBO",
            "padawan": "SOSTANTIVO",
            "maestro": "SOSTANTIVO"
        }

    def analisi_lessicale(self, frase:list):
        analisi = []
        for parola in frase:
            parola = parola.lower()
            try:
                analisi.append((self.dizionario[parola], parola))
            except KeyError:
                raise ErroreLessicale(f"Token sconosciuto: {parola}")
        return analisi


class Parser:

    def analizza_soggetto_oggetto(self, token: list):
        return {"ARTICOLO": token[0][1], "SOSTANTIVO": token[1][1]}

    def analizza_gruppo_verbale(self, token: list):
        verbo = token[0][1]
        oggetto = self.analizza_soggetto_oggetto(token[1:])
        return {"VERBO": verbo, "OGGETTO": oggetto}

    def analizza_frase(self, token: list):
        soggetto = self.analizza_soggetto_oggetto(token[:2])
        gruppo_verbale = self.analizza_gruppo_verbale(token[2:])
        return {"SOGGETTO": soggetto, "GRUPPO_VERBALE": gruppo_verbale}


    def analisi_sintattica(self, analisi: list):
        struttura = ["ARTICOLO", "SOSTANTIVO", "VERBO", "ARTICOLO", "SOSTANTIVO"]

        if len(analisi) != 5:
            raise ErroreSintattico(f"Numero di token non valido: attesi 5, ricevuti {len(analisi)}")

        for i, (desc, parola) in enumerate(analisi):
            if desc != struttura[i]:
                raise ErroreSintattico(f"Token non valido alla posizione {i + 1}: atteso {struttura[i]}, trovato {desc} ('{parola}')")

        albero = {
            "FRASE": self.analizza_frase(analisi)
        }
        return albero

class Riconoscitore:

    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()

    def main(self, is_logging: bool = True):

        frasi_da_analizzare = []
        log = []
        with open("./testo.txt", "r") as file:
            for riga in file:
                riga = riga.strip()
                riga = riga.split()
                frasi_da_analizzare.append(riga)

        if is_logging:
            for i, frase in enumerate(frasi_da_analizzare):
                try:
                    analisi = self.lexer.analisi_lessicale(frase)
                    self.parser.analisi_sintattica(analisi)
                except (ErroreLessicale, ErroreSintattico) as e:
                    frase_errata = " ".join(frase)
                    log.append(f"{type(e).__name__} alla riga {i + 1}: {frase_errata} | {e}\n")

            with open("./log.txt", "w", encoding="utf-8") as log_file:
                if log:
                    log_file.writelines(log)
                else:
                    log_file.write("Nessun errore riscontrato.")
        else:
            for i, frase in enumerate(frasi_da_analizzare):
                try:
                    analisi = self.lexer.analisi_lessicale(frase)
                    self.parser.analisi_sintattica(analisi)
                except (ErroreLessicale, ErroreSintattico) as e:
                    frase_errata = " ".join(frase)
                    raise Exception(f"Errore alla riga {i + 1}: {frase_errata} | {type(e).__name__}: {e}")


rick = Riconoscitore()
rick.main()