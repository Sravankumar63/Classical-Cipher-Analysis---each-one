from core.cipher import Cipher
from core.validators import validate_text
from core.exceptions import InvalidKeyError
class MonoalphabeticCipher(Cipher):
    def _v(self,key):
        key=str(key or '').upper()
        if len(key)!=26 or not key.isalpha() or len(set(key))!=26:raise InvalidKeyError("Substitution key must contain 26 unique letters.")
        return key
    def encrypt(self,text,key):
        text=validate_text(text);key=self._v(key);return ''.join(key[ord(c)-65] if c.isupper() else key[ord(c)-97].lower() if c.islower() else c for c in text)
    def decrypt(self,text,key):
        text=validate_text(text);key=self._v(key);rev={key[i]:chr(65+i) for i in range(26)};return ''.join(rev[c] if c.isupper() else rev[c.upper()].lower() if c.islower() else c for c in text)
