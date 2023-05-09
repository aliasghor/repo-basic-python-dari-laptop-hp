# upper case
brokk = "brokk";
print("Woi " + brokk);

woi = brokk.upper();
print("WOI " + woi);
# lower case
cok = "GKK GTT COKKK!!";
woi = cok.lower()
print(woi);

# pengecekan denganisX method
selow = "Selooww bae kali ngab";
woi = selow.islower()
print("apakah selow huruf kecil = " + str(woi));

#isalpha uuntuk cek semuanya huruf apa gk
print("===========================isalpha=====================");
huruf = "Gerry";
hasil = huruf.isalpha();
print(hasil);

#istitle
print("=========================istitle========================");
judul = "Ali Ganteng";
cekJudul = judul.istitle();
print(str(cekJudul));

# startswith() endswith()
print("=========================Startswith and endswith========================");
cekStart = "Ali kece".startswith("Ali");
print(str(cekStart));
cekEnd = "Ali kece".endswith("kece");
print(str(cekEnd));

# penggabungan komponen join() split()
print("=========================join() istitle()========================");
arr = ["Ali","Kece","Abis"];
gabung = "  ".join(arr);
print(arr);
print(gabung);
gabung = " yoi ".join(arr);
print(gabung);
print(gabung.split("yoi"));

#alokai karakter rjust() ljust() center()
kanan = "kanan".rjust(10);
print("'"+ kanan + "'");

kiri = "kiri".ljust(10);
print("'"+ kiri + "'");

tengah = "tengah".center(20,"-");
print("'" + tengah + "'");