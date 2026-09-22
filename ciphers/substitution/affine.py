from core.cipher import Cipher
from core.validators import validate_text
from core.exceptions import InvalidKeyError
class AffineCipher(Cipher):
    VALID_A_VALUES=[1,3,5,7,9,11,15,17,19,21,23,25]
    def _validate_key(self,a,b):
        try:a=int(a)%26;b=int(b)%26
        except:raise InvalidKeyError("Affine keys must be integers.")
        if a not in self.VALID_A_VALUES:raise InvalidKeyError("Invalid value for 'a'.")
        return a,b
    def _inv(self,a):
        for x in range(26):
            if a*x%26==1:return x
        raise InvalidKeyError("No modular inverse exists.")
    def encrypt(self,text,key):
        text=validate_text(text)
        if not isinstance(key,(tuple,list)) or len(key)!=2:raise InvalidKeyError("Affine key must be (a,b).")
        a,b=self._validate_key(*key);out=''
        for c in text:
            if c.isupper():out+=chr((a*(ord(c)-65)+b)%26+65)
            elif c.islower():out+=chr((a*(ord(c)-97)+b)%26+97)
            else:out+=c
        return out
    def decrypt(self,text,key):
        text=validate_text(text);a,b=self._validate_key(*key);ai=self._inv(a);out=''
        for c in text:
            if c.isupper():out+=chr((ai*((ord(c)-65)-b))%26+65)
            elif c.islower():out+=chr((ai*((ord(c)-97)-b))%26+97)
            else:out+=c
        return out
