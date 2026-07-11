print("=" * 40)
print("      KALKULATOR BMI INTERAKTIF")
print("=" * 40)


jenis_kelamin = input("Masukkan jenis kelamin (Laki-laki/Perempuan): ").lower()
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))


tinggi = tinggi / 100


bmi = berat / (tinggi ** 2)

print("\n===== HASIL BMI =====")
print("BMI Anda = {:.2f}".format(bmi))


if bmi < 18.5:
    kategori = "Kurang"
elif bmi < 25:
    kategori = "Normal"
elif bmi < 30:
    kategori = "Berlebih"
else:
    kategori = "Obesitas"

print("Kategori BMI:", kategori)


if kategori == "Normal":
    print("\nSelamat! BMI Anda sudah berada pada kategori normal.")
    print("Tetap jaga pola makan, olahraga, dan istirahat yang cukup.")


else:
    print("\n=== Kuis Evaluasi Kebiasaan ===")

    olahraga = input("1. Apakah Anda jarang berolahraga? (Ya/Tidak): ").lower()
    manis = input("2. Apakah Anda sering makan makanan manis? (Ya/Tidak): ").lower()
    tidur = input("3. Apakah waktu tidur Anda kurang dari 7 jam sehari? (Ya/Tidak): ").lower()

    print("\n===== FEEDBACK =====")

    
    if kategori == "Kurang":
        if olahraga == "ya" and tidur == "ya":
            print("Berat badan Anda kurang dan kebiasaan kurang aktif serta kurang tidur dapat memengaruhi kesehatan.")
            print("Cobalah makan makanan bergizi, olahraga ringan secara rutin, dan tidur cukup.")
        elif tidur == "ya":
            print("Tidur yang cukup membantu proses pemulihan dan menjaga kesehatan tubuh.")
        else:
            print("Perbanyak makanan bergizi dengan protein dan karbohidrat sehat agar berat badan meningkat secara sehat.")

 
    elif kategori == "Berlebih":
        if olahraga == "ya" and manis == "ya":
            print("Kurang olahraga dan sering mengonsumsi makanan manis dapat menyebabkan berat badan meningkat.")
            print("Kurangi makanan tinggi gula dan mulai rutin berolahraga.")
        elif olahraga == "ya":
            print("Cobalah berolahraga minimal 30 menit setiap hari.")
        elif manis == "ya":
            print("Kurangi minuman dan makanan yang mengandung banyak gula.")
        else:
            print("Pertahankan pola hidup sehat agar BMI kembali normal.")


    elif kategori == "Obesitas":
        if olahraga == "ya" and manis == "ya" and tidur == "ya":
            print("Beberapa kebiasaan Anda berisiko meningkatkan obesitas.")
            print("Mulailah mengatur pola makan, olahraga rutin, dan tidur yang cukup.")
        elif olahraga == "ya" or manis == "ya":
            print("Perubahan kecil seperti mengurangi gula dan meningkatkan aktivitas fisik dapat membantu menurunkan berat badan.")
        else:
            print("Tetap lakukan pola hidup sehat dan pertimbangkan berkonsultasi dengan tenaga kesehatan.")

    
    print("\n=== Saran Berdasarkan Jenis Kelamin ===")

    if jenis_kelamin == "laki-laki":
        print("Saran untuk Laki-laki:")
        print("- Perbanyak aktivitas fisik seperti jogging atau latihan kekuatan.")
        print("- Konsumsi protein yang cukup untuk menjaga massa otot.")
        print("- Hindari minuman tinggi gula dan makanan cepat saji.")

    elif jenis_kelamin == "perempuan":
        print("Saran untuk Perempuan:")
        print("- Konsumsi makanan bergizi seimbang yang kaya zat besi dan kalsium.")
        print("- Lakukan olahraga seperti jalan kaki, bersepeda, atau yoga.")
        print("- Hindari diet ekstrem dan tetap penuhi kebutuhan nutrisi harian.")

    else:
        print("Jenis kelamin tidak dikenali. Masukkan 'Laki-laki' atau 'Perempuan' saat menjalankan program.")

print("\nTerima kasih telah menggunakan Kalkulator BMI Interaktif.")


# @danangsiseka