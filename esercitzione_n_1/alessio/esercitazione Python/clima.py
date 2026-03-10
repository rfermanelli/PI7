# caricamento file cartella dati
def carica_dati(nome_file):
    dati = []

    with open(nome_file, "r") as file:
        for riga in file:
            riga = riga.strip()
            if riga == "":
                continue

            # trasformo la riga di testo in una lista di stringhe
            parti = riga.split(",")
            id_ril = int(parti[0])
            # separo i componenti della data
            g, m, a = parti[1].split("-") 
            # tupla (DD, MM, YYYY)
            data = (int(g), int(m), int(a))
            stazione = parti[2]
            temperatura = float(parti[3])
            umidita = float(parti[4])
            pressione = float(parti[5])
            co2 = float(parti[6])

            # dizionario
            rilevazione = { 
                "id": id_ril,
                "data": data,
                "stazione": stazione,
                "temperatura": temperatura,
                "umidita": umidita,
                "pressione": pressione,
                "co2": co2
            }
            dati.append(rilevazione) # lista finale

    return dati

# media
def media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def lista_stazioni(dati):
    stazioni = []
    for r in dati:
        if r["stazione"] not in stazioni:
            stazioni.append(r["stazione"])
    return stazioni

# dati stazione
def dati_stazione(dati, nome):
    risultato = []
    for r in dati:
        if r["stazione"] == nome:
            risultato.append(r)
    return risultato

# filtro intervallo date
def filtro_date(dati, data_inizio, data_fine):
    risultato = []
    for r in dati:
        if data_inizio <= r["data"] <= data_fine:
            risultato.append(r)
    return risultato

# filtro stazioni
def analisi_stazioni(dati):
    stazioni = lista_stazioni(dati)
    risultati = {}

    for s in stazioni:
        ds = dati_stazione(dati, s)
        temperature = []
        umidita = []
        pressione = []
        co2 = []
        for r in ds:
            temperature.append(r["temperatura"])
            umidita.append(r["umidita"])
            pressione.append(r["pressione"])
            co2.append(r["co2"])

        risultati[s] = {
            "temp_media": media(temperature),
            "temp_min": min(temperature),
            "temp_max": max(temperature),
            "umidita_media": media(umidita),
            "pressione_media": media(pressione),
            "co2_max": max(co2)
        }

    return risultati

# anomalie
def rileva_anomalie(dati, soglia_temp, soglia_co2):
    anomalie = []

    for r in dati:
        gravita = 0
        if r["temperatura"] > soglia_temp:
            gravita += r["temperatura"] - soglia_temp
        if r["co2"] > soglia_co2:
            gravita += r["co2"] - soglia_co2
        if gravita > 0:
            nuovo = r.copy()
            nuovo["gravita"] = gravita
            anomalie.append(nuovo)

    # lamba = ordinare i dizionari guardando solo il valore gravita
    anomalie.sort(key=lambda x: x["gravita"], reverse=True)
    return anomalie

# filtro tempo
def analisi_temporale(dati):
    # lamba = serve per trovare il num piu alto  su tutta la riga del dizionario che contiene quel numero
    giorno_temp_max = max(dati, key=lambda r: r["temperatura"])
    giorno_co2_max = max(dati, key=lambda r: r["co2"])
    stazioni = lista_stazioni(dati)

    variabilita = []
    for s in stazioni:
        ds = dati_stazione(dati, s)
        temperature = []
        for r in ds:
            temperature.append(r["temperatura"])
        var = max(temperature) - min(temperature)
        variabilita.append((s, var))
    stazione_var = max(variabilita, key=lambda x: x[1])
    return giorno_temp_max, giorno_co2_max, stazione_var

# creazione report
def genera_report(dati, soglia_temp, soglia_co2):
    stazioni = lista_stazioni(dati)

    for s in stazioni:
        ds = dati_stazione(dati, s)
        num = len(ds)

        temperature = [r["temperatura"] for r in ds]
        media_temp = media(temperature)

        anomalie_temp = sum(1 for r in ds if r["temperatura"] > soglia_temp)
        anomalie_co2 = sum(1 for r in ds if r["co2"] > soglia_co2)

        giorno_critico = max(ds, key=lambda r: r["co2"])

        testo = ""
        testo += f"STAZIONE: {s}\n"
        testo += f"Numero rilevazioni: {num}\n"
        testo += f"Media temperatura: {media_temp:.2f}\n"
        testo += f"Anomalie temperatura: {anomalie_temp}\n"
        testo += f"Anomalie CO2: {anomalie_co2}\n"
        testo += f"Giorno CO2 massimo: {giorno_critico['data']}\n"
        testo += "\n"
        yield testo

# salvataggio report
def crea_file_report(nome_file, generatore):
    file = open(nome_file, "w")
    for riga in generatore:
        print(riga)
        file.write(riga)
    file.close()
            
# simulazione temperatura
def simulazione_temperatura(dati, percentuale):
    stazioni = lista_stazioni(dati)
    risultati = []

    for s in stazioni:
        ds = dati_stazione(dati, s)
        temperature = [r["temperatura"] for r in ds]
        media_originale = media(temperature)
        nuove = list(map(lambda t: t * (1 + percentuale / 100), temperature))
        nuova_media = media(nuove)
        incremento = nuova_media - media_originale
        risultati.append((s, incremento))
    risultati.sort(key=lambda x: x[1], reverse=True)
    return risultati

