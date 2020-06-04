import pytest
from cryptography.cryptography import encrypt, decryp, crack_code, is_broken

def test_encrypt_one():
    text = "ABCDE"
    key = 3
    expected = "DEFGH"

    actual = encrypt(text,key)

    assert actual == expected, 'Error encrypting 5 letters.'

def test_encrypt_two():
    text = "It was the best of times, it was the worst of times."    
    key = 13
    expected = "VG JnF Gur orFG Bs GvzrF, vG JnF Gur JBEFG Bs GvzrF."

    actual = encrypt(text,key)

    assert actual == expected, 'Error encrypting 12 words.'

def test_decryp_one():
    text = "VG JnF Gur orFG Bs GvzrF, vG JnF Gur JBEFG Bs GvzrF."
    key = 13
    expected = "It was the best of times, it was the worst of times."    

    actual = decryp(text,key)

    assert actual == expected, 'Error decrypting 12 words.'

def test_decryp_two():
    text = "MpsAly jvttvu Dvykz myvt kvjBtluAz"
    key = 7
    expected = "Filter common words from documents"    

    actual = decryp(text,key)

    assert actual == expected, 'Error decrypting 5 words.'

def test_crack_code_one():
    text = "MpsAly jvttvu Dvykz myvt kvjBtluAz"
    expected = "Filter common words from documents"    

    actual = crack_code(text)

    assert actual == expected, 'Error cracking 5 words.'

def test_crack_code_two():
    text = "PA Dhz Aol ilzA vm Aptlz, pA Dhz Aol DvyzA vm Aptlz."
    expected = "It was the best of times, it was the worst of times."    

    actual = crack_code(text)

    assert actual == expected, 'Error cracking 12 words.'

def test_crack_code_tree():
    text = "nBy xIA, NBy wuN, zCMB uHx LuvvCN uLy AIIx JyNM!"
    expected = "The dog, the cat, fish and rabbit are good pets!"    

    actual = crack_code(text)

    assert actual == expected, 'Error cracking sentence.'

def test_is_broken_one():
    text = "some uh when jds said"
    expected = "Only 3 from 5 words where recognized. There is a 60 % chance of being broken."    

    actual = is_broken(text)

    assert actual == expected, 'Error identifying if is a broken sentence.'

def test_is_broken_one():
    text = "The dog, the cat, fish and rabbit are good pets!"
    expected = "Only 9 from 10 words where recognized. There is a 90 % chance of being broken."    

    actual = is_broken(text)

    assert actual == expected, 'Error identifying if is a broken sentence.'