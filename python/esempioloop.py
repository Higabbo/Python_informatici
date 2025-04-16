uscita = ''

while uscita != "q":
    print("-----menu-----")
    print("a) gioca")
    print("b) calcola")
    print("c) saluta")
    print("q) esci")
    print("--------------")
    
    scelta = str(input("scegli un'opzione: "))
    if scelta == "a":
        print("hai scelto di giocare")
    elif scelta == "b":
        print("hai scelto di calcolare qualcosa") 
    elif scelta == "c":
        print("hai scelto di salutare")
    elif scelta == "q":
        print("arrivederci")
    else:
        print("opzione non valida")