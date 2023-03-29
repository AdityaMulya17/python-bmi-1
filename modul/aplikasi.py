berat_badan = float(input("Masukkan berat badan: "))

if(berat_badan < 60):
    print("Berat badan anda normal")
    gula_darah = float(input("Masukkan gula darah: "))
    if(gula_darah < 140):
        print("Anda Normal")
    else:
        print("Anda perlu ke dokter")
else:
    print("Berat badan anda tidak normal")
    print("Anda perlu ke dokter")