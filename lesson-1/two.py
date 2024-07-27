import one

print("Top level in two.py")

one.func()

if __name__ == "__main__":
    print("Two.py is direct")
else:
    print("Two.py is imported")
    