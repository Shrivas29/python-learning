class FC:
    def __init__(self, letter="b"):
        self.letter = [letter]

    def add(self):
        self.letter.append("a")
        print("We have added a letter 'a' to the list")

    def addbetween(self):
        self.letter.insert(1, "c")
        print("We have inserted a letter 'c' between 'b' and 'a'")

    def remove(self):
        if "a" in self.letter:
            self.letter.remove("a")
            print("We have removed a letter 'a' from the list")
        else:
            print("The letter 'a' is not in the list to remove")

fc = FC()


fc.add()
print(fc.letter)  

fc.addbetween()
print(fc.letter) 

fc.remove()
print(fc.letter)  

    

    