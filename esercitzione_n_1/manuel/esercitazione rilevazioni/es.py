############ ESERCIZIO ANALISI RILEVAZIONI AMBIENTALI MANUEL ############

# APERTURA FILE #
def apri_file():
    try:
        file = open("rilevazioni.txt", "r")
    except FileNotFoundError:
        file = open("rilevazioni.txt", "w")
    return file


# CARICAMENTO DATI #
def caricamento_dati():
    dati = []

    file = apri_file()   
    righe = file.readlines()
    file.close()

    for riga in righe:
        riga = riga.strip()

        if riga == "":
            continue

        parti = [p.strip() for p in riga.split(",")]

        if len(parti) == 7:
            giorno, mese, anno = parti[1].split("-")

            diz = {
                "id": int(parti[0]),
                "data": (int(giorno), int(mese), int(anno)),
                "stazione": parti[2],
                "temperatura": float(parti[3]),
                "umidita": float(parti[4]),
                "pressione": float(parti[5]),
                "co2": float(parti[6])
            }

            dati.append(diz)

    return dati



# ANALISI DELLE STAZIONI #
def analisi_stazioni(dati):

    stazioni = {}

    for rilevazione in dati:
        nome = rilevazione["stazione"]

        if nome not in stazioni:
              stazioni[nome] = []

        stazioni[nome].append(rilevazione)


    for nome, lista in stazioni.items():

        temperature = list(map(lambda x: x["temperatura"], lista))
        umidita = list(map(lambda x: x["umidita"], lista))
        pressione = list(map(lambda x: x["pressione"], lista))
        co2 = list(map(lambda x: x["co2"], lista))

        print("Stazione:", nome)
        print("temperatura media:", sum(temperature)/len(temperature))
        print("temperatura minima:", min(temperature))
        print("temperatura massima:", max(temperature))
        print("Media umidità:", sum(umidita)/len(umidita))
        print("Media pressione:", sum(pressione)/len(pressione))
        print("CO2 massima:", max(co2))


# RILEVAMENTO ANOMALIE #
def ril_anomalie(dati, soglia_temp=15, soglia_co2=400):
    anomalie = []
    for r in dati:
        if r["temperatura"] > soglia_temp or r["co2"] > soglia_co2:
            anomalie.append(r)
    return sorted(anomalie, key=lambda x: (x["temperatura"], x["co2"]), reverse=True)



# FILTRO TRA DUE DATE #
def filtrodate(dati):
    datetrovate=[]
    data1_input = input("Inserisci la prima data gg-mm-yyyy: ").strip()
    data2_input = input("Inserisci la seconda data gg-mm-yyyy: ").strip()

    giorno1, mese1, anno1 = map(int, data1_input.split("-"))
    giorno2, mese2, anno2 = map(int, data2_input.split("-"))

    data1 = (anno1, mese1, giorno1)
    data2 = (anno2, mese2, giorno2)

    for r in dati:
        gg, mm, yyyy = r["data"]
        data_r = (yyyy, mm, gg)
        if data1 <= data_r <= data2:
            datetrovate.append(r)

    if not datetrovate:
        print("Nessuna rilevazione!")
    else:
        print("Rilevazioni tra il", data1_input, "e il", data2_input, ":")
        for r in datetrovate:
            print(r)

    return datetrovate



# FILTRO PER STAZIONE #
def filtrostazioni(dati):
    nome_stazione = input("Inserisci il nome della stazione: ").strip()
    trovato = False

    for r in dati:
        if r["stazione"] == nome_stazione:
            if not trovato:
                print("Rilevazioni in", nome_stazione,":")
            print(r)
            trovato = True
    if not trovato:
        print("Questa stazione non è presente.")

