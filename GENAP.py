nama_saya = "Sarah Manuella Lumban Gaol"
NIM = "230441100072"
Ploting = "A"
Prodi = 'SI Sistem Informasi 2023'
print(f"NAMA : {nama_saya}")
print(f"NIM  : {NIM}")
print(f"PLOTING :{Ploting}")
print(f"PRODI: {Prodi}")

# SOAL NOMOR 1
print(f"-----Soal Nomor 1-----")
# Input panjang, lebar, dan tinggi dari pengguna
panjangBalok = int(input("Masukkan panjang balok: "))
lebarBalok = int(input("Masukkan lebar balok: "))
tinggiBalok = int(input("Masukkan tinggi balok: "))
#hitung volume balok
volumeBalok = panjangBalok * lebarBalok * tinggiBalok 
#tampilkan volume balok
print(f"Volume balok adalah: {volumeBalok} satuan kubik")


# SOAL NOMOR 2
print(f"-----Soal Nomor 2-----")
# Input jari-jari dan tinggi dari pengguna
jari_jariTabung = float(input("Masukkan jari-jari tabung: "))
tinggiTabung = float(input("Masukkan tinggi tabung: "))
# Menghitung volume tabung
volumeTabung = 22/7 * jari_jariTabung*jari_jariTabung * tinggiTabung
# Menampilkan hasil volume tabung
print(f"Volume tabung adalah: {volumeTabung:.2f}")


# SOAL NOMOR 3
print(f"-----Soal Nomor 3-----")
# Input jari-jari  dari pengguna
jari_jariBola = float(input("Masukkan jari-jari Bola: "))
# Menghitung volume tabung
volumeBola = 4/3 * 22/7 * jari_jariBola * jari_jariBola * jari_jariBola
# Menampilkan hasil volume tabung
print(f"Volume Bola adalah: {volumeBola:.2f}")