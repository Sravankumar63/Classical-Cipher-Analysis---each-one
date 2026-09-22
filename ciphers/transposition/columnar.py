from core.cipher import Cipher
from core.validators import validate_text,validate_keyword
from core.exceptions import InvalidKeyError
class ColumnarTranspositionCipher(Cipher):
    def _order(self,key):
        key=validate_keyword(key,True)
        if len(set(key))!=len(key):raise InvalidKeyError("Columnar key must contain unique letters.")
        return key,sorted(range(len(key)),key=lambda i:key[i])
    def encrypt(self,text,key):
        text=validate_text(text);key,order=self._order(key);cols=len(key);rows=[text[i:i+cols] for i in range(0,len(text),cols)];return ''.join(row[c] for c in order for row in rows if c<len(row))
    def decrypt(self,text,key):
        text=validate_text(text);key,order=self._order(key);cols=len(key);rc=(len(text)+cols-1)//cols;rem=len(text)%cols;lengths=[rc]*cols
        if rem:
            for c in range(rem,cols):lengths[c]-=1
        data=['']*cols;i=0
        for c in order:data[c]=text[i:i+lengths[c]];i+=lengths[c]
        return ''.join(data[c][r] for r in range(rc) for c in range(cols) if r<len(data[c]))
