import re
messi = "bonjour"
key = "salutsa"
pattern = re.compile("[A-Za-z]")

# Permet de savoir si la clé fait la bonne taille et si elle est trop petite la dupliquer jusqu'a quelle fasse la taille du message
def generateKey(message, cle):
    cle = list(cle)
    if len(message) == len(cle):
        return (cle)
    else:
        for i in range(len(message) -
                       len(cle)):
            cle.append(cle[i % len(cle)])
        return "".join(cle)

motDeGenerer = generateKey(messi,key)
print(motDeGenerer)


# permet de crypter notre mot
def cipherText(message, cle):
    cipher_text = []
    for i in range(len(message)):
        x = (ord(message[i].upper()) +
             ord(cle[i].upper())) % 26
        x += ord('a')
        cipher_text.append(chr(x))

    return ("".join(cipher_text))


print(cipherText(messi, key))
toto = cipherText(messi,key)


def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i].upper()) -
             ord(key[i].upper()) + 26) % 26
        x += ord('a')
        orig_text.append(chr(x))
    return ("".join(orig_text))


print(originalText(toto, key))


#def isUpperNotUpper(message):



# for i in message:
# indexMessage = ord(i)
# for x in cle:
# indexCle = ord(x)
# print(indexMessage+indexCle%26)

# for x in alphabete:
# index += 1
# if x == i:
# print(index)

# while i != x:
# index += 1
# print(index)

#print(ord(messi[i].upper()))
    #    print(ord(key[i]))