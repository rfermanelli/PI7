   #analisi dati ambientali
   #carica dati
   
def carica_dati(rilevazionedati):

    dati = []

    with open("rilevazionedati.txt", "r") as file:
         for _ in range(4):
             next(file)

         for riga in file: 
            riga = riga.strip()
            if riga == "":   # salta righe vuote
                continue
            elemento = riga.split(",")

            id_rilevazione = int(elemento[0])
            giorno, mese, anno = map(int, elemento[1].split("-"))
            data = (giorno, mese, anno)
            stazione = elemento[2]
            temperatura = float(elemento[3])
            umidita = float(elemento[4])
            pressione = float(elemento[5])
            co2 = float(elemento[6])

            rilevazione = {
                "id": id_rilevazione,
                "data": data,
                "stazione": stazione,
                "temperatura": temperatura,
                "umidita": umidita,
                "pressione": pressione,
                "co2": co2
            }

            dati.append(rilevazione)

    return dati


def stampa_dati(dati):

    print("\n--- TUTTE LE RILEVAZIONI ---\n")

    for r in dati:

        giorno, mese, anno = r["data"]
 
        a = f'''ID:{r["id"]} 
            Data:{giorno}-{mese}-{anno} 
            Stazione:{r["stazione"]}  
            Temp:{r["temperatura"]}°C  
            Umidità:{r["umidita"]}%  
            Pressione:{r["pressione"]} hPa  
            CO2:{r["co2"]} ppm'''
        print(a)
    


 # analisi descrittiva 

def stazione_dati(analisidati):
    risultati = {}


    for r in analisidati:
        nome = r["stazione"]
        if nome not in risultati:
                risultati[nome] = {
                "temperature": [],
                "umidita": [],
                "pressione": [],
                "co2": []
            }
        risultati[nome]["temperature"].append(r["temperatura"])
        risultati[nome]["umidita"].append(r["umidita"])
        risultati[nome]["pressione"].append(r["pressione"])
        risultati[nome]["co2"].append(r["co2"])

        

    for nome, lista in risultati.items():
        temp_media = sum(x["temperatura"] for x in lista) / len(lista)
        temp_min = min(x["temperatura"] for x in lista)
        temp_max = max(x["temperatura"] for x in lista)
        umi_media = sum(x["umidita"] for x in lista) / len(lista)
        pres_media = sum(x["pressione"] for x in lista) / len(lista)
        co2_max = max(x["co2"] for x in lista)



        risultati[nome] = {
            "media_temp": temp_media,
            "min_temp": temp_min,
            "max_temp": temp_max,
            "umi_media" : umi_media,
            "pres_media" : pres_media,
            "co2_max" : co2_max
        }

        
        print(f"\nStazione: {nome}")
        print(f"Temperatura media: {temp_media:.2f} °C")
        print(f"Temperatura minima: {temp_min} °C")
        print(f"Temperatura massima: {temp_max} °C")
        print(f"Umidità media: {umi_media:.2f} %")
        print(f"Pressione media: {pres_media:.2f} hPa")
        print(f"CO2 massima: {co2_max} ppm")       
    

# rilevamento di anomalie

def rileva_anomalie(dati, soglia_temp, soglia_co2):
    SOGLIA_TEMP: int = 30
    SOGLIA_CO2: int = 400

    anomalie=[]

    for r in dati:
        if r["temperatura"] > soglia_temp:
            anomalie.append(r)
        if r["co2"] > soglia_co2:
            anomalie.append(r)

    anomalie_ordinate = sorted(anomalie, key = lambda r: r["temperatura"],
    reverse = True
    )
    anomalie_ordinate = sorted(anomalie_ordinate, key = lambda r: r["co2"], reverse = True)

    return anomalie_ordinate


# filtri dinamici
dati = carica_dati("rilevazionedati")
miei_dati = dati

def filtro_temperatura(dati, min_temp, max_temp):
    range_T = list(filter(lambda r: min_temp <= r["temperatura"] <= max_temp,dati))
    return stampa_dati(range_T)

def filtro_co2(dati, min_co2, max_co2):
    range_co2 = list(filter(lambda r: min_co2 <= r["co2"] <= max_co2,dati))
    return(stampa_dati(range_co2))

def filtro_pressione(dati, min_pres, max_pres):
    range_P = list(filter(lambda r:  min_pres <= r["pressione"] <= max_pres, dati))
    return(stampa_dati(range_P))

def filtro_date(dati, data_inizio, data_fine):
    data_inizio = (1, 1, 2025)
    data_fine = (10, 4, 2025)
    range_d = list(filter(lambda r: data_inizio <= r["data"] <= data_fine, dati))
    return(stampa_dati(range_d))

def filtro_stazione(dati, stazione):
    range_s = list(filter(lambda r: r["stazione"] == stazione, dati))
    return(stampa_dati(range_s))

    

# analisi temporale

def giorno_temperatura_max(dati):
    max_t = max(dati, key = lambda r: r["temperatura"])
    return max_t["data"]

def giorno_co2_max(dati):
    max_c = max(dati, key=lambda x: x["co2"])
    return max_c["data"]

def stazione_variabilita_termica_max(dati):
    stazioni = {}

    for r in dati:
        nome = r["stazione"]
        if nome not in stazioni:
            stazioni[nome] = []
            stazioni[nome].append(r["temperatura"])
    max_var = 0
    st_max = None

    for nome, temp in stazioni.items():
        var = max(temp) - min (temp)
        if var > max_var:
            max_var = var
            st_max = nome
    return st_max



# genera report

