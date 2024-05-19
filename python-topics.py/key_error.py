#key error
def dict_1():
    A = {"apple":"red","banana":"yellow"}
    try:
        k = A.get["orange"]
        print(k)
    except KeyError as e:
        print("key not found",e)
dict_1()