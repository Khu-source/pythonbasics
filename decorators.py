def announce(f):
    def wrapper():
        print("Running...")
        f()
        print("Done")
    return wrapper

@announce
def hello():
    print("Hello world")

hello()