def cek_ganjil_genap():
    angka = int(input("Masukkan sebuah angka: "))

    if angka % 2 == 0:
        print(f"{angka} adalah bilangan Genap")
    else:
        print(f"{angka} adalah bilangan Ganjil")


# Fungsi 2 : Perkalian
def perkalian():
    angka1 = int(input("Masukkan angka pertama : "))
    angka2 = int(input("Masukkan angka kedua   : "))

    hasil = angka1 * angka2

    print(f"Hasil perkalian {angka1} x {angka2} = {hasil}")


# Fungsi 3 : Menghitung Jumlah Bilangan Ganjil dan Genap
def hitung_jumlah():
    batas = int(input("Masukkan batas angka: "))

    genap = 0
    ganjil = 0

    for i in range(1, batas + 1):
        if i % 2 == 0:
            genap += 1
        else:
            ganjil += 1

    print(f"Jumlah bilangan genap  : {genap}")
    print(f"Jumlah bilangan ganjil : {ganjil}")


# Fungsi Menu
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

        input("\nTekan Enter untuk kembali ke menu...")


# Program Utama
menu()