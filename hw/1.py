def add_four(a):
    x = 2

    def add_some():
        print("x = " + str(x))
        return a + x
    return add_some()


print(add_four(5))


