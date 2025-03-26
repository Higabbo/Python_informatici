# Chiedi all'utente se ha superato l'esame scritto
esameScritto = input("Hai superato l'esame scritto? (sì/no): ")== "sì"

# Chiedi all'utente se ha superato l'esame orale
esameOrale = input("Hai superato l'esame orale? (sì/no): ")== "sì"

# In questo caso il professore è buono
print("PROFESSORE BRAVO")

if esameScritto and esameOrale:
    print("Complimenti! Hai superato entrambi gli esami.")
elif esameScritto or esameOrale:
    print("Hai superato solo uno degli esami.")
else:
    print("Mi dispiace, non hai superato nessuno dei due esami.")

# In questo caso il professore è cattivo
print("PROFESSORE CATTIVO")

if esameScritto and esameOrale:
    print("Complimenti! Hai superato l'esame.")
elif esameScritto and not esameOrale:
    print("Mi dispiace, non hai superato l'orale.")
elif not esameScritto and esameOrale:
    print("Mi dispiace, non hai superato lo scritto.")
else:
    print("Mi dispiace, non hai superato l'esame perché entrambi sono andati male.")
