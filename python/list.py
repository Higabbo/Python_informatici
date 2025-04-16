#list servono per contenere piu informazioni simili tra di loro sono delimitate da le parentesi quadre []
mia_lista = ["mela", "banana", "kiwi", "arancia"]
print(mia_lista)
#il ciclo for è adattoa stampare ogni singolo elemneto dlella lista
for frutta in mia_lista:
    print(frutta)
    
#esempio lista di voti. tutte le volte che sono insufficenti stampo il voto
voti = [4, 5, 6, 7, 8, 9, 10]
for voto in voti:
    if voto < 6:
        print("voto insufficiente", voto)    
    else:
        print("voto sufficiente", voto)