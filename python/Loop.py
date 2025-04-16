print("Esercizio Pari e Dispari. Ti verrà chiesto di inserire un numero. Se inserisci 0 termina il programma")

numero = int(input("inserisci un numero"))

while numero != 0:
    if numero % 2 == 0:
        print("il numero è pari")
    else:
        print("il numero è dispari")
    numero = int(input("inserisci un altro numero: "))

print("Hai inserito 0, il programma è terminato.") 