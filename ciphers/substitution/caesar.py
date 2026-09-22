from core.cipher import Cipher
from core.validators import validate_text,validate_caesar_key
class CaesarCipher(Cipher):
    def encrypt(self,text,key):
        text=validate_text(text);key=validate_caesar_key(key);out=''
        for c in text:
            if c.isupper():out+=chr((ord(c)-65+key)%26+65)
            elif c.islower():out+=chr((ord(c)-97+key)%26+97)
            else:out+=c
        return out
    def decrypt(self,text,key):return self.encrypt(text,-validate_caesar_key(key))
