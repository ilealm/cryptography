def getAlfabethPossition(ch):
    alfabeth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    ch = ch.upper()    
    position = alfabeth.index(ch) #stars cointing on 0
    return position

def getAlfabethLetter(index):
    alfabeth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'           
    return alfabeth[index]


def encrypt(plain, key):
  # 'Iris Leal is my name 41'
    encrypt_msg = ''
    if not plain or not key:
        raise Exception("The text and the key must be supplied.")
        return ""

  # i need to take each character of the string
    for ch in plain:
        # print(ch)
        if not ch.isalpha():
            encrypt_msg += ch
        else:
            # if is a letter: get the position on the alphabet
            alphabet_possition = getAlfabethPossition(ch)  # stars on 0
            # use mod to get the value of the new letter
            new_possition = (alphabet_possition + int(key)) % 26
            # get the letter on that position
            new_letter = getAlfabethLetter(new_possition)
            # add to the final message
            encrypt_msg += new_letter
            # print('Position of ', ch, ' is ', alphabet_possition, ' new position: ', new_possition, ' new_letter: ', new_letter)

    return encrypt_msg



def decryp(plainkey= None):

    # if key = Nonetry to decrypt another way
    pass


if __name__ == "__main__":
    text = 'Iris Leal is my name 41'
    # text = 'ABCDEFG'
    # text = 'I'
    key= 3
    print (encrypt(text,key))