# FILTRO TRA DUE TEMPERATURE #
def filtrotemperature(dati):
    temperaturetrovate=[]
    temperatura_1 = float(input("Inserisci la prima temperatura: "))
    temperatura_2 = float(input("Inserisci la seconda temperatura: "))
   
    for r in dati:
        temperatura_r= r["temperatura"]
        if temperatura_1 <= temperatura_r <= temperatura_2:
            temperaturetrovate.append(r)
    
    if not temperaturetrovate:
        print("Nessuna rilevazione!")
    else:
        print("Rilevazioni tra i", temperatura_1,"°", "e i", temperatura_2,"°", ":")
        for r in temperaturetrovate:
            print(r)
     
    return temperaturetrovate



# FILTRO TRA DUE PRESSIONI #
def filtropressioni(dati):
    pressionitrovate=[]
    pressione_1 = float(input("Inserisci la prima pressione: "))
    pressione_2 = float(input("Inserisci la seconda pressione: "))
   
    for r in dati:
        pressione_r= r["pressione"]
        if pressione_1 <= pressione_r <= pressione_2:
            pressionitrovate.append(r)
    
    if not pressionitrovate:
        print("Nessuna rilevazione!")
    else:
        print("Rilevazioni tra la pressione", pressione_1, "e", pressione_2, ":")
        for r in pressionitrovate:
            print(r)
    return pressionitrovate


# FILTRO TRA DUE VALORI CO2 #
def filtro_co2(dati):
    co2_trovate=[]
    co2_1 = float(input("Inserisci la prima co2: "))
    co2_2 = float(input("Inserisci la seconda co2: "))
   
    for r in dati:
        co2_r= r["co2"]
        if co2_1 <= co2_r <= co2_2:
            co2_trovate.append(r)
    
   
    
    if not co2_trovate:
        print("Nessuna rilevazione!")
    else:
        print("Rilevazioni tra ", co2_1, "e", co2_2, ":")
        for r in co2_trovate:
            print(r)
    return co2_trovate
    


# ANALISI TEMPORALE #
def analisi_temporale(dati):

    max_temp = max(dati, key=lambda x: x["temperatura"])
    max_co2 = max(dati, key=lambda x: x["co2"])
    variabilita_ter={}
    

    for r in dati:
        stazione = r["stazione"]

        if stazione not in variabilita_ter:
            variabilita_ter[stazione] = []

        variabilita_ter[stazione].append(r["temperatura"])

    stazione_var = max(
        variabilita_ter.items(),
        key=lambda x: max(x[1]) - min(x[1])
    )
        
    print("Giorno con temperatura più alta:", max_temp["data"])
    print("Giorno con CO2 più alta:", max_co2["data"])
    print("Stazione con maggiore variabilità:", stazione_var[0])



# GENERAZIONE REPORT #
def gen_report(dati, soglia_temp, soglia_co2):

    stazioni= {}

    for r in dati:
        nome = r["stazione"]

        if nome not in stazioni:
            stazioni[nome] = []

        stazioni[nome].append(r)

    for nome, lista in stazioni.items():

        temperature = list(map(lambda x: x["temperatura"], lista))

        anomalie_temp = len(list(filter(lambda x: x["temperatura"] > soglia_temp, lista)))
        anomalie_co2 = len(list(filter(lambda x: x["co2"] > soglia_co2, lista)))

        giorno_critico_co2 = max(lista, key=lambda x: x["co2"])

        yield f"""
STAZIONE: {nome}
Tot rilevazioni: {len(lista)}
Media temperatura: {sum(temperature)/len(temperature)}
Anomalie temperatura: {anomalie_temp}
Anomalie CO2: {anomalie_co2}
Giorno piu critico (CO2): {giorno_critico_co2['data']}
"""



# SALVATAGGIO REPORT #
def salva_report(generatore):
    file = open("report.txt", "w")
    for parte in generatore:
        file.write(parte)
    file.close()
    print("Report salvato su report.txt")