# menu / filtri / stampa
def menu():
    print("Login UTENTE")
    print("Seleziona Opzione Analisi:")
    dati = carica_dati("dati.txt")
    dati_filtrati = dati
    stazioni_disponibili = lista_stazioni(dati)

    while True:
        print("\n1 Filtra per date")
        print("2 Filtra per stazioni")
        print("3 Filtra per temperatura")
        print("4 Filtra per CO2")
        print("5 Analisi stazioni")
        print("6 Analisi anomalie e simulazione temperatura")
        print("7 Analisi temporale")
        print("8 Genera report")
        print("0 Esci")
        scelta = input("Scelta: ")

        if scelta == "1":
            print("INTERVALLO DATE")
            g = int(input("Giorno inizio: "))
            m = int(input("Mese inizio: "))
            a = int(input("Anno inizio: "))
            data_inizio = (g, m, a)

            g = int(input("Giorno fine: "))
            m = int(input("Mese fine: "))
            a = int(input("Anno fine: "))
            data_fine = (g, m, a)

            dati_filtrati = filtro_date(dati_filtrati, data_inizio, data_fine)
            print(f"\nRILEVAZIONI PER DATE")
            for r in dati_filtrati:
                print(f"ID: {r['id']}, Data: {r['data']}, Stazione: {r['stazione']}, "
                      f"Temp: {r['temperatura']}°C, Umidità: {r['umidita']}%, "
                      f"Pressione: {r['pressione']} hPa, CO2: {r['co2']} ppm")

        elif scelta == "2":
            print("Stazioni disponibili:", stazioni_disponibili)
            scelta_stazione = input("Inserisci nome stazione: ")
            dati_filtrati = [r for r in dati_filtrati if r["stazione"] == scelta_stazione]
            print(f"\nRILEVAZIONI PER STAZIONE {scelta_stazione}")
            for r in dati_filtrati:
                print(f"ID: {r['id']}, Data: {r['data']}, Stazione: {r['stazione']}, "
                      f"Temp: {r['temperatura']}°C, Umidità: {r['umidita']}%, "
                      f"Pressione: {r['pressione']} hPa, CO2: {r['co2']} ppm")

        elif scelta == "3":
            t_min = float(input("Temperatura minima: "))
            t_max = float(input("Temperatura massima: "))
            dati_filtrati = [r for r in dati_filtrati if t_min <= r["temperatura"] <= t_max]
            print(f"\nRILEVAZIONI PER TEMPERATURA {t_min}-{t_max}°C")
            for r in dati_filtrati:
                print(f"ID: {r['id']}, Data: {r['data']}, Stazione: {r['stazione']}, "
                      f"Temp: {r['temperatura']}°C, Umidità: {r['umidita']}%, "
                      f"Pressione: {r['pressione']} hPa, CO2: {r['co2']} ppm")

        elif scelta == "4":
            co2_min = float(input("CO2 minima: "))
            co2_max = float(input("CO2 massima: "))
            dati_filtrati = [r for r in dati_filtrati if co2_min <= r["co2"] <= co2_max]
            print(f"\nRILEVAZIONI PER CO2 {co2_min}-{co2_max} ppm")
            for r in dati_filtrati:
                print(f"ID: {r['id']}, Data: {r['data']}, Stazione: {r['stazione']}, "
                      f"Temp: {r['temperatura']}°C, Umidità: {r['umidita']}%, "
                      f"Pressione: {r['pressione']} hPa, CO2: {r['co2']} ppm")

        elif scelta == "5":
            risultato = analisi_stazioni(dati_filtrati)
            for s in risultato:
                print("\nStazione:", s)
                for k in risultato[s]:
                    print(k, ":", risultato[s][k])

        elif scelta == "6":
            soglia_temp = float(input("Soglia temperatura: "))
            soglia_co2 = float(input("Soglia CO2: "))
            percentuale = float(input("Percentuale variazione temperatura: "))

            anomalie = rileva_anomalie(dati_filtrati, soglia_temp, soglia_co2)
            print("\nANOMALIE RILEVATE")
            for a in anomalie:
                print(f"ID: {a['id']}, Data: {a['data']}, Stazione: {a['stazione']}, "
                      f"Temp: {a['temperatura']}°C, CO2: {a['co2']}, Gravità: {a['gravita']}")

            risultati = simulazione_temperatura(dati_filtrati, percentuale)
            print("\nSIMULAZIONE VARIAZIONE TEMPERATURA")
            for r in risultati:
                print(f"Stazione: {r[0]}, Incremento medio temperatura: {r[1]:.2f}°C")

        elif scelta == "7":
            tmax, co2max, var = analisi_temporale(dati_filtrati)
            print("Giorno temperatura max:", tmax)
            print("Giorno CO2 max:", co2max)
            print("Stazione variabilità termica:", var)

        elif scelta == "8":
            soglia_temp = float(input("Soglia temperatura: "))
            soglia_co2 = float(input("Soglia CO2: "))
            gen = genera_report(dati_filtrati, soglia_temp, soglia_co2)
            crea_file_report("report.txt", gen)

        elif scelta == "0":
            break

# avvio 
if __name__ == "__main__":
    menu()