def genera_report(dati, soglia_temp, soglia_co2):
    stazioni={}

    for r in dati:
        nome = r["stazione"]
        if nome not in stazioni:
            stazioni[nome]=[]
            stazioni[nome].append(r)

    for nome, lista in stazioni.items():
        totale=len(lista)
        media_temp= sum(x["temperatura"]for x in lista) / totale
        anomalie_temp= len(list(filter(lambda x:x["temperatura"]> soglia_temp, lista))) / totale
        giorno_co2_max= max(lista, key = lambda x: x["co2"])["data"]

        yield f"stazione: {nome}"
        yield f"totale rilevazioni: {totale}"
        yield f"media temperatura: {media_temp}"
        yield f"anomalie temperatura: {anomalie_temp}"
        yield f"anomalie co2: {giorno_co2_max}"
        yield "-" * len(f"Stazione: {nome}")

        with open("report.txt", "w") as file:
            for riga in genera_report(dati):
             file.write(riga + "\n")

def stampa_report(dati, soglia_temp, soglia_co2):

    print("\n--- REPORT ---\n")

    for riga in genera_report(dati, soglia_temp, soglia_co2):
        print(riga)



# simulazioni

def simulazione_variazione(dati, var_percentuale):
    medie_originali = {}
    medie_nuove = {}
    
    for r in dati:
        stazione = r["stazione"]
        if stazione not in medie_originali:
            medie_originali[stazione] = []
            medie_nuove[stazione] = []
        medie_originali[stazione].append(r["temperatura"])
        nuova_temp = r["temperatura"] * (1 + var_percentuale / 100)
        medie_nuove[stazione].append(nuova_temp)
    
    risultati = []
    for stazione in medie_originali:
        media_orig = sum(medie_originali[stazione]) / len(medie_originali[stazione])
        media_nuova = sum(medie_nuove[stazione]) / len(medie_nuove[stazione])
        incremento = media_nuova - media_orig
        risultati.append((stazione, incremento))
    
    risultati.sort(key=lambda x: x[1], reverse=True)
    
    return risultati


menu = """
0 - esc
1 - Calcolo descrittivo per stazione di rilevamento
2 - Rilevamento di anomalie
3 - Filtro per intervallo di date
4 - Filtro per stazione di rilevamento
5 - Filtro per intervallo di Temperature
6 - Filtro per intervallo di pressioni
7 - Filtro per intervallo di concentrazioni di CO2
8 - Calcolo giorno con la temperatura più alta
9 - Calcolo giorno con maggiore concentrazione di CO2
10 - Stazione con la maggiore variabilità termica
11 - Report strutturato per stazione di rilevamento
12 - Funzione di simulazione
"""

def main():
    rilevazionedati = input("rilevazionidati.txt")
    dati = carica_dati("rilevazionedati.txt")
    scelta = - 1
    while scelta != 0:

        print(menu)
        scelta = int(input("Scegli un valore: "))

        if scelta == 1:
            stazione_dati(dati)

        elif scelta == 2:
            soglia_temp = float(input("Inserisci soglia temperatura: "))
            soglia_co2 = float(input("Inserisci soglia CO2: "))
            anomalie = rileva_anomalie(dati, soglia_temp, soglia_co2)
            stampa_dati(anomalie)

        elif scelta == 3:
            print("Filtro per intervallo di date")

            g1 = int(input("Giorno inizio: "))
            m1 = int(input("Mese inizio: "))
            a1 = int(input("Anno inizio: "))

            g2 = int(input("Giorno fine: "))
            m2 = int(input("Mese fine: "))
            a2 = int(input("Anno fine: "))

            data_inizio = (g1, m1, a1)
            data_fine = (g2, m2, a2)

            risultati = filtro_date(dati, data_inizio, data_fine)

            stampa_dati(risultati)

        elif scelta == 4:
            stazione = input("Inserisci nome stazione: ")

            risultati = filtro_stazione(dati, stazione)

            stampa_dati(risultati)

        elif scelta == 5:
            min_temp = float(input("Temperatura minima: "))
            max_temp = float(input("Temperatura massima: "))

            risultati = filtro_temperatura(dati, min_temp, max_temp)

            stampa_dati(risultati)

        elif scelta == 6:

            min_pres = float(input("Pressione minima: "))
            max_pres = float(input("Pressione massima: "))

            risultati = filtro_pressione(dati, min_pres, max_pres)

            stampa_dati(risultati)

        elif scelta == 7:

            min_co2 = float(input("CO2 minima: "))
            max_co2 = float(input("CO2 massima: "))

            risultati = filtro_co2(dati, min_co2, max_co2)

            stampa_dati(risultati)

        elif scelta == 8:
            giorno = giorno_temperatura_max(dati)

            print("Giorno con temperatura più alta:", giorno)

        elif scelta == 9:
            giorno = giorno_co2_max(dati)

            print("Giorno con CO2 più alta:", giorno)

        elif scelta == 10:
            stazione = stazione_variabilita_termica_max(dati)

            print("Stazione con maggiore variabilità termica:", stazione)

        elif scelta == 11:
            soglia_temp = float(input("Soglia temperatura anomalie: "))
            soglia_co2 = float(input("Soglia CO2 anomalie: "))

            stampa_report(dati, soglia_temp, soglia_co2)

        elif scelta == 12:
            var = float(input("Inserisci variazione percentuale temperatura: "))

            risultati = simulazione_variazione(dati, var)

            print("\n--- RISULTATI SIMULAZIONE ---\n")

            for stazione, incremento in risultati:

                print(f"Stazione: {stazione}  Incremento medio: {incremento:.2f}")

        elif scelta == 0:

            print("Uscita dal programma")

        else:

            print("Scelta non valida")


main()
        

















