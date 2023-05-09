class A:

    def show(self):
        print("Ini adalah A")

class B:

    def show(self):
        print("Ini adalah B")

class C(A,B):

    pass

obejek = C()
obejek.show()
# help(obejek)