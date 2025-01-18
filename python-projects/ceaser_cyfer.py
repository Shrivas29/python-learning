ala = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encode and type 'decode' to decode ").lower

message = input("what is the message u want to type").lower
swift_num  = int(input("enter a swift number "))

#example input "shrivas"
def encript(orginal_text,swift_number):
    cypher_text = ""

    for letter in orginal_text:
        placeholder = ala.index(letter) + swift_number # 19 -> 21 due to adding the swift number with our index value 
        placeholder %= len(ala)
        cypher_text += ala[placeholder]
    print(cypher_text)

encript(message,swift_num)


def dycript(orginal_text,swift_number):
     cypher_text = ""

     for letter in orginal_text:
         placeholder = ala.index(letter) - swift_number # 21 -> 19  due to subracting the swift number with our index value 
         placeholder %= len(ala)
         cypher_text += ala[placeholder]
     print(cypher_text)

dycript(message,swift_num)


def ceasar(orginal_text,swift_number,direction_1):
    output = ""
    for letter in orginal_text:
        if letter not in ala:
          output += letter
        else:  
          if direction_1 == "decode":
             swift_number *= -1
             
             placeholder = ala.index(letter) + swift_number # 21 -> 19  due to subracting the swift number with our index value 
             placeholder %= len(ala)
             cypher_text += ala[placeholder]
             print(cypher_text)

ceasar(message,swift_num,direction)


# to restart the game 

restart = True

while restart:
    direction = input("type 'encode' to encode and type 'decode' to decode ").lower
    message = input("what is the message u want to type").lower
    swift_num  = int(input("enter a swift number "))
        

    output_1 = input("if you wanna countinue type 'yes' and if you dont wanna countinue then type 'no' ").lower
    if output_1 == "no":
        restart = False

    else:
        restart = True


