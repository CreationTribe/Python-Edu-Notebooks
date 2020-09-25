# logic error is a misunderstanding of how the data should be entered
# runtime error is the result of a logic error


# Exception handling

filename = input("Enter name of file: ")

try:
    myfile = open(filename, 'r')
except OSError:
    print("That file could not be opened. Using default file.")
    myfile = open("default.txt", 'r')


def mockmod(a, b):
    try:
        c = a/b
    except TypeError:
        print("wrong types, wanted floating point nums")
    except ZeroDivisionError:
        print("can't use a zero for second number")
    except:
        print("something happen?!")
    else:
        print("Good, yay, no problems")
    finally:
        print("the function has ended")
    return c


x = input("give number")
if x == 0:
    raise ZeroDivisionError

# import help
#
# help(modules)