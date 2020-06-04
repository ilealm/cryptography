import nltk
nltk.download('words')
from nltk.corpus import words

def getAlfabethPossition(ch):
    alfabeth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    
    position = alfabeth.index(ch) # starts cointing on 0
    return position

def getAlfabethLetter(index):
    alfabeth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
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
            new_possition = (alphabet_possition + int(key)) % 52 # % 26
            new_letter = getAlfabethLetter(new_possition)
            encrypt_msg += new_letter
    return encrypt_msg



def decryp(plain, key):
    if key:
        return encrypt( plain, -key)


def crack_code(plain):
    word_list = words.words()
    key_with_max_words = 0
    max_words_found = 0
    plain_words = plain.split(' ')

    for index in range (52):
        founded_words_per_index = 0
        for word in plain_words:
            decryp_word = decryp(word, index)
            if decryp_word in word_list: 
                founded_words_per_index += 1
        if founded_words_per_index > max_words_found:
            max_words_found = founded_words_per_index
            key_with_max_words = index

    return decryp(plain,key_with_max_words)

def is_broken(plain):
    """
    Method that try to identify if a code is broken
    """
    word_list = words.words()
    
    plain_list = plain.split(' ')
    num_plain_list = len(plain_list)

    founded_words = 0
    for word in plain_list:
        word = word.replace(',','')
        word = word.replace('.','')
        word.strip()
        word.lower()
        if word in word_list: 
            founded_words += 1        

    if founded_words == num_plain_list:
        porcentage = 0
    else:
        porcentage = int((founded_words/num_plain_list)*100)

    return f'Only {founded_words} from {num_plain_list} words where recognized. There is a { porcentage } % chance of being broken.'

