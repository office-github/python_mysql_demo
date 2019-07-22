# Execute without any error
# function contains class
# name of fun, class and function in the class is same i.e. fun

def fun():
    class fun:
        def fun(self):
            print((self))
    fun().fun()
fun()

# ===================
# Output:
# ---------------------
# <__main__.fun.<locals>.fun object at 0x0096DD90>
