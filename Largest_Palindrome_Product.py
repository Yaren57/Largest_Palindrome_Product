sonuc = 0
for sayi1 in range(9999, 100, -1):
    for sayi2 in range(sayi1, 100, -1):
        x = sayi1 * sayi2
        if x > sonuc:
            carpim = str(sayi1 * sayi2)
            if carpim == carpim[::-1]:
                sonuc = sayi1 * sayi2
print(sonuc)