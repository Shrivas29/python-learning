try:
    k = open("demofile.txt", "r")
    print(k)
except FileNotFoundError:
    print("the given file was not found")