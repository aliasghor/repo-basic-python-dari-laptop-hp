a = 10;
a **= 2;
print(a);

b = True;
print("\nnilai b =",b);
b |= False;
print("nilai b |= False, maka niali b =",b);

c = True;
c &= False;
print("\nnilai c = True, akan menjadi =",c);

d = True;
d ^= True;
print("\nnilai c = True, akan menjadi =",c);

e = 0b0100;
print("\nnilai e =",format(e,"04b"));
e >>=2;
print("nilai e >>=2, nilai e menjadi",e);
e <<=2;
print("nilai e <<=2, nilai e menjadi",e);