namaAwal = "Ali";
namaTengah = "Masyhuri";
namaAkhir = "Asghor";
namaLengkap = namaAwal + " " + namaTengah + " "+ namaAkhir;
print(namaLengkap);

# 1.menghitung panjang string
panjang = len(namaLengkap);
print("panjang dari nama " + namaLengkap + " = " + str(panjang));

# 2.operator untuk string
d = "Ali";
status = d in namaLengkap;
print("Apakah string " + d + " ada di " + namaLengkap + " = " + str(status));

d = "Ali";
status = d not in namaLengkap;
print("Apakah string " + d + " tidak ada di " + namaLengkap + " = " + str(status));

# mengulang string
print(5*"WKW");

#indexing
print(namaLengkap[0:3]);

# item paling kecil
print("paling kecil:" + min(namaLengkap));

# item paling gede
print("paling kecil:" + max(namaLengkap));

ascii_code = ord(" ");
print(str(ascii_code));

data = 117;
print(chr(data));

# 4 operator dalem bentuk method
data = "gerry";
jumlah = data.count("r");
print("jumlah r pada gerry =",jumlah);