from core.cipher import Cipher
from core.validators import validate_text
class AtbashCipher(Cipher):
    def encrypt(self,text,key=None):
        text=validate_text(text);out=''
        for c in text:
            if c.isupper():out+=chr(90-(ord(c)-65))
            elif c.islower():out+=chr(122-(ord(c)-97))
            else:out+=c
        return out
    def decrypt(self,text,key=None):return self.encrypt(text)
