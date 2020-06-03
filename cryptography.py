def getAlfabethPossition(ch):
    alfabeth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    ch = ch.upper()    
    position = alfabeth.index(ch) #stars cointing on 0
    return position

def getAlfabethLetter(index):
    alfabeth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'           
    return alfabeth[index]


def encrypt(plain, key):  
    encrypt_msg = ''
    if not plain or not key:
        raise Exception("The text and the key must be supplied.")
        return ""

    for ch in plain:
        if not ch.isalpha():
            encrypt_msg += ch
        else:
            alphabet_possition = getAlfabethPossition(ch)  # stars on 0
            new_possition = (alphabet_possition + int(key)) % 26
            new_letter = getAlfabethLetter(new_possition)
            encrypt_msg += new_letter
            # print('Position of ', ch, ' is ', alphabet_possition, ' new position: ', new_possition, ' new_letter: ', new_letter)

    return encrypt_msg



def decryp(plain, key= None):
    if key:
      return encrypt( plain, -key)



if __name__ == "__main__":
    text = 'Iris Leal is my name 41'
    # text = 'ABCDEFG'
    # text = 'I'
    key= 3
    code = encrypt(text,key)
    print(text)
    print (code )
    decode = decryp(code, key)
    print (decode)