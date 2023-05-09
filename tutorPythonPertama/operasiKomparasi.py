x = 4;
y = 5;
a = 6;
b = 7;
hasil = x != y, a == b;

print(hasil);

# is sebagai komparasi object identity
num1 = 5;
num2 = 5;
print("nilai num1 =",num1,"id =",hex(id(num1)));
print("nilai num2 =",num2,"id =",hex(id(num2)));
hasil2 = num1 is not num2;
print("x is y =",hasil2);