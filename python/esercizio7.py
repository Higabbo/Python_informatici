for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("mazinga")
    elif i % 3 == 0:
        print("BOOM")
    elif i % 5 == 0:
        print("ZOOM")
    else:
        print(i)