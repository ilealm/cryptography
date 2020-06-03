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
            # print('Position of ', ch, ' is ', alphabet_possition, ' new position: ', new_possition, ' new_letter: ', new_letter)

    return encrypt_msg



def decryp(plain, key):
    if key:
        return encrypt( plain, -key)


def crack_code(plain):
    word_list = words.words()
    # print(word_list[0:10])
    key_with_max_words = 0
    max_words_found = 0
    plain_words = plain.split(' ')

    for index in range (26):
        # this is the counter of words in this round
        founded_words_per_index = 0
        for word in plain_words:
            decryp_word = decryp(word, index)
            if decryp_word in word_list: 
                founded_words_per_index += 1
                print('I found this word in the list', decryp_word, ' in round ', index)
        if founded_words_per_index > max_words_found:
            print('Change values from ', founded_words_per_index, ' to ', max_words_found)
            max_words_found = founded_words_per_index
            key_with_max_words = index
            print('NEW values from ', founded_words_per_index, ' to ', max_words_found, ' index: ', index)


    # i know i can have move 26 switchs

    # for each word, i will create a new word moving from 0-26 Position
    # i will see if the word exist, if so, i will have a words_existing_count for each iteration

    # will return the iterations with more words existing 
        # word_list = words.words()
        # print(word_list[0:10])
    print('key_with_max_words ', key_with_max_words)
    return decryp(plain,key_with_max_words)



if __name__ == "__main__":
    # text = 'Iris Leal is my name 41 xyz'
    # text = 'ABCDEFG'
    # text = 'I'
    text = 'It was the best of times, it was the worst of times.'
    key= 13
    code = encrypt(text,key)
    # print(text)
    print('the code is: ', code )
    # decode = decryp(code, key)
    # print (decode)
    # print(decryp(code))
    print(crack_code(code))

