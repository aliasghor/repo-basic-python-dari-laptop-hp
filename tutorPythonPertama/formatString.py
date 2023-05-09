# template literals versi python
brokk = "apa kabarr brokk";
formatStr = f"{brokk}";
print(formatStr);

pembatas = "pembatas".center(70,"=");
print(pembatas);
# string
string = "Ali ganteng";
hasil = f"Apakah {string} iyaa donggg";
print(hasil);

pembatas = "pembatas".center(70,"=");
print(pembatas);
# num
angka = 2005.5;
hasil = f"angka = {angka}";
print(hasil);
#boolean
pembatas = "pembatas".center(70,"=");
print(pembatas);

bool = False;
hasil = f"Nilai boolean = {bool}";
print(hasil)
#bilangan bulat
pembatas = "pembatas".center(70,"=");
print(pembatas);

angka = 15;
hasil = f"bilangan bulat = {angka:d}";
print(hasil);
# bilangan ribuan
pembatas = "pembatas".center(70,"=");
print(pembatas);

angka = 1000000000000000000;
hasil = f"{angka:,}";
print(hasil);
#bilangan decimal
pembatas = "pembatas".center(70,"=");
print(pembatas);

angka = 2005.5212345;
hasil = f"angka = {angka:.1f}";
print(hasil);

# menampilkan leading zero
pembatas = "pembatas".center(70,"=");
print(pembatas);

angka = 2005.5212345;
hasil = f"angka = {angka:010.4f}";
print(hasil);

#f format persen
pembatas = "pembatas".center(70,"=");
print(pembatas);

persen = 0.045;
hasil = f"persen = {persen:.2%}";
print(hasil);

# melakukan operasi aritmatika dalem template literals
pembatas = "pembatas".center(70,"=");
print(pembatas);

x = 10;
y = 10;
hasil = f"hasilnya adalah = {x / y}";
print(hasil);

# format angka laen (binary,octal,hexadecimal)
pembatas = "pembatas".center(70,"=");
print(pembatas);

angka = 255;
formatBinary = f"binary = {bin(angka)}";
formatOctal = f"octal = {oct(angka)}";
formatHexadecimal = f"hexadecimal{hex(angka)}";
print(f"{formatBinary}, {formatOctal}, {formatHexadecimal}");