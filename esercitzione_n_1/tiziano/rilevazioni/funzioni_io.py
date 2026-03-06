def leggi_rilevazioni(file):
    """Legge un file .txt formattato da virgole e lo trasforma in una lista di rilevazioni."""

    rilevazioni = []
    with open(file, "r") as file:
        for riga in file:
            riga = riga.strip()
            if riga == "":
                continue
            riga = riga.split(",")

            data_split = riga[1].split("-")
            data_tupla = (int(data_split[0]), int(data_split[1]), int(data_split[2]))

            rilevazione = {
                "id_rilevazione": int(riga[0]),
                "data": data_tupla,
                "stazione_di_rilevamento": riga[2],
                "temperatura": float(riga[3]),
                "umidita": float(riga[4]),
                "pressione": float(riga[5]),
                "concentrazione_co2": float(riga[6]),

            }
            rilevazioni.append(rilevazione)

    return rilevazioni

def crea_lista_stazioni(rilevazioni):
    """Crea una lista di stazioni."""
    lista_stazioni = []
    # Controlla ogni rilevazione e salva ogni stazione unica nella lista
    for rilevazione in rilevazioni:
        stazione = rilevazione["stazione_di_rilevamento"]
        if stazione not in lista_stazioni:
            lista_stazioni.append(stazione)
    return lista_stazioni

def aggiungi_rilevazione(rilevazioni):
    """Aggiunge una rilevazione in append al file delle rilevazioni nella cartella corrente.
    L'id viene auto-incrementato rispetto all'ultimo presente."""
    id_rilevazione = rilevazioni[-1]["id_rilevazione"] + 1
    data = input("Inserisci la data in formato DD-MM-YYYY: ")
    stazione = input("Inserisci il nome della stazione: ")
    temperatura = float(input("Inserisci la temperatura: "))
    umidita = float(input("Inserisci l'umidità: "))
    pressione = float(input("Inserisci la pressione: "))
    co2 = float(input("Inserisci la concentrazione di CO2: "))

    try:
        with open("rilevazioni.txt", "a") as file:
            file.write(f"{id_rilevazione},{data},{stazione},{temperatura},{umidita},{pressione},{co2}\n")
        return True
    except (FileNotFoundError, PermissionError):
        return False
