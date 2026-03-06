"""Eserciziario Python, I dizionari, Avanzato 1

Esercizio n. 1
Merge profondo con conflitti semantici
Dati due dizionari D e D’, costruire un dizionario D”
con una funzione di deep_merge(D, D’) che unisca
ricorsivamente i due dizionari D e D’, arbitrariamente
annidati, secondo le regole:
1)I valori scalari diversi sono uniti a formare una
tupla;
2)Le liste sono concatenate senza duplicati,
preservando l’ordine;
3)Le tuple sono concatenate senza duplicati,
preservandone l’ordine;
4)Gli insiemi sono uniti;
5)I dizionari sono fusi in modo ricorsivo.

___
Output:
D” = {"a": (1, 2), "b": [1, 2, 3, 4], "c": {"x": 10,
"y": [1, 2, 3], "z": 5}, "d": ("foo", ["foo", "bar"]),
"e": 100}"""

diz1 = {"a": 1, "b": [1, 2, 3], "c": {"x": 10, "y": [1,
                                                     2]}, "d": "foo"}
diz2 = {"a": 2, "b": [3, 4], "c": {"y": [2, 3], "z": 5},
        "d": ["foo", "bar"], "e": 100}
def deep_merge(diz1, diz2):

    new_diz = {}
    chiavi = diz1.keys() | diz2.keys()

    for chiave in chiavi:
        if chiave in diz1 and chiave not in diz2:
            new_diz[chiave] = diz1[chiave]
        elif chiave in diz2 and chiave not in diz1:
            new_diz[chiave] = diz2[chiave]
        else:
            val1 = diz1[chiave]
            val2 = diz2[chiave]

            if isinstance(val1, dict) and isinstance(val2, dict):
                new_diz[chiave] = deep_merge(val1, val2)
            elif isinstance(val1, set) and isinstance(val2, set):
                new_diz[chiave] = val1 | val2
            elif isinstance(val1, list) and isinstance(val2, list):
                risultato = []
                for elemento in val1 + val2:
                    if elemento not in risultato:
                        risultato.append(elemento)
                new_diz[chiave] = risultato
            elif isinstance(val1, tuple) and isinstance(val2, tuple):
                risultato = []
                for elemento in val1 + val2:
                    if elemento not in risultato:
                        risultato.append(elemento)
                new_diz[chiave] = tuple(risultato)
            else:
                new_diz[chiave] = (val1, val2)
    return new_diz

print(diz1)
print(diz2)
print(deep_merge(diz1, diz2))

