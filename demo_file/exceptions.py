# ZeroDivisionError: division by zero

# 10 * (1/0)

# -----------------------
# Exception Handling
# =======================

try:
    10 * (1/0)
except ZeroDivisionError:
    print("Divide By Zero Not Allowed")


try:
    10 * (1/0)
except ZeroDivisionError as error:
    print(format(error))

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [D, B, C]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")