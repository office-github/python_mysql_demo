class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

ret = MyClass().f()
print(ret)

if __name__ == "__main__":
    print("Main Method")
else:
    print(__name__, " : Method name")