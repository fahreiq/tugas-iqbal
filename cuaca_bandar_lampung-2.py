import requests

link = "https://api.open-meteo.com/v1/forecast?latitude=-5.4292&longitude=105.2610&daily=temperature_2m_max,precipitation_sum&timezone=Asia%2FBangkok&forecast_days=7"
respon = requests.get(link).json()

daftar_suhu = respon["daily"]["temperature_2m_max"]
daftar_hujan = respon["daily"]["precipitation_sum"]
daftar_hari = respon["daily"]["time"]

for i in range(len(daftar_hari)):
    hari = daftar_hari[i]
    suhu = daftar_suhu[i]
    hujan = daftar_hujan[i]

    if suhu > 30 or hujan > 5:
        file = open("laporan_cuaca.txt", "a")
        file.write("Tanggal: " + str(hari) + " Suhu: " + str(suhu) + " Derajat, Hujan: " + str(hujan) + " mm\n")
        file.close()
        print("Data hari " + str(hari) + " masuk ke file")
    else:
        print("Data hari " + str(hari) + " tidak memenuhi kriteria, dilewati")
