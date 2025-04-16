# i=0 
# while i < 100:
#     print(i) 
#     i += 1
#     range(100)
# range(100) è un oggetto iterabile che genera i numeri da 0 a 99
for i in range(100):
    print(i)

for i in range(15, 20): # inizio, fine
    print(i)
    
for i in range(10, 50, 2): # inizio, fine, incremento
    print("incremento di 2",i )
#break e continue
#break interrompe il ciclo, continue salta l'iterazione corrente e continua con la successiva
#esempio; dato un set di numero da 1 a 10 interrompiamo il ciclo quando troviamo 5
for i in range(1, 11):
    if i == 5:
        break
    print(i)
    
for x in range(1, 11):
    if x == 5:
        continue
    print("la x vale",x)