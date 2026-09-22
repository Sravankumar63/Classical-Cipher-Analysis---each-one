import numpy as np
from core.cipher import Cipher
from core.validators import validate_text
from core.exceptions import InvalidKeyError
class HillCipher(Cipher):
    def _v(self,key):
        try:m=np.array(key,dtype=int)
        except:raise InvalidKeyError("Hill key must be a square matrix.")
        if m.ndim!=2 or m.shape[0]!=m.shape[1]:raise InvalidKeyError("Hill key must be a square matrix.")
        if np.gcd(round(np.linalg.det(m)),26)!=1:raise InvalidKeyError("Hill key matrix must be invertible modulo 26.")
        return m%26
    def _prep(self,t,n):
        t=''.join(c.upper() for c in t if c.isalpha()); return t+"X"*((n-len(t)%n)%n)
    def _proc(self,t,m):
        nums=[ord(c)-65 for c in t]; out=[]
        for i in range(0,len(nums),len(m)):out.extend(np.dot(m,np.array(nums[i:i+len(m)]))%26)
        return ''.join(chr(int(x)%26+65) for x in out)
    def _inv(self,m):
        d=round(np.linalg.det(m))%26; di=pow(int(d),-1,26)
        if len(m)!=2:raise InvalidKeyError("Currently Hill Cipher supports 2x2 matrices.")
        a=np.array([[m[1][1],-m[0][1]],[-m[1][0],m[0][0]]]);return di*a%26
    def encrypt(self,text,key):m=self._v(key);return self._proc(self._prep(validate_text(text),len(m)),m)
    def decrypt(self,text,key):m=self._v(key);return self._proc(self._prep(validate_text(text),len(m)),self._inv(m))
