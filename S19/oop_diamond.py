class A:
    def bar(self):
        print("bar from A")


class B(A):
    pass
    # def bar(self):
    #     print("bar from B")


class C(A):
    pass
    # def bar(self):
    #     print("bar from C")


class D(B, C):
    pass
    # def bar(self):
    #     print("bar from D")


d = D()
d.bar()

# problema diamantului - cum se mostenesc atributele din clasele superioare
