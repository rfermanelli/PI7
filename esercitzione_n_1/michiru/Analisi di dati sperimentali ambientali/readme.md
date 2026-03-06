Programmatore informatico 

Esercitazione n. 1
20 febbraio 2026
Analisi di dati sperimentali ambientali
----------------------------------------------------------

Il nome di progetto: Analisi di dati sperimentali ambientali
/main.py
/README.md
/dati_inverno.txt

----------------------------------------------------------

📌INDICAZIONI GENERALI

    L’esecuzione del lavoro deve prevedere esclusivamente metodi procedurali (non è consentito l’utilizzo dei metodi della programmazione a oggetti). 
    E’ invece obbligatorio l’utilizzo di:
Liste
Tuple
Dizionari
Funzioni utente
Funzioni built-in
Funzioni lambda
Generatori yield

    Non è consentito l’utilizzo di librerie esterne; e il codice deve essere leggibile e deve avere carattere di modularità. 

console
non usa classe e oggetti
----------------------------------------------------------

📌OBIETTIVI

    Realizzare una applicazione da riga di comando (console) per l’analisi di dati provenienti dai sensori ambientali di stazioni di rilevamento che hanno il compito di monitorare i seguenti parametri fisici:
Temperatura
Umidità
Pressione
Concentrazione di CO2.

----------------------------------------------------------

📌SPECIFICHE(仕様)
    L’applicazione deve gestire un file .txt in cui ogni riga costituisce una rilevazione. Il formato della rilevazione è il seguente:
id_rilevazione, data, stazione_di_rilevamento, temperatura, umidità, pressione, concentrazione_co2
    Dove: la data ha il formato DD-MM-YYYY, la stazione_di_rilevamento è un identificativo testuale e tutti gli altri dati sono di tipo numerico.

✅def leggi_file

----------------------------------------------------------

📌MODELLAZIONE 
    I dati provenienti dal file .txt devono essere memorizzati in una lista di dizionari; le date devono essere rappresentate con tuple aventi il formato che segue: (DD, MM, YYYY); e, qualora si renda necessario, è utile prevedere strutture annidate per calcolare le aggregazioni di dati.

✅def leggi_file

----------------------------------------------------------

📌FUNZIONI

Analisi de
[scrittiva per stazione di rilevamento]

    Per ogni stazione di rilevamento calcolare:
Temperatura media
Temperature minima e massima
Umidità media
Pressione media

Valore massimo raggiunto dalla concentrazione di CO2

✅def genera_report

#####################################################

[Rilevamento di anomalie per stazione]

    Una rilevazione è considerata anomala se:
La temperatura è maggiore di una soglia impostata dall’utente
La CO2 è maggiore di una soglia impostata dall’utente
    L’applicazione deve restituire la lista delle anomalie ordinate per gravità (utilizzare obbligatoriamente una funzione lambda come chiave dell’ordinamento).

✅def genera_report / #yield

#####################################################

[Filtri dinamici]

L’applicazione deve consentire all’utente di filtrare i dati delle rilevazioni nel modo che segue:
Filtro per intervallo di date
Filtro per stazione di rilevamento
Filtro per intervallo di temperature
Filtro per intervallo di pressione
Filtro per intervallo di CO2

✅def filtra_per_stazione
✅def filtra_per_intervallo_temperatura
✅def filtra_per_intervallo_pressione
✅def filtra_per_intervallo_co2
✅def filtra_per_data

#####################################################

[Analisi temporale]

L’applicazione deve calcolare:
Il giorno con la temperatura più alta
Il giorno con la maggiore concentrazione di CO2
La stazione di rilevamento con la maggiore variabilità termica
   L’ordinamento e le selezioni devono obbligatoriamente utilizzare funzioni lambda.

✅def analisi_temporale

#####################################################

[Generatore di report]

    L’applicazione deve generare un report strutturato per stazione di rilevamento contenente:
Il numero totale delle rilevazioni
La media globale delle temperature
Il numero totale delle anomalie per la temperatura
Il numero totale delle anomalie per la concentrazione di CO2
Il giorno più critico in base al valore della concentrazione della CO2
   Il report deve essere prodotto obbligatoriamente utilizzando un generatore yield per la visualizzazione a console; e deve essere salvato su un file .txt

✅def salva_report_su_file

#####################################################
	
[Simulazione]

    L’applicazione deve implementare una funzione di simulazione che:
Riceve in input una variazione percentuale della temperatura
La applica a tutte le temperature esistenti
Ricalcoli la nuova media globale delle temperature per stazione di rilevamento
Calcoli l’incremento medio rispetto alla media originale
Restituisca i dati ordinati per incremento medio 

✅def simulazione

#####################################################

[Alimentazione del file .txt dei dati delle rilevazioni (facoltativa)] 
    L’applicazione deve implementare una funzione di inserimento dei dati  delle rilevazioni nel file .txt; la funzione deve ricevere in input:
id_rilevazione
data
stazione_di_rilevamento
temperatura, umidità
pressione, 
concentrazione_CO2
E deve inserire una nuova riga nel file .txt 

✅def aggiungi_rilevazione

----------------------------------------------------------


