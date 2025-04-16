for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print(f"{numero} -AL PROF SONO NEUTRALE")
    elif numero % 3 == 0:
        print(f"{numero} -IL PRF MI AMA")
    elif numero % 5 == 0:
        print(f"{numero} -IL PROFFFFF MI ODIA")
    else:
        print(numero)

