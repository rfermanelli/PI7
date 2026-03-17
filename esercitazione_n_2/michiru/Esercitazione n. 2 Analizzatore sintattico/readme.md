 * Programmatore informatico
 * Esercitazione n. 2

 * 12 marzo 2026
   2026年3月12日

 * Analizzatore sintattico

-------------------------------------------------------------------------
##Termini che non conosco
##Lsw: Language Star Wars 
##EOF: End of file, indica la fine della sequenza di token, il file è vuoto e significa finire di verificare
##NFA/DFA: DFA: si muove su un unico percorso, NFA: può muoversi su più percorsi contemporaneamente
##LL (top down):
##LR (bottom up):
##un algoritmo di parsing: 


 * INDICAZIONI GENERALI

 * Non è consentito l’utilizzo di librerie esterne; e il codice deve essere leggibile e deve avere carattere di "modularità".

-------------------------------------------------------------------------

 * OBIETTIVI
   
 * Realizzazione di un analizzatore sintattico di un linguaggio sottoinsieme della lingua italiana.

-------------------------------------------------------------------------

 * SPECIFICHE

 * L’applicazione deve gestire un file in cui ogni riga costituisce una stringa del linguaggio Lsw sottoinsieme limitatissimo dell’italiano, che ammette come corretta la stringa:

 * Il padawan ha un maestro *
   「Il padawan ha un maestro *
 * Nonché tutte e sole quelle che si ottengono da essa permutando articoli e sostantivi nel modo seguente:
 * il (un) maestro (padawan) ha un (il) padawan (maestro)
   il (un) maestro (padawan) ha un (il) padawan (maestro)
 * L’applicazione ha lo scopo di fornire un algoritmo di analisi sintattica del testo contenuto nel file per stabilire se tale testo rispetta 
    le regole grammaticali imposte per il linguaggio Lsw.
   
 *  F. Luccio, Strutture Linguaggi Sintassi, Boringhieri, p. 144.
 *  F. Luccio 著『Strutture Linguaggi Sintassi』Boringhieri出版 144ページより

-------------------------------------------------------------------------

 * MODELLAZIONE
   
 * La grammatica formale del linguaggio Lsw è G(Lsw) = {T, N, P, S}

 * T = {il, un, ha, maestro, padawan}
 * N = {<articolo>, <sostantivo>, <verbo>, <soggetto>, <oggetto>, <gruppo_verbale>, <frase>},
 * P = {a, b, c, d, e, f, g}, l'ordine delle frase?
 * S = <frase> start symbol


 * L’insieme P delle produzioni (la sintassi) del linguaggio Lsw è:

 * a <articolo> ::= il | un
 * b <sostantivo> ::= padawan | maestro
 * c <soggetto> ::= <articolo> <sostantivo>
 * d <oggetto> ::= <articolo> <sostantivo>
 * e <verbo> ::= ha
 * f <gruppo verbale> ::= <verbo> <oggetto>
 * g <frase> ::= <soggetto> <gruppo_verbale>

 * L’analizzatore lessicale è il primo modulo del compilatore.

 * Ha il compito di generare i token (le categorie sintattiche) della stringa che analizza.
 * Ogni classe di token è descritta da un pattern, ossia da un'espressione regolare (regex).
 * Per ogni espressione regolare esiste un automa a stati finiti non deterministico (NFA) equivalente che riconosce lo stesso linguaggio.
 * L’analizzatore sintattico è il secondo modulo del compilatore.
 * Riceve la sequenza dei token generata dall’analizzatore lessicale; 
    verifica che la sequenza appartenga al linguaggio generato dalla grammatica costruendo un albero sintattico 
    e utilizzando un algoritmo di parsing (LL (top down), LR (bottom up)).

-------------------------------------------------------------------------

 * FUNZIONI

 * Analizzatore lessicale (lexer)
 * L’analizzatore lessicale ha il compito di riconoscere le categorie sintattiche che costituiscono la stringa.
 * Se, a esempio, in input riceve la stringa: il padawan ha un maestro
 * allora in output deve restituire la sequenza delle categorie lessicali: <articolo> <sostantivo> <verbo> <articolo> <sostantivo>
 * o la sequenza delle coppie token-lessico: <ARTICOLO, il> <SOSTANTIVO, padawan> <VERBO, ha> <ARTICOLO, un> <SOSTANTIVO, maestro>

####################################################################

 * Analizzatore sintattico (parser)

 * L’analizzatore sintattico ha il compito di verificare che la sequenza di token generata dal lexer rispetti le regole grammaticali del linguaggio, 
    costruendo un albero sintattico che ne rappresenta la struttura.
 * <frase>
 * <soggetto>
 * <articolo> ➜ il
 * <sostantivo> ➜ padawan
 * <gruppo verbale>
 * <verbo> ➜ ha
 * <oggetto>
 * <articolo> ➜ un
 * <sostantivo> ➜ maestro

 * Se la sequenza di token non è sintatticamente valida (cioè non è derivabile dalla grammatica), allora l’analizzatore genera un’eccezione (errore sintattico).

####################################################################

 * Riconoscitore sintattico (lexer + parser)

 * Il riconoscitore sintattico è il controller del lexer e del parser.
 * Legge ciascuna delle righe del file e le passa in input al lexer, che costituisce il primo modulo funzionale della catena.
 * In seguito passa in input al parser la sequenza di token generata dal lexer; e valuta la risposta del parser per:

 * a) continuare il processo di analisi del file fino alla fine generando un log degli errori sintattici;
 * b) interrompere il processo di analisi del file al primo errore sintattico riscontrato.
 * Le soluzioni a) e b) sono esclusive.

        #f.write("Il padawan ha un maestro\n")       # Corretto
        #f.write("un maestro ha il padawan\n")       # Corretto (scambio)
        #f.write("il maestro ha un maestro\n")       # Corretto
        #f.write("il padawan padawan ha un\n")       # Errore (ordine errato)
        #f.write("un padawan ha maestro\n")          # Errore (manca articolo)
        #f.write("il padawan ha un jedi\n")          # Errore (parola sconosciuta)

-------------------------------------------------------------------------
