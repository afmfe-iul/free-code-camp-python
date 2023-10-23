# Context management with a class
from contextlib import contextmanager


class ManagedFile:
    def __init__(self, filename):
        print("init")
        self.filename = filename

    def __enter__(self):
        print("enter")
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("exception has been handled")

        print("exit")
        return True


with ManagedFile("gil.txt") as file:
    print("file first line:", file.readline()[0:-1])  # removes line break
    file.write("blah")  # no write permissions, this throws

print("main end 1")


# Context Management with function
@contextmanager
def open_managed_file(filename):
    f = open(filename, "r")
    try:
        yield f
    except Exception:
        print("exception has been handled")
        return True
    finally:
        f.close()


with open_managed_file("gil.txt") as file:
    print("file first line:", file.readline()[0:-1])  # removes line break
    file.write("blah")  # no write permissions, this throws

print("main end 2")
