##Termini che non conosco
##Lexer (Analizzatore lessicale): Dividere in unità minime di significato. Queste parole sono chiamate token.
##Parser (Analizzatore sintattico): Verificare se l'ordine dei token è corretto.
##token: È il testo della parola cosi com'è. ["il", "maestro", "ha"]
##terminal: È il simbolo grammaticale che rappresenta il significato ola parte del discorso. ["il", "maestro", "ha"] == [ARTICOLO, SOSTANTIVO, VERBO]

import sys

#creare tokens
class Lexer:
    
    def __init__(self):
        # Definizione dei simboli terminali T
        self.vocabulary = {
            "il": "ARTICOLO",
            "un": "ARTICOLO",
            "ha": "VERBO",
            "maestro": "SOSTANTIVO",
            "padawan": "SOSTANTIVO"
        }

    def tokenize(self, text):
        # Divide per spazi e tokenizza ogni parola
        words = text.strip().split()
        tokens = []
        for word in words:
            # Converte in minuscolo per il confronto
            token_type = self.vocabulary.get(word.lower())
            if token_type:
                tokens.append((token_type, word))
            else:
                # Errore se la parola non esiste nel linguaggio Lsw
                raise ValueError(f"Errore Lessicale: '{word}' non appartiene al linguaggio Lsw.")
        return tokens

#verificare l'ordine dei token
class Parser:
    
    def __init__(self):
        self.tokens = []
        self.index = 0
        self.current_token = None

    #_ : def per solo questo class
    #passaggio al prossimo
    def _advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    #verifica e conferma
    def _match(self, expected_type):
        if self.current_token and self.current_token[0] == expected_type:
            self._advance()
        else:
            actual = self.current_token[0] if self.current_token else "FINE_FILE"
            raise SyntaxError(f"Atteso {expected_type}, ma trovato {actual}.")

    #direttore dell'analisi
    def parse(self, tokens):
        """
        Punto di ingresso principale per l'analisi
        """
        self.tokens = tokens
        self.index = 0
        if not self.tokens:
            return False
        
        self.current_token = self.tokens[0]
        
        try:
            # g: <frase> ::= <soggetto> <gruppo_verbale>
            self._parse_soggetto()
            self._parse_gruppo_verbale()
            
            # Verifica che non ci siano token residui dopo la fine della frase
            if self.current_token is not None:
                raise SyntaxError("La struttura della frase non termina correttamente (parole in eccesso).")
            return True
        except SyntaxError as e:
            raise e

    #regola del soggetto, usa _match
    def _parse_soggetto(self):
        self._match("ARTICOLO")
        self._match("SOSTANTIVO")

    #regola del predicato, usa _match
    def _parse_gruppo_verbale(self):
        self._match("VERBO")
        self._parse_oggetto()

    #regola del pggetto, usa _match
    def _parse_oggetto(self):
        self._match("ARTICOLO")
        self._match("SOSTANTIVO")

#coordinatore generale
class LswRecognizer:

    def __init__(self, mode='a'):
        self.lexer = Lexer()
        self.parser = Parser()
        self.mode = mode  # 'a': continua analisi, 'b': interrompe al primo errore

    #esecuzione dell'analisi sul file
    def process_file(self, filename):
        print(f"--- Inizio Analisi: {filename} (Modalità: {self.mode}) ---")
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    content = line.strip()
                    if not content:
                        continue
                    
                    try:
                        # 1. Analisi lessicale
                        tokens = self.lexer.tokenize(content)
                        # 2. Analisi sintattica
                        self.parser.parse(tokens)
                        print(f"[Riga {line_num}] OK: {content}")
                    
                    except (ValueError, SyntaxError) as e:
                        print(f"[Riga {line_num}] ERRORE: {content}")
                        print(f"    Dettagli: {e}")
                        if self.mode == 'b':
                            print("!!! Analisi interrotta a causa della modalità 'b'.")
                            return
        except FileNotFoundError:
            print(f"Errore: Il file '{filename}' non è stato trovato.")


def main():
    #creazione del file di input per il test (include i pattern richiesti)
    filename = "input_lsw.txt"
     
    #avvio del riconoscitore
    # Modalità 'a': analizza tutto e mostra i log degli errori
    # Modalità 'b': si ferma alla prima riga non valida
    recognizer = LswRecognizer(mode='a')
    recognizer.process_file(filename)

if __name__ == "__main__":
    main()

        


