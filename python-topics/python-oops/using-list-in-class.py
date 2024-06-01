class FC:
    def __init__(self, letter="b"):
        self.letter = [letter]

    def add(self,add_letter = "a"):
        self.letter.append(add_letter)
        print("We have added a letter 'a' to the list")

    def addbetween(self,position,add_letter = "c"):
        if 0 <= position <= len(self.letter):
           self.letter.insert(position,add_letter)
           print("We have inserted a letter 'c' between 'b' and 'a'")
        else:
            print(f"invalid position:{position}")

    def remove(self,letter_add):
        if letter_add in self.letter:
            self.letter.remove(letter_add)
            print("We have removed a letter 'a' from the list")
        else:
            print("The letter 'a' is not in the list to remove")

fc = FC()


fc.add("a")
print(fc.letter)  

fc.addbetween(1,"c")
print(fc.letter) 

fc.remove("a")
print(fc.letter)  

    

    