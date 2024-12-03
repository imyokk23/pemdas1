#152023120
#AMSA EFRAIM CICIO TARIGAN 
#TUGAS GIT 

data_panen = {
    'lokasi1': {'nama_lokasi': 'Kebun A', 'hasil_panen': {'padi': 1200, 'jagung': 800, 'kedelai': 500}},
    'lokasi2': {'nama_lokasi': 'Kebun B', 'hasil_panen': {'padi': 1500, 'jagung': 900, 'kedelai': 450}},
    'lokasi3': {'nama_lokasi': 'Kebun C', 'hasil_panen': {'padi': 1100, 'jagung': 750, 'kedelai': 600}},
    'lokasi4': {'nama_lokasi': 'Kebun D', 'hasil_panen': {'padi': 1300, 'jagung': 850, 'kedelai': 550}},
    'lokasi5': {'nama_lokasi': 'Kebun E', 'hasil_panen': {'padi': 1400, 'jagung': 950, 'kedelai': 480}},
}

print("Data Panen:")
for lokasi in data_panen:
    print(f"{lokasi} - {data_panen[lokasi]['nama_lokasi']}: {data_panen[lokasi]['hasil_panen']}")
print()

# lokasi2
print(f"Hasil jagung lokasi2: {data_panen['lokasi2']['hasil_panen']['jagung']}")
print()

# lokasi3
print(f"Nama lokasi3: {data_panen['lokasi3']['nama_lokasi']}")
print()

hasil_padi = {}
hasil_kedelai = {}

for lokasi in data_panen:
    hasil_padi[lokasi] = data_panen[lokasi]['hasil_panen']['padi']
    hasil_kedelai[lokasi] = data_panen[lokasi]['hasil_panen']['kedelai']

print("Hasil panen padi:")
print(hasil_padi)
print()

print("Hasil panen kedelai:")
print(hasil_kedelai)
print()

# Kondisi 
print("Kondisi Lokasi:")
for lokasi in data_panen:
    nama = data_panen[lokasi]['nama_lokasi']
    padi = data_panen[lokasi]['hasil_panen']['padi']
    jagung = data_panen[lokasi]['hasil_panen']['jagung']
    
    if padi > 1300 or jagung > 800:
        print(f"{nama}: Perlu perhatian khusus.")
    else:
        print(f"{nama}: Kondisi baik.")