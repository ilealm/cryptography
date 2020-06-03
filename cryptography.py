def getAlfabethPossition(ch):
    alfabeth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    ch = ch.upper()    
    position = alfabeth.index(ch) #stars cointing on 0
    return position


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
            # print('Position of ', ch, ' is ', alphabet_possition)
            # use mod to get the value of the new letter
            new_possition = (alphabet_possition + int(key)) % 26
            # print (new_possition)
            print('Position of ', ch, ' is ', alphabet_possition, ' new position: ', new_possition)
            # get the letter on that position
            # add to the final message
        encrypt_msg += ch
  # if isn't a letteradd to encrypt_msg


    return encrypt_msg



def decryp(plainkey= None):

    # if key = Nonetry to decrypt another way
    pass


if __name__ == "__main__":
    # text = 'Iris Leal is my name 41'
    text = 'ABCDEFG'
    # text = 'VWXYZ'
    key=3
    print (encrypt(text,key))