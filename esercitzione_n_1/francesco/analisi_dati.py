from datetime import datetime

rivelazioni = "c:/Users/MYSELF/Downloads/python/analisi dati in python/rivelazioni.txt"

def create_struct():
    lista_rilevazioni = []

    try:
        with open(rivelazioni, "r", encoding="utf-8") as file:
            for riga in file:
                riga = riga.strip()

                if not riga:  
                    continue

                valori = riga.split(",")

                riv = {
                    "id": int(valori[0]),
                    "data": datetime.strptime(valori[1], "%d-%m-%y").date(),
                    "stazione": valori[2],
                    "temperatura": float(valori[3]),
                    "umidita": float(valori[4]),
                    "pressione": float(valori[5]),
                    "co2": float(valori[6])
                }

                lista_rilevazioni.append(riv)

        return lista_rilevazioni

    except FileNotFoundError:
        open(rivelazioni, "w", encoding="utf-8").close()
        return []


def stampa_riv(rilevazioni):
    print(f"{'ID':<3} {'Data':<10} {'Stazione':<10} {'Temp(°C)':<9} {'Umidità(%)':<11} {'Pressione':<10} {'CO2(ppm)':<9}")
    print("-"*65)
    for r in rilevazioni:
        print(f"{r['id']:<3} {r['data'].strftime('%d/%m/%y'):<10} {r['stazione']:<10} {r['temperatura']:<9.1f} {r['umidita']:<11.1f} {r['pressione']:<10.1f} {r['co2']:<9.1f}")
    print("")

def calc_md_st(rivelazioni: list, luogo):
    
    dati = []

    for r in rivelazioni:
        if r.get("stazione").lower() == luogo.lower():
            d = {
                            "temperatura": r['temperatura'],
                            "umidita": r['umidita'],
                            "pressione": r['pressione'],
                            "co2": r['co2']
                        }
            dati.append(d)

    risultato = {
                        "temp_media": sum(d["temperatura"] for d in dati) / len(dati),
                        "temp_min": min(d["temperatura"] for d in dati),
                        "temp_max": max(d["temperatura"] for d in dati),
                        "umidita_media": sum(d["umidita"] for d in dati) / len(dati),
                        "pressione_media": sum(d["pressione"] for d in dati) / len(dati),
                        "co2_max": max(d["co2"] for d in dati)
                    }

    return risultato

def stampa_mmd(mmd):

    print(f"TEMP. MEDIA(°C): {mmd['temp_media']}")
    print(f"TEMP. MIN(°C): {mmd['temp_min']}")
    print(f"TEMP. MAX(°C): {mmd['temp_max']}")
    print(f"UMIDITA MEDIA(%): {mmd['umidita_media']}")
    print(f"PRESSIONE MEDIA(hPa): {mmd['pressione_media']}")
    print(f"CO2 MAX(ppm): {mmd['co2_max']}")
    print("")

analisi = create_struct()
stampa_riv(analisi)

luogo = input('Inserisci il luogo della stazione di rilevamento: ')
mmd = calc_md_st(analisi,luogo)
stampa_mmd(mmd)

temp_lim = 22.0
co2_lim = 416.0

def anomalie(rivelazioni):

    anom_temp = []
    anom_co2 = []

    for r in rivelazioni:
        if r.get("temperatura") >= temp_lim:
            anom_temp.append(r)

    sorted(anom_temp,key = lambda x : (x["temperatura"] >= temp_lim), reverse=True)

    for r in rivelazioni:
        if r.get("co2") >= co2_lim:
            anom_co2.append(r)

    sorted(anom_temp,key = lambda x : (x["co2"] >= co2_lim), reverse=True)

    return anom_temp, anom_co2

stampa_riv(anomalie(analisi)[0])
stampa_riv(anomalie(analisi)[1])

print("Inserisci il tipo di filtraggio ('data','stazione','temp','pressione','co2'): ")
tipo = input()

def filtra(rivelazioni, tipo):

    risultati = []

    match tipo:

        case "data":
            data_inizio = datetime.strptime(input("Data inizio: "), "%d/%m/%y").date()
            data_fine = datetime.strptime(input("Data fine: "), "%d/%m/%y").date()

            for r in rivelazioni:
                data_r = r["data"]
                if data_inizio <= data_r <= data_fine:
                    risultati.append(r)

        case "stazione":
            st = input("Stazione: ")

            for r in rivelazioni:
                if r["stazione"].casefold() == st.casefold():
                    risultati.append(r)

        case "temp":
            tmin = float(input("Temp minima: "))
            tmax = float(input("Temp massima: "))

            for r in rivelazioni:
                if tmin <= r["temperatura"] <= tmax:
                    risultati.append(r)

        case "pressione":
            pmin = float(input("Pressione minima: "))
            pmax = float(input("Pressione massima: "))

            for r in rivelazioni:
                if pmin <= r["pressione"] <= pmax:
                    risultati.append(r)

        case "co2":
            cmin = float(input("CO2 minimo: "))
            cmax = float(input("CO2 massimo: "))

            for r in rivelazioni:
                if cmin <= r["co2"] <= cmax:
                    risultati.append(r)

        case _:
            print("Filtro non valido")

    return risultati

