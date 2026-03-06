import sys

data_file = "dati_inverno.txt"

# lettura di un file
def leggi_file(data_file):
    dati = []
    with open(data_file, "r") as f:
        for line in f:
            parti = line.strip().split(",")#ogni riga
            id_r, data_str, stazione, temp, umid, press, co2 = parti
            giorno, mese, anno = map(int, data_str.split("-"))
            #Conversione di tipo per dizionario
            dati.append({
                "id": int(id_r),
                "data": (giorno, mese, anno),
                "stazione": stazione,
                "temperatura": float(temp),
                "umidita": float(umid),
                "pressione": float(press),
                "co2": int(co2)
            })
    return dati


# creare un rapporto (yield)
def genera_report(dati, temp_soglia=5.0, co2_soglia=430):
    stazioni_dati = {}
    #sistemare ogni stazione come key
    for r in dati:
        s = r["stazione"]
        stazioni_dati.setdefault(s, []).append(r)
    #calcolare
    for s, rilevazioni in stazioni_dati.items():
        n_r = len(rilevazioni)

        temp_media = sum(r["temperatura"] for r in rilevazioni) / n_r
        temp_min = min(r["temperatura"] for r in rilevazioni)
        temp_max = max(r["temperatura"] for r in rilevazioni)

        umid_media = sum(r["umidita"] for r in rilevazioni) / n_r
        press_media = sum(r["pressione"] for r in rilevazioni) / n_r

        rilevazione_critica = max(rilevazioni, key=lambda r: r["co2"])
        co2_max = rilevazione_critica["co2"]
        giorno_critico = rilevazione_critica["data"]
        #se anomalie
        anomalie_temp = len([r for r in rilevazioni if r["temperatura"] > temp_soglia])
        anomalie_co2 = len([r for r in rilevazioni if r["co2"] > co2_soglia])
        #yield
        yield (
            f"Stazione {s}:\n"
            f"Numero rilevazioni={n_r}, Temp Media={temp_media:.1f}, "
            f"Temp Min={temp_min}, Temp Max={temp_max}\n"
            f"Umid Media={umid_media:.1f}, Press Media={press_media:.1f}, CO2 Max={co2_max}\n"
            f"Anomalie Temp>{temp_soglia}: {anomalie_temp}, "
            f"Anomalie CO2>{co2_soglia}: {anomalie_co2} "
            f"({'nessuna' if anomalie_co2 == 0 else 'presente'})\n"
            f"Giorno critico CO2: {giorno_critico}"
        )

#crea un rapporto file
def salva_report_su_file(nome_file_output, generatore):
    with open(nome_file_output, "w") as f:
        for blocco_report in generatore:
            print(blocco_report) # Stampa a console
            f.write(blocco_report + "\n") # Scrive su file
    print(f"Report salvato con successo in: {nome_file_output}")

#filtrare ogni settore
def filtra_per_stazione(dati):
    st = input("Stazione di rilevamento: ")
    filtrati = list(filter(lambda r: r["stazione"] == st, dati))
    for r in filtrati:
        print(r)
    return filtrati


def filtra_per_intervallo_temperatura(dati):
    t_min = float(input("Temperatura minima: "))
    t_max = float(input("Temperatura massima: "))
    filtrati = list(filter(lambda r: t_min <= r["temperatura"] <= t_max, dati))
    for r in filtrati:
        print(r)
    return filtrati


def filtra_per_intervallo_pressione(dati):
    p_min = float(input("Pressione minima: "))
    p_max = float(input("Pressione massima: "))
    filtrati = list(filter(lambda r: p_min <= r["pressione"] <= p_max, dati))
    for r in filtrati:
        print(r)
    return filtrati


def filtra_per_intervallo_co2(dati):
    c_min = int(input("CO2 minima: "))
    c_max = int(input("CO2 massima: "))
    filtrati = list(filter(lambda r: c_min <= r["co2"] <= c_max, dati))
    for r in filtrati:
        print(r)
    return filtrati


def filtra_per_data(dati):
    giorno = int(input("Giorno (DD): "))
    mese = int(input("Mese (MM): "))
    anno = int(input("Anno (YYYY): "))
    filtrati = list(filter(lambda r: r["data"] == (giorno, mese, anno), dati))
    for r in filtrati:
        print(r)
    return filtrati

