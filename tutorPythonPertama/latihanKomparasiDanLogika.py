inputAngka = float(input("Silahkan masukan angka yg kurang dari 3 ato lebih\n dari 10:"));

kurangDari = (inputAngka < 3);
print("kurang dari 3 =",kurangDari);

lebihDari = (inputAngka > 10);
print("lebih dari 10 =",lebihDari);

isCorrect = kurangDari or lebihDari;
print("operator ternarynya:",isCorrect);

inputAngka = float(input("Silahkan masukan angka yg kurang dari 3 ato lebih\n dari 10:"));

kurangDari = (inputAngka > 3);
print("kurang dari 3 =",kurangDari);

lebihDari = (inputAngka < 10);
print("lebih dari 10 =",lebihDari);

isCorrect = kurangDari and lebihDari;
print("operator ternarynya:",isCorrect);

inputAngka = float(input("Silahkan masukan angka yg kurang dari 5 ato lebih\n dari 8: "));

kurangDari = (inputAngka < 5);
print("kurang dari 5 =",kurangDari);

lebihDari = (inputAngka > 8);
print("lebih dari 8 =",lebihDari);

result = kurangDari and lebihDari;
print("hasilnya adalah:",result);