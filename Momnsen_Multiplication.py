Tab = True
while Tab:
    itilizate = input("Rantre yon nonb ant 1 a 10 pou afiche tab miltiplikasyon l: ")
    while (not itilizate.isdigit()):
        itilizate = input("Rantre yon nonb ant 1 a 10 pou afiche tab miltiplikasyon l: ")
    itilizate = int(itilizate)
    while (itilizate < 0 or itilizate > 10):
        itilizate = int(input("Rantre yon nonb ant 1 a 10 pou afiche tab miltiplikasyon l: "))
    for n in range(1,11):
        nonb = n * itilizate
        print(n, "*", itilizate , "=", nonb )
    print()
    anko = input("Tape 'w' si w vle afiche yon lòt tab epi 'n' si w vle kanpe : ")
    if anko == "w":
        Tab = True
    else:
        Tab = False