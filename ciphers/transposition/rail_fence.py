from core.cipher import Cipher
from core.validators import validate_text
from core.exceptions import InvalidKeyError
class RailFenceCipher(Cipher):
    def _v(self,k):
        try:k=int(k)
        except:raise InvalidKeyError("Number of rails must be an integer.")
        if k<2:raise InvalidKeyError("Number of rails must be at least 2.")
        return k
    def encrypt(self,text,key):
        text=validate_text(text);r=self._v(key)
        if r>=len(text):return text
        f=[[] for _ in range(r)];row=0;d=1
        for c in text:
            f[row].append(c);d=1 if row==0 else -1 if row==r-1 else d;row+=d
        return ''.join(''.join(x) for x in f)
    def decrypt(self,text,key):
        text=validate_text(text);r=self._v(key)
        if r>=len(text):return text
        pat=[];row=0;d=1
        for _ in text:
            pat.append(row);d=1 if row==0 else -1 if row==r-1 else d;row+=d
        lens=[pat.count(i) for i in range(r)];f=[];i=0
        for n in lens:f.append(list(text[i:i+n]));i+=n
        pos=[0]*r;return ''.join(f[x][pos[x]] for x in pat for _ in [pos.__setitem__(x,pos[x]+1)])