stampa_riv(filtra(analisi,tipo))

def analisi_temporale(rivelazioni):
    
        giorno_max_temp = max(rivelazioni, key=lambda r: r["temperatura"])["data"]
        giorno_max_co2 = max(rivelazioni, key=lambda r: r["co2"])["data"]

        stazioni = {}

        for r in rivelazioni:
            st = r["stazione"]
            temp = r["temperatura"]

            if st not in stazioni:
                stazioni[st] = {"min": temp, "max": temp}
            else:
                if temp < stazioni[st]["min"]:
                    stazioni[st]["min"] = temp
                if temp > stazioni[st]["max"]:
                    stazioni[st]["max"] = temp

        stazione_max = max(stazioni,key=lambda s: stazioni[s]["max"] - stazioni[s]["min"])

        print("Dalle analisi risulta che: ")
        print(f"il giorno piu' caldo è stato il {giorno_max_temp}")
        print(f"il giorno con piu' co2 è stato il {giorno_max_co2}")
        print(f"e la stazione\i di rilevamento con piu' varietà termica è\sono: {stazione_max}")
        print("")

analisi_temporale(analisi)

def report(rivelazioni):
    stazioni = {}

    anom_temp = anomalie(rivelazioni)[0]
    anom_co2 = anomalie(rivelazioni)[1]

    for r in rivelazioni:
        st = r["stazione"]
        temp = r["temperatura"]
        co2 = r["co2"]
        data = r["data"]

        if st not in stazioni:
            stazioni[st] = {
                "tot_rilevazioni": 0,
                "somma_temp": 0,
                "tot_anom_temp": 0,
                "tot_anom_co2": 0,
                "giorni_co2": {}
            }

        stazioni[st]["tot_rilevazioni"] += 1
        stazioni[st]["somma_temp"] += temp
    
        if r in anom_temp:
            stazioni[st]["tot_anom_temp"] += 1
        if r in anom_co2:
            stazioni[st]["tot_anom_co2"] += 1

        if data not in stazioni[st]["giorni_co2"]:
            stazioni[st]["giorni_co2"][data] = co2
        else:
            stazioni[st]["giorni_co2"][data] = max(stazioni[st]["giorni_co2"][data], co2)

    for st, dati in stazioni.items():
        media_temp = dati["somma_temp"] / dati["tot_rilevazioni"]
        giorno_critico = max(dati["giorni_co2"], key=lambda g: dati["giorni_co2"][g])
        co2_critico = dati["giorni_co2"][giorno_critico]

        yield f"--- Stazione: {st} ---"
        yield f"Totale rilevazioni: {dati['tot_rilevazioni']}"
        yield f"Temperatura media: {media_temp:.2f} °C"
        yield f"Totale anomalie temporali: {dati['tot_anom_temp']}"
        yield f"Totale anomalie CO2: {dati['tot_anom_co2']}"
        yield f"Giorno più critico (CO2 massima: {co2_critico}): {giorno_critico}"
        yield ""
 
with open("report.txt", "w") as file:
    file.write("REPORT RIVELAZIONI\n")
    file.write("=================\n\n")

    for data in report(analisi):
        print(data)
        file.write(data)
        file.write("\n")

def simulazione(rivelazioni):
    print("SIMULAZIONE\n")

    var_pr = float(input("Inserisci la variazione in percentuale della temperatura: "))

    stazioni = {}

    for r in rivelazioni:
        st = r["stazione"]
        temp = r["temperatura"]

        if st not in stazioni:
            stazioni[st] = {
                "tot_rilevazioni": 0,
                "original_sum_temp": 0,
                "new_sum_temp":0,
            }
        stazioni[st]["tot_rilevazioni"] += 1
        stazioni[st]["original_sum_temp"] += temp
        stazioni[st]["new_sum_temp"] += temp + (temp*var_pr)/100

    for st, dati in stazioni.items():
        original_md_temp = dati["original_sum_temp"]/dati["tot_rilevazioni"]
        dati["original_md_temp"] = original_md_temp
        new_md_temp = dati["new_sum_temp"]/dati["tot_rilevazioni"]
        dati["new_md_temp"] = new_md_temp
        incremento = new_md_temp - original_md_temp
        dati["incremento"] = incremento


    stazioni_ordinate = sorted(stazioni.items(),key= lambda x: x[1]["new_md_temp"], reverse=True)

    print("\nRisultato:\n")
    print(f"{'Stazione':<15}{'Originale °C':>15}{'Nuova °C':>15}{'Incremento':>15}")
    print("="*60)

    for st, dati in stazioni_ordinate:
        print(
            f"{st:<15}"
            f"{dati['original_md_temp']:>15.2f}"
            f"{dati['new_md_temp']:>15.2f}"
            f"{dati['incremento']:>15.2f}"
        )

simulazione(analisi)
