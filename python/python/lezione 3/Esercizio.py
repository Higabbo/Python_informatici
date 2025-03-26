nome = input("Qual è il tuo nome? ")
eta = int(input("Quanti anni hai? "))
invito = bool(input("Hai un invito? (sì/no) "))

if eta >= 18 and invito:
    print("Ciao " + nome + " puoi far parte del club dei programmatori!")
elif eta <= 18 and invito:
    print("Caro " + nome + " non hai ancora compiuto 18 anni. Anche se hai l'invito non puoi entrare.")
elif eta > 18 and not invito:
    print("Caro " + nome + " pur avendo 18 anni non puoi entrare poiché ti manca l'invito.")
else:
    print("Mi spiace " + nome + " non puoi far parte del club. Non hai 18 anni e non hai neppure un invito.")
