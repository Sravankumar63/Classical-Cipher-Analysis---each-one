from core.cipher import Cipher
from core.validators import validate_text, validate_keyword
class BifidCipher(Cipher):
    def _create_square(self,key):
        key=validate_keyword(key,allow_spaces=True); seq=""
        for c in key+"ABCDEFGHIKLMNOPQRSTUVWXYZ":
            c="I" if c=="J" else c
            if c not in seq: seq+=c
        return [seq[i:i+5] for i in range(0,25,5)]
    def _pos(self,s,c):
        c="I" if c=="J" else c
        for r in range(5):
            for col in range(5):
                if s[r][col]==c:return r+1,col+1
    def _char(self,s,r,c):return s[r-1][c-1]
    def _prep(self,t):return "".join(c.upper() for c in t if c.isalpha()).replace("J","I")
    def encrypt(self,text,key):
        s=self._create_square(key); t=self._prep(validate_text(text)); rows=[]; cols=[]
        for c in t:r,col=self._pos(s,c);rows.append(r);cols.append(col)
        z=rows+cols; return ''.join(self._char(s,z[i],z[i+1]) for i in range(0,len(z),2))
    def decrypt(self,text,key):
        s=self._create_square(key); t=self._prep(validate_text(text)); z=[]
        for c in t:z.extend(self._pos(s,c))
        h=len(z)//2; return ''.join(self._char(s,r,c) for r,c in zip(z[:h],z[h:]))
