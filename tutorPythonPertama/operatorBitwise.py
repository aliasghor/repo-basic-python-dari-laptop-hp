a = 9;
b = 5;
# bitwiese or tandanya gini |
print("\n=================OR===============");
c = a | b;
print("nilai : ",a,"binary:",format(a,"08b"));
print("nilai : ",b,"binary:",format(b,"08b"));
print("nilai : ",c,"binary:",format(c,"08b"));

# bitwise and tandanya gini &
print("\n=================AND===============");
c = a & b;
print("nilai : ",a,"binary:",format(a,"08b"));
print("nilai : ",b,"binary:",format(b,"08b"));
print("nilai : ",c,"binary:",format(c,"08b"));

#bitwise XOR tandanya gini ^
print("\n=================Xor===============");
c = a ^ b;
print("nilai : ",a,"binary:",format(a,"08b"));
print("nilai : ",b,"binary:",format(b,"08b"));
print("nilai : ",c,"binary:",format(c,"08b"));

# bitwise NOT tandanya gini ~
print("\n=================NOT===============");
c = ~a;
print("nilai : ",a,"binary:",format(a,"08b"));
print("nilai : ",c,"binary:",format(c,"08b"));

#shift right tandana gini >>
print("\n=================Shift right=================");
c = a >> 2
print("nilai a :",a,"binary :",format(a,"08b"));
print("nilai a :",c,"binary :",format(c,"08b"));

#shift left tandana gini <<
print("\n=================Shift left=================");
c = a << 2
print("nilai a :",a,"binary :",format(a,"08b"));
print("nilai a :",c,"binary :",format(c,"08b"));