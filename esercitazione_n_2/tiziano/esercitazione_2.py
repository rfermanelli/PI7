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

    def analisi_lessicale(self, frase: list):
        analisi = []
        for parola in frase:
            parola = parola.lower()
            try:
                # Ogni parola viene mappata alla sua categoria e aggiunta come tupla (categoria, parola)
                analisi.append((self.dizionario[parola], parola))
            except KeyError:
                # Se la parola non è nel dizionario, non appartiene al lessico del linguaggio
                raise ErroreLessicale(f"Token sconosciuto: {parola}")
        return analisi


class Parser:

    def analizza_soggetto_oggetto(self, token: list):
        # Soggetto e oggetto hanno la stessa struttura <articolo> <sostantivo>
        # token[0] è la tupla dell'articolo, token[1] è la tupla del sostantivo
        # [1] estrae il valore dalla tupla, es. ("ARTICOLO", "il")[1] → "il"
        return {"ARTICOLO": token[0][1], "SOSTANTIVO": token[1][1]}

    def analizza_gruppo_verbale(self, token: list):
        # <verbo> <oggetto>
        # token[0] è il verbo, il resto della lista costituisce l'oggetto
        verbo = token[0][1]
        oggetto = self.analizza_soggetto_oggetto(token[1:])
        return {"VERBO": verbo, "OGGETTO": oggetto}

    def analizza_frase(self, token: list):
        # <frase> = <soggetto> + <gruppo_verbale>
        # I primi due token formano il soggetto, i restanti tre il gruppo verbale
        soggetto = self.analizza_soggetto_oggetto(token[:2])
        gruppo_verbale = self.analizza_gruppo_verbale(token[2:])
        return {"SOGGETTO": soggetto, "GRUPPO_VERBALE": gruppo_verbale}

    def analisi_sintattica(self, analisi: list):
        # La grammatica impone esattamente 5 token:
        struttura = ["ARTICOLO", "SOSTANTIVO", "VERBO", "ARTICOLO", "SOSTANTIVO"]

        if len(analisi) != len(struttura):
            raise ErroreSintattico(f"Numero di token non valido: attesi {len(struttura)}, ricevuti {len(analisi)}")

        # Verifica che ogni token sia nella categoria attesa dalla grammatica
        for i, (desc, parola) in enumerate(analisi):
            if desc != struttura[i]:
                raise ErroreSintattico(f"Token non valido alla posizione {i + 1}: atteso {struttura[i]}, trovato {desc} ('{parola}')")

        # Se la verifica è passata, costruisce l'albero sintattico come dizionario innestato
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
                # Ogni riga viene trasformata in lista di parole per il lexer
                riga = riga.split()
                frasi_da_analizzare.append(riga)

        for i, frase in enumerate(frasi_da_analizzare):
            try:
                analisi = self.lexer.analisi_lessicale(frase)
                albero = self.parser.analisi_sintattica(analisi)
                print(f"ANALISI: {analisi}\n"
                      f"ALBERO: {albero}\n"
                      f"{'-' * 150}\n")


            except (ErroreLessicale, ErroreSintattico) as e:
                frase_errata = " ".join(frase)
                if not is_logging:
                    # Soluzione b: interrompe al primo errore
                    raise Exception(f"Errore alla riga {i + 1}: {frase_errata} | {type(e).__name__}: {e}")
                # Soluzione a: accumula gli errori nel log e continua
                log.append(f"{type(e).__name__} alla riga {i + 1}: {frase_errata} | {e}\n")

        with open("./log.txt", "w", encoding="utf-8") as log_file:
            if log:
                log_file.writelines(log)
            else:
                log_file.write("Nessun errore riscontrato.")


rick = Riconoscitore()
rick.main()