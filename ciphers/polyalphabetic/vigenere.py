from core.cipher import Cipher
from core.validators import validate_text, validate_keyword

class VigenereCipher(Cipher):
    def encrypt(self,text,key):
        text=validate_text(text); key=validate_keyword(key,allow_spaces=True); result=""; i=0
        for char in text:
            if char.isalpha():
                shift=ord(key[i%len(key)])-65; base=65 if char.isupper() else 97
                result+=chr((ord(char)-base+shift)%26+base); i+=1
            else: result+=char
        return result
    def decrypt(self,text,key):
        text=validate_text(text); key=validate_keyword(key,allow_spaces=True); result=""; i=0
        for char in text:
            if char.isalpha():
                shift=ord(key[i%len(key)])-65; base=65 if char.isupper() else 97
                result+=chr((ord(char)-base-shift)%26+base); i+=1
            else: result+=char
        return result
