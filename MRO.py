# Method Resolution Order(MRO) it denotes the way a programming language resolves a method or attribute.
class A:
    def rk(self):
        print("in class A")


class B(A):
    # def rk(self):
    #     print("IN CLASS B")
    pass


class C(B, A):
    pass


r = A()
r1 = B()
r2 = C()
r.rk()
r1.rk()
r2.rk()
