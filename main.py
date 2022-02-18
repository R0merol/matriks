"""
Pemrograman Matriks
Nama: Faris Faikar Razannafi
NIM: 4611421092
Rombel: 2
Prodi: Teknik Informatika
"""


def input_matriks_pro(skalar=False, kali=False):
    matriks_a = []
    matriks_b = []
    nilai_skalar = 0
    baris_a, kolom_a, baris_b, kolom_b = 0, 0, 0, 0

    if kali:
        # Pilih ordo matriks A dan B
        baris_a = int(input("Pilih jumlah baris matriks A: "))
        kolom_a = int(input("Pilih jumlah kolom matriks A: "))
        print(f"Matriks A berordo {baris_a}x{kolom_a}")
        baris_b = kolom_a
        print(f"Pilih jumlah kolom matriks B: {baris_b}")
        kolom_b = int(input("Pilih jumlah kolom matriks B: "))
        print(f"Matriks B berordo {baris_b}x{kolom_b}")
        print("-" * 20)
    else:
        # Pilih ordo matriks
        baris_a = int(input("Pilih jumlah baris matriks: "))
        kolom_a = int(input("Pilih jumlah kolom matriks: "))
        print(f"Matriks A dan B berordo {baris_a}x{kolom_a}")
        if skalar:
            nilai_skalar = int(input("Pilih nilai skalar: "))
        print("-" * 20)

    # Input element matriks A dan B
    print("Input element matriks A")
    for i in range(baris_a):
        matriks_a.append([])
        for j in range(kolom_a):
            matriks_a[i].append(int(input(f"A {i + 1}, {j + 1}: ")))
    print("-" * 20)
    if kali:
        print("Input element matriks B")
        for i in range(baris_b):
            matriks_b.append([])
            for j in range(kolom_b):
                matriks_b[i].append(int(input(f"B {i + 1}, {j + 1}: ")))
        print("-" * 20)
    elif not skalar:
        print("Input element matriks B")
        for i in range(baris_a):
            matriks_b.append([])
            for j in range(kolom_a):
                matriks_b[i].append(int(input(f"B {i + 1}, {j + 1}: ")))
        print("-" * 20)

    # Tampilkan matriks A dan B
    print("A:")
    for i in range(baris_a):
        print('\t[', end=" ")
        for j in range(kolom_a):
            print(f"{matriks_a[i][j]}", end=" ")
        print(']\n', end="")
    if kali:
        print("B:")
        for i in range(baris_b):
            print('\t[', end=" ")
            for j in range(kolom_b):
                print(f"{matriks_b[i][j]}", end=" ")
            print(']\n', end="")
    elif skalar:
        print(f"Nilai Skalar: {nilai_skalar}")
    else:
        print("B:")
        for i in range(baris_a):
            print('\t[', end=" ")
            for j in range(kolom_a):
                print(f"{matriks_b[i][j]}", end=" ")
            print(']\n', end="")

    if skalar:
        return matriks_a, nilai_skalar
    else:
        return matriks_a, matriks_b


def input_matriks():
    matriks_a = []
    matriks_b = []

    # Pilih ordo matriks A dan B
    print(">>> Input ordo matriks")
    baris = int(input("Pilih jumlah baris matriks: "))
    kolom = int(input("Pilih jumlah kolom matriks: "))
    print(f"Matriks A dan B berordo {baris}x{kolom}")
    print("-" * 20)

    # Input element matriks A dan B
    print(">>> Input element matriks A")
    for i in range(baris):
        matriks_a.append([])
        for j in range(kolom):
            matriks_a[i].append(int(input(f"A {i + 1}, {j + 1}: ")))
    print("-" * 20)
    print(">>> Input element matriks B")
    for i in range(baris):
        matriks_b.append([])
        for j in range(kolom):
            matriks_b[i].append(int(input(f"B {i + 1}, {j + 1}: ")))
    print("-" * 20)

    # Tampilkan matriks A dan B
    print(">>> Hasil Kalkulasi")
    print("A:")
    for i in range(baris):
        print('\t[', end=" ")
        for j in range(kolom):
            print(f"{matriks_a[i][j]}", end=" ")
        print(']\n', end="")
    print("B:")
    for i in range(baris):
        print('\t[', end=" ")
        for j in range(kolom):
            print(f"{matriks_b[i][j]}", end=" ")
        print(']\n', end="")

    return matriks_a, matriks_b


