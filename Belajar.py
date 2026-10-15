import datetime

nama_hari = ["Senen","Selasa","Rabu","Kamis","jumaat","sabtu","minggu"]

tgl = int(input("masukan tanggal lahir (1-31):"))
bln = int(input("masukan bulan lahir (1-12):"))
thn = int(input("masukan tahun lahir (contoh 2005:"))

tanggal_lahir = datetime.date(thn, bln, tgl)

indeks_hari = tanggal_lahir.weekday()

print(f"kamu lahir pada hari {nama_hari[indeks_hari]}")