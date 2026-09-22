from core.cipher import Cipher
from core.validators import validate_text, validate_keyword
from core.exceptions import InvalidKeyError
class PlayfairCipher(Cipher):
    def _m(self,key):
        key=validate_keyword(key,allow_spaces=True);seq=""
        for c in key+"ABCDEFGHIKLMNOPQRSTUVWXYZ":
            c="I" if c.upper()=="J" else c.upper()
            if c not in seq:seq+=c
        return [seq[i:i+5] for i in range(0,25,5)]
    def _p(self,m,c):
        c="I" if c=="J" else c
        for r in range(5):
            for k in range(5):
                if m[r][k]==c:return r,k
        raise InvalidKeyError("Character not found in Playfair square.")
    def _pairs(self,t):
        t=''.join(c.upper() for c in t if c.isalpha()).replace('J','I');out=[];i=0
        while i<len(t):
            a=t[i]
            if i+1>=len(t):out.append(a+'X');i+=1
            elif t[i+1]==a:out.append(a+'X');i+=1
            else:out.append(a+t[i+1]);i+=2
        return out
    def encrypt(self,text,key):
        m=self._m(key);out=''
        for a,b in self._pairs(validate_text(text)):
            r1,c1=self._p(m,a);r2,c2=self._p(m,b)
            if r1==r2:out+=m[r1][(c1+1)%5]+m[r2][(c2+1)%5]
            elif c1==c2:out+=m[(r1+1)%5][c1]+m[(r2+1)%5][c2]
            else:out+=m[r1][c2]+m[r2][c1]
        return out
    def decrypt(self,text,key):
        t=''.join(c.upper() for c in validate_text(text) if c.isalpha()).replace('J','I');t+=('X' if len(t)%2 else '');m=self._m(key);out=''
        for i in range(0,len(t),2):
            r1,c1=self._p(m,t[i]);r2,c2=self._p(m,t[i+1])
            if r1==r2:out+=m[r1][(c1-1)%5]+m[r2][(c2-1)%5]
            elif c1==c2:out+=m[(r1-1)%5][c1]+m[(r2-1)%5][c2]
            else:out+=m[r1][c2]+m[r2][c1]
        return out
