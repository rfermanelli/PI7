class Camera:

    TIPI_VALIDI = ["Singola", "Doppia", "Suite"]

    def __init__(self, numero, tipo, occupata: bool):
        self.numero = numero
        if tipo not in self.TIPI_VALIDI:
            raise ValueError(f"Errore: tipo della stanza non valido. Deve essere uno dei seguenti: {self.TIPI_VALIDI}")
        self.tipo = tipo
        self.occupata = occupata

class Prenotazione:

    def __init__(self, nome_cognome, durata_soggiorno, stanza):
        self.nome = nome_cognome
        self.durata_soggiorno = durata_soggiorno
        self.stanza = stanza

class Hotel:

    def __init__(self):
        self.camere = []
        self.prenotazioni = []

    def aggiungi_camera(self):
        numero = input("Inserisci il numero della camera: ")
        tipo = input("Inserisci il tipo della camera: Singola/Doppia/Suite").title()
        occupata = input("La stanza è occupata? Si/No").lower()
        occupata = True if occupata == "si" else False
        nuova_camera = Camera(numero=numero, tipo=tipo, occupata=occupata)
        self.camere.append(nuova_camera)
        print(f"Camera {numero} aggiunta con successo.")

    def aggiungi_prenotazione(self):
        nome_cognome = input("Inserisci il nome e il cognome di chi vuole prenotare: ")
        durata_soggiorno = input("Per quanti giorni dovrà pernottare?: ")
        print("NUMERO | TIPO | STATO")
        for camera in self.camere:
            stato = "Occupata" if camera.occupata else "Libera"
            print(f"{camera.numero} | {camera.tipo} | {stato}")
        camera_scelta = input("Per favore inserisci il numero della camera da occupare: ")

        camera_trovata = None
        for camera in self.camere:
            if camera.numero == camera_scelta:
                camera_trovata = camera
                break
            else:
                print("Errore, camera inesistente.")

        if camera_trovata is None:
            print("Errore: camera inesistente.")
            return
        elif not camera_trovata.occupata:
            prenotazione = Prenotazione(nome_cognome, durata_soggiorno, camera_trovata)
            camera_trovata.occupata = True
            self.prenotazioni.append(prenotazione)
            print(f"Prenotazione confermata per {nome_cognome} nella camera {camera_scelta}.")
        else:
            print("Errore, la camera scelta risulta essere occupata.")

