print("=== Sistem Reservasi Kamar Hotel ===")

jumlah_tamu = int(input("Masukkan jumlah tamu: "))

if jumlah_tamu > 4:
    print("Maaf, maksimal kapasitas dalam satu kali reservasi adalah 4 orang.")

else:
    print("\nPilihan Kamar: deluxe / superior")
    tipe_kamar = input("Masukkan tipe kamar: ").lower()

    if tipe_kamar == "deluxe":
        nama_kamar = "Kamar Deluxe"
        harga_kamar = 500000
    elif tipe_kamar == "superior":
        nama_kamar = "Kamar Superior"
        harga_kamar = 300000
    else:
        nama_kamar = "Kamar Standard"
        harga_kamar = 200000
        print("Info: Tipe kamar tidak valid, otomatis dialihkan ke Kamar Standard.")

    sarapan = input("Tambah paket sarapan? (y/t): ").lower()
    biaya_sarapan = 0

    if sarapan == "y":
        biaya_sarapan = 50000
        print("Info: Paket sarapan ditambahkan.")

    total_bayar = harga_kamar + biaya_sarapan

    print("\n=== Struk Reservasi ===")
    print(f"Tipe Kamar       : {nama_kamar}")
    print(f"Harga Kamar      : Rp {harga_kamar}")
    print(f"Biaya Sarapan    : Rp {biaya_sarapan}")
    print("------------------------------")
    print(f"TOTAL BAYAR      : Rp {total_bayar}")
