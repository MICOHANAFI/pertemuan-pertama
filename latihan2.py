while True:
    angka = int(input("Masukkan sebuah angka: "))

    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap")
    else:
        print(f"{angka} adalah bilangan ganjil")

    pilihan = input("\nKetik 'exit' untuk keluar atau tekan Enter untuk mencoba lagi: ")

    if pilihan.lower() == "exit":
        print("Terima kasih telah menggunakan program.")
        break