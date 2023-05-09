nama = "Ali asghor"
umur = 19
hobi = "ngoding"
orang = f"hi nama saya: {nama}, \numur saya: {umur}, \nhobi saya: {hobi}"
print(orang);

# string multiline triple single qouets
pembatas = "pembatas".center(68,"=")
print(pembatas)

person = f"""
nama : {nama}
umur : {umur}
hobi : {hobi}
"""
print(person);

# mengatur lebar
pembatas = "pembatas".center(68,"=")
print(pembatas)

nama = "gerry"
umur = "sudah di surga"
hobi = "tidur"
gerry = f"""
nama : {nama:>15}
umur : {umur}
hobi : {hobi}
"""
print(gerry)