def input_matriks_skalar():
    matriks = []

    # Pilih ordo matriks
    print(">>> Input ordo matriks")
    baris = int(input("Pilih jumlah baris matriks: "))
    kolom = int(input("Pilih jumlah kolom matriks: "))
    print(f"Matriks berordo {baris}x{kolom}")
    skalar = int(input("Pilih nilai skalar: "))
    print("-" * 20)

    # Input element matriks
    print(">>> Input element matriks A")
    for i in range(baris):
        matriks.append([])
        for j in range(kolom):
            matriks[i].append(int(input(f"A {i + 1}, {j + 1}: ")))
    print("-" * 20)

    # Tampilkan matriks
    print(">>> Hasil Kalkulasi")
    print("A:")
    for i in range(baris):
        print('\t[', end=" ")
        for j in range(kolom):
            print(f"{matriks[i][j]}", end=" ")
        print(']\n', end="")
    print(f"Nilai Skalar: {skalar}")

    return matriks, skalar


def input_matriks_kali():
    matriks_a = []
    matriks_b = []

    # Pilih ordo matriks
    print(">>> Input ordo matriks")
    baris_a = int(input("Pilih jumlah baris matriks A: "))
    kolom_a = int(input("Pilih jumlah kolom matriks A: "))
    print(f"Matriks A berordo {baris_a}x{kolom_a}")
    baris_b = kolom_a
    print(f"Pilih jumlah kolom matriks B: {baris_b}")
    kolom_b = int(input("Pilih jumlah kolom matriks B: "))
    print(f"Matriks B berordo {baris_b}x{kolom_b}")
    print("-" * 20)

    # Input element matriks
    print(">>> Input element matriks A")
    for i in range(baris_a):
        matriks_a.append([])
        for j in range(kolom_a):
            matriks_a[i].append(int(input(f"A {i + 1}, {j + 1}: ")))
    print("-" * 20)
    print(">>> Input element matriks B")
    for i in range(baris_b):
        matriks_b.append([])
        for j in range(kolom_b):
            matriks_b[i].append(int(input(f"B {i + 1}, {j + 1}: ")))
    print("-" * 20)

    # Tampilkan matriks A dan B
    print(">>> Hasil Kalkulasi")
    print("A:")
    for i in range(baris_a):
        print('\t[', end=" ")
        for j in range(kolom_a):
            print(f"{matriks_a[i][j]}", end=" ")
        print(']\n', end="")
    print("B:")
    for i in range(baris_b):
        print('\t[', end=" ")
        for j in range(kolom_b):
            print(f"{matriks_b[i][j]}", end=" ")
        print(']\n', end="")

    return matriks_a, matriks_b


def penjumlahan_matriks(matriks_a, matriks_b):
    matriks_hasil = []

    baris = len(matriks_a)
    kolom = len(matriks_a[0])

    # Kalkulasi penjumlahan matriks
    for i in range(baris):
        matriks_hasil.append([])
        for j in range(kolom):
            matriks_hasil[i].append(matriks_a[i][j] + matriks_b[i][j])

    # Tampilkan hasil penjumlahan matriks A + B
    print("A + B:")
    for i in range(baris):
        print('\t[', end=" ")
        for j in range(kolom):
            print(f"{matriks_hasil[i][j]}", end=" ")
        print(']\n', end="")


def pengurangan_matriks(matriks_a, matriks_b):
    matriks_hasil = []

    baris = len(matriks_a)
    kolom = len(matriks_a[0])

    # Kalkulasi penjumlahan matriks
    for i in range(baris):
        matriks_hasil.append([])
        for j in range(kolom):
            matriks_hasil[i].append(matriks_a[i][j] - matriks_b[i][j])

    # Tampilkan hasil pengurangan matriks A - B
    print("A - B:")
    for i in range(baris):
        print('\t[', end=" ")
        for j in range(kolom):
            print(f"{matriks_hasil[i][j]}", end=" ")
        print(']\n', end="")


