numerosecreto = 301
tentativimax= 4

while tentativimax > 0:
    tentativo = int(input("Indovina il numero segreto: "))

    if tentativo == numerosecreto:
        print("Hai indovinato!")
    elif tentativo != numerosecreto:
        tentativimax -= 1
        print("Hai sbagliato! Hai ancora", tentativimax, "tentativi")
    if tentativimax == 1:
        print("Attenzione, ti rimane un solo tentativo!")
  
    if tentativimax == 0:
        print("Hai esaurito i tentativi!")
    else: print("non è un numero valido")
        