#aggiungere i dati
def aggiungi_rilevazione(data_file):
    id_r = input("ID rilevazione: ")
    data = input("Data (DD-MM-YYYY): ")
    stazione = input("Stazione di rilevamento: ")
    temperatura = input("Temperatura: ")
    umidita = input("Umidità: ")
    pressione = input("Pressione: ")
    co2 = input("Concentrazione CO2: ")

    riga = f"{id_r},{data},{stazione},{temperatura},{umidita},{pressione},{co2}\n"

    with open(data_file, "a") as f:
        f.write(riga)

    print("Rilevazione aggiunta!")

#analizzare il giorno
def analisi_temporale(dati):
    # giorno con temperatura più alta
    max_temp = max(dati, key=lambda r: r["temperatura"])
    print(f"Giorno con temperatura più alta: {max_temp['data']} Temp={max_temp['temperatura']}")
    # giorno con maggiore CO2
    max_co2 = max(dati, key=lambda r: r["co2"])
    print(f"Giorno con maggiore CO2: {max_co2['data']} CO2={max_co2['co2']}")
    # stazione con maggiore variabilità termica
    stazioni = {}
    for r in dati:
        stazioni.setdefault(r["stazione"], []).append(r["temperatura"])

    variabilita = [(s, max(vals) - min(vals)) for s, vals in stazioni.items()]
    variabilita.sort(key=lambda x: x[1], reverse=True)

    print(f"Stazione con maggiore variabilità termica: {variabilita[0][0]} ΔT={variabilita[0][1]}")

#simulazione
def simulazione(dati):
    variazione = float(input("Variazione percentuale della temperatura (%): "))

    stazioni_dati = {}
    for r in dati:
        stazioni_dati.setdefault(r["stazione"], []).append(r)

    incremento_med = []

    for s, rilevazioni in stazioni_dati.items():
        media_orig = sum(r["temperatura"] for r in rilevazioni) / len(rilevazioni)
        temp_nuove = [r["temperatura"] * (1 + variazione / 100) for r in rilevazioni]
        media_nuova = sum(temp_nuove) / len(temp_nuove)
        incremento_med.append((s, media_nuova - media_orig))

    incremento_med.sort(key=lambda x: x[1], reverse=True)

    print("Incremento medio per stazione:")
    for s, inc in incremento_med:
        print(f"{s}: {inc:.2f}°C")

#Top
print("Esercitazione n. 1")
print("Analisi di dati sperimentali ambientali")


def menu():
    dati = leggi_file(data_file)

    while True:
        print("--- Menu ---")
        print("1. Visualizza report")
        print("2. Filtra dati")
        print("3. Analisi temporale")
        print("4. Aggiungi nuova rilevazione")
        print("5. Simulazione")
        print("6. Esci")

        scelta = input("Seleziona un'opzione (1-6): ")
        #1
        if scelta == "1":
            for riga in genera_report(dati):
                print(riga)

            #la scelta per creare un file
            user_input = input("Vorrei salvare questo report? y/n: ").lower()
            if user_input == "y":
                mio_generatore = genera_report(dati)
                salva_report_su_file("report_finale.txt", mio_generatore)
            elif user_input == "n":
                continue
            else:
                print("Opzione non valida.")
        #2
        elif scelta == "2":
            print("1. Per intervallo temperatura")
            print("2. Per intervallo pressione")
            print("3. Per intervallo CO2")
            print("4. Per data")
            print("5. Per stazione")

            tipo = input("Seleziona tipo di filtro (1-5): ")

            if tipo == "1":
                filtra_per_intervallo_temperatura(dati)
            elif tipo == "2":
                filtra_per_intervallo_pressione(dati)
            elif tipo == "3":
                filtra_per_intervallo_co2(dati)
            elif tipo == "4":
                filtra_per_data(dati)
            elif tipo == "5":
                filtra_per_stazione(dati)
        #3
        elif scelta == "3":
            analisi_temporale(dati)
        #4
        elif scelta == "4":
            aggiungi_rilevazione(data_file)
            dati = leggi_file(data_file)
        #5
        elif scelta == "5":
            simulazione(dati)
        #6
        elif scelta == "6":
            sys.exit()
      
        else:
            print("Opzione non valida.")

#escuzione        
menu()

        
