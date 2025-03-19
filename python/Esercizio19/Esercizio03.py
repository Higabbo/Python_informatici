saldo= 10000  # Saldo iniziale
Guadagno = float(input("Inserisci il guadagno di questo mese: "))  # Chiede all'utente il Guadagno

if Guadagno > 1000:
    print("Bravo, questo mese hai guadagnato bene.")
    saldo += 1000 + (Guadagno - 1000)
elif Guadagno > 0:
    print("Mi spiace, questo mese hai guadagnato così così.")
    saldo += 1000
elif Guadagno == 0:
    print("Questo mese non hai guadagnato nulla.")
else:
    print("Questo mese stai perdendo soldi.")
    saldo += Guadagno 
print("questo è il tuo conto di questo mese", saldo)  