def perkalian_skalar(matriks, skalar):
    matriks_hasil = []

    baris = len(matriks)
    kolom = len(matriks[0])

    # Kalkulasi perkalian skalar matriks
    for i in range(baris):
        matriks_hasil.append([])
        for j in range(kolom):
            matriks_hasil[i].append(matriks[i][j] * skalar)

    # Tampilkan hasil matriks A * skalar
    print(f"A * {skalar}:")
    for i in range(baris):
        print('\t[', end=" ")
        for j in range(kolom):
            print(f"{matriks_hasil[i][j]}", end=" ")
        print(']\n', end="")


def perkalian_dua_matriks(matriks_a, matriks_b):
    matriks_hasil = []

    baris_a = len(matriks_a)
    kolom_a = len(matriks_a[0])
    kolom_b = len(matriks_b[0])

    # Kalkulasi perkalian matriks
    for i in range(baris_a):
        matriks_hasil.append([])
        for j in range(kolom_b):
            hasil = 0
            for k in range(kolom_a):
                hasil += matriks_a[i][k] * matriks_b[k][j]
            matriks_hasil[i].append(hasil)

    # Tampilkan hasil perkalian matriks A * B
    print("A * B:")
    for i in range(baris_a):
        print('\t[', end=" ")
        for j in range(kolom_b):
            print(f"{matriks_hasil[i][j]}", end=" ")
        print(']\n', end="")


def main():
    while True:
        print(">>> Pilih program yang ingin dijalankan:")
        print("1. Penjumlahan Matriks")
        print("2. Pengurangan Matriks")
        print("3. Perkalian Skalar")
        print("4. Perkalian Dua Matriks")
        pilihan = input("Pilihan: ")
        print("-" * 20)
        if pilihan == "1":
            matriks_a, matriks_b = input_matriks()
            penjumlahan_matriks(matriks_a, matriks_b)
        elif pilihan == "2":
            matriks_a, matriks_b = input_matriks()
            pengurangan_matriks(matriks_a, matriks_b)
        elif pilihan == "3":
            matriks_a, matriks_b = input_matriks_skalar()
            perkalian_skalar(matriks_a, matriks_b)
        elif pilihan == "4":
            matriks_a, matriks_b = input_matriks_kali()
            perkalian_dua_matriks(matriks_a, matriks_b)
        else:
            print("Pilih antara 1-4")
            print("-" * 20)
            continue
        print("-" * 20)
        pilihan = input(">>> Apakah anda ingin melakukan kalkulasi lagi? [y]: ")
        if pilihan.lower() == "y":
            print("")
            print("#" * 20, "-" * 20, "#" * 20)
            print("")
            continue
        else:
            print("Terima kasih telah menggunakan program ini :)")
            break


if __name__ == '__main__':
    main()

"""
# Stable version
if pilihan == "1":
    matriks_a, matriks_b = input_matriks()
    penjumlahan_matriks(matriks_a, matriks_b)
elif pilihan == "2":
    matriks_a, matriks_b = input_matriks()
    pengurangan_matriks(matriks_a, matriks_b)
elif pilihan == "3":
    matriks_a, matriks_b = input_matriks_skalar()
    perkalian_skalar(matriks_a, matriks_b)
elif pilihan == "4":
    matriks_a, matriks_b = input_matriks_kali()
    perkalian_dua_matriks(matriks_a, matriks_b)

# Retarded pro version
if pilihan == "1":
    matriks_a, matriks_b = input_matriks()
    penjumlahan_matriks(matriks_a, matriks_b)
elif pilihan == "2":
    matriks_a, matriks_b = input_matriks_pro()
    pengurangan_matriks(matriks_a, matriks_b)
elif pilihan == "3":
    matriks_a, matriks_b = input_matriks_pro(skalar=True)
    perkalian_skalar(matriks_a, matriks_b)
elif pilihan == "4":
    matriks_a, matriks_b = input_matriks_pro(kali=True)
    perkalian_dua_matriks(matriks_a, matriks_b)
"""
