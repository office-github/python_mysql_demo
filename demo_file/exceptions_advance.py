import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.", sys.exc_info())
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# The try … except statement has an optional else clause, which, when present, must follow all except clauses.
# It is useful for code that must be executed if the try clause does not raise an exception.
# For example:

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# When an exception occurs, it may have an associated value, also known as the exception’s argument.
# The presence and type of the argument depend on the exception type.

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)

# Raise EXCEPTION

try:
    raise NameError("Hi There")
except NameError:
    print ("An Exception flew by!")
    raise # Reraise the exception and shows the error on the console that this is not handle.