# SIMULAZIONE AUMENTO TEMPERATURA #
def simulazione(dati, percentuale):

    risultati = {}
    incremento = percentuale / 100

    for r in dati:

        nome = r["stazione"]

        if nome not in risultati:
            risultati[nome] = []

        nuova_temp = r["temperatura"] * (1 + incremento)
        risultati[nome].append(nuova_temp - r["temperatura"])

    media_incrementi_stazione = []

    for nome, incrementi in risultati.items():
        media_inc = sum(incrementi) / len(incrementi)
        media_incrementi_stazione.append((nome, round(media_inc, 2)))

    media_incrementi_stazione.sort(key=lambda x: x[1], reverse=True)

    return media_incrementi_stazione

# ALIMENTAZIONE FILE #
def alimenta_rilevazioni(dati):
    while True:
        nuovo_id = int(input("Inserisci nuovo id: "))
        if any(r["id"] == nuovo_id for r in dati):
            print("L'ID", nuovo_id ,"esiste già! Inserisci un ID diverso.")
        else:
            break
        
    nuova_data= input("inserisci una nuova data in formato gg-mm-yyyy: ")
    nuova_stazione= input("inserisci una nuova stazione di rilevamento: ")
    nuova_temperatura= float(input("inserisci una nuova temperatura: "))
    nuova_umidita= float(input("inserisci una nuova umidità: "))
    nuova_pressione= float(input("inserisci una nuova pressione: "))
    nuova_co2= float(input("inserisci una nuova co2: "))

    with open("rilevazioni.txt", "a") as file:
        file.write("\n") 
        riga_nuova = f"{nuovo_id}, {nuova_data}, {nuova_stazione}, {nuova_temperatura}, {nuova_umidita}, {nuova_pressione}, {nuova_co2}\n"
        file.write(riga_nuova)
        file.close()
   
    print("dati inseriti correttamente nel file rilevazioni.txt")
    

# MENU DEL PROGRAMMA #
def menu_interattivo():
    dati = caricamento_dati()

    while True:
        print("\n|||| MENU PRINCIPALE||||")
        print("1- Ricevi dati delle stazioni")
        print("2- Rilevamento anomalie")
        print("3- Analisi temporale")
        print("4- crea file Report")
        print("5- Simulazione aumento temperatura")
        print("6- Filtro per date")
        print("7- Filtro per stazione")
        print("8- Filtro per temperature")
        print("9- Filtro per pressioni")
        print("10- Filtro per CO2")
        print("11- Inserimento nuova rilevazione")
        print("0- Esci")

        scelta = input("Scegli un'opzione: ").strip()

        if scelta == "1":
            analisi_stazioni(dati)
        elif scelta == "2":
            lista_anomalie = ril_anomalie(dati, 15, 400)
            print("ANOMALIE ORDINATE:")
            for a in lista_anomalie:
                print(a)
        elif scelta == "3":
            analisi_temporale(dati)
        elif scelta == "4":
            soglia_temp = float(input("Inserisci soglia temperatura: "))
            soglia_co2 = float(input("Inserisci soglia CO2: "))
            report = gen_report(dati, soglia_temp, soglia_co2)
            salva_report(report)
        elif scelta == "5":
            percentuale = float(input("Aumento temperatura (%): "))
            print(simulazione(dati, percentuale))
        elif scelta == "6":
            filtrodate(dati)
        elif scelta == "7":
            filtrostazioni(dati)
        elif scelta == "8":
            filtrotemperature(dati)
        elif scelta == "9":
            filtropressioni(dati)
        elif scelta == "10":
            filtro_co2(dati)
        elif scelta == "11":
            alimenta_rilevazioni(dati)
            dati = caricamento_dati()
        elif scelta == "0":
            print("DISCONNESSIONE DAL PROGRAMMA ESEGUITA CON SUCCESSO")
            break
        else:
            print("Scelta non presente, Riprova.")


# FUNZIONE PRINCIPALE #
def main():
    menu_interattivo()
main()