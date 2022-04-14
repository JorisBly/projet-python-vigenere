message = 'bonjour'
cle = 'salutsa'
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']


# Permet de savoir si la clef fait la bonne taille et si elle est trop petite la dupliquer jusqu'a quelle fasse la bonne taille
def generateKey(message, cle):
    cle = list(cle)
    if len(message) == len(cle):
        return cle
    else:
        for i in range(len(message) -
                       len(cle)):
            cle.append(cle[i % len(cle)])

    return ("".join(cle))


# Permet de crypter notre mot
def cipherText(message, cle):
    cipher_text = []
    for i in range(len(message)):
        print("----------")
        print(ord(message[i]))
        print(ord(cle[i]))
        x = (ord(message[i].upper()) +
             ord(cle[i].upper())) % 26

        x += ord('a')
        cipher_text.append(chr(x))
        print(cle)
        print(message)
        return (print("".join(cipher_text)))


print(cipherText(message, cle))


def originalText(cipher_text, cle):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i].upper()) -
             ord(cle[i].upper()) + 26) % 26
        x += ord('a')
        orig_text.append(chr(x))
    return ("".join(orig_text))




# return ("".join(cipher_text))

# for i in message:
#   indexMessage = ord(i)
#  print(indexMessage)

# for x in clef:
#   indexClef = ord(x)
#  print(indexMessage + indexClef % 26)
