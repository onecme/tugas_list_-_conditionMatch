print("Soal Nomer 1")
kendaraan = ["B 26547 SOY", "Motor", 120, "Hitam"]
print(kendaraan)
print()

print("Soal Nomer 2")
kendaraan.append(18000000)
kendaraan.append(2)
kendaraan.insert(2,"Street Beat")
kendaraan.insert(3,"matic")
print("Jawaban nomer 2 = ", kendaraan)
print()

print("Soal Nomer 3")
pilih = str(input("Masukkan pilihan (persegi/lingkaran/ segitiga) : "))

match pilih:
    case "persegi" | "Persegi" | "PERSEGI" :
        sisi = int(input("Masukkan sisi persegi : "))
        luasPersegi = sisi*sisi
        print("luas persegi = ", luasPersegi)
    case "lingkaran" | "Lingkaran" | "LINGKARAN":
        jariJari = int(input("Masukkan jari-jari lingkaran : "))
        luasLingkaran = 22/7 *jariJari *jariJari
        print("luas lingkaran = ", luasLingkaran)
    case "segitiga" | "Segitiga" | "SEGITIGA":
        alas = int(input("Alas segitiga : "))
        tinggi = int(input("Tinggi segitiga : "))
        luasSegitiga = 1/2 *alas *tinggi
        print("Luas segitiga = ", luasSegitiga)
    case _:
        print("error")
        
