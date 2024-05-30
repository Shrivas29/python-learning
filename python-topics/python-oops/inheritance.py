class Books:

    made = "paper"

    def __init__(self,name,type):

        self.name = name
        self.type = type
    def read(self):
        print("you can read the book")


    def write(self):
        print("you can also write")

class Manga(Books):

    def __init__(self):
        print("book completed")
    

    def read(self):
        print("the manga can be read")

    def write(self):
        print("you can write")

class Horror(Books):
    
    def __init__(self):
        print("book completed")
    
    def read(self):
        print("you can read")
    
    def write(self):
        print("you can write")


#multiple inhertance 
class Comics(Horror,Manga):
        
    def __init__(self):
        print("book completed")

b0 = Horror()
b0.read()
b0.write()


b1 = Manga()
b1.read()
b1.write()


b2 = Comics()
b2.read()
b2.write()