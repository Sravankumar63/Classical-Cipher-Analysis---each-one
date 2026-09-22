from core.cipher import Cipher
from core.validators import validate_text
from core.exceptions import InvalidKeyError
class RouteCipher(Cipher):
    def _v(self,key):
        try:r,c=key;r=int(r);c=int(c)
        except:raise InvalidKeyError("Route key must be (rows, columns).")
        if r<1 or c<1:raise InvalidKeyError("Rows and columns must be positive.")
        return r,c
    def encrypt(self,text,key):
        text=validate_text(text);r,c=self._v(key);g=[['']*c for _ in range(r)];i=0
        for x in range(r):
            for y in range(c):
                if i<len(text):g[x][y]=text[i];i+=1
        return ''.join(g[x][y] for y in range(c) for x in range(r) if g[x][y])
    def decrypt(self,text,key):
        text=validate_text(text);r,c=self._v(key);g=[['']*c for _ in range(r)];i=0
        for y in range(c):
            for x in range(r):
                if i<len(text):g[x][y]=text[i];i+=1
        return ''.join(g[x][y] for x in range(r) for y in range(c) if g[x][y])
