# Fungsi 1 : Cek Ganjil / Genap
def cek_ganjil_genap():
    while True:
        angka = int(input("\nMasukkan sebuah angka: "))

        if angka % 2 == 0:
            print(f"{angka} adalah bilangan Genap")
        else:
            print(f"{angka} adalah bilangan Ganjil")

        if not ulangi("Cek lagi"):
            break


# Fungsi 2 : Perkalian
def perkalian():
    while True:
        angka1 = int(input("\nMasukkan angka pertama : "))
        angka2 = int(input("Masukkan angka kedua   : "))

        hasil = angka1 * angka2

        print(f"Hasil perkalian {angka1} x {angka2} = {hasil}")

        if not ulangi("Hitung lagi"):
            break


# Fungsi 3 : Menghitung Jumlah Bilangan Ganjil dan Genap
def hitung_jumlah():
    while True:
        batas = int(input("\nMasukkan batas angka: "))

        genap = 0
        ganjil = 0

        for i in range(1, batas + 1):
            if i % 2 == 0:
                genap += 1
            else:
                ganjil += 1

        print(f"Jumlah bilangan genap  : {genap}")
        print(f"Jumlah bilangan ganjil : {ganjil}")

        if not ulangi("Hitung lagi"):
            break


# Fungsi pilihan ulang
def ulangi(keterangan):
    while True:
        print("\n==============================")
        print(f"1. {keterangan}")
        print("0. Keluar")
        print("==============================")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            return True
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program.")
            return False
        else:
            print("Pilihan tidak valid!")


# Fungsi Menu Utama
def menu():
    while True:
        print("\n==============================")
        print("         MENU PROGRAM")
        print("==============================")
        print("1. Cek Ganjil / Genap")
        print("2. Perkalian")
        print("3. Hitung Jumlah Ganjil & Genap")
        print("0. Keluar")
        print("==============================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            cek_ganjil_genap()

        elif pilihan == "2":
            perkalian()

        elif pilihan == "3":
            hitung_jumlah()

        elif pilihan == "0":
            print("Terima kasih telah menggunakan program.")
            break

        else:
            print("Pilihan tidak valid!")


# Program Utama
menu()