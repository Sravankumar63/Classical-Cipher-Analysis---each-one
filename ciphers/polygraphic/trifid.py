from core.cipher import Cipher
from core.validators import validate_text, validate_keyword
class TrifidCipher(Cipher):
    def _create_cube(self,key):
        key=validate_keyword(key,allow_spaces=True);seq=""
        for c in key+"ABCDEFGHIJKLMNOPQRSTUVWXYZ+":
            if c not in seq:seq+=c
        return seq
    def _position(self,cube,char):
        i=cube.index(char);layer=i//9+1;r=i%9;return layer,r//3+1,r%3+1
    def _char(self,cube,l,r,c):return cube[(l-1)*9+(r-1)*3+(c-1)]
    def _prepare(self,text):return ''.join(c.upper() for c in text if c.isalpha())
    def encrypt(self,text,key):
        cube=self._create_cube(key);text=self._prepare(validate_text(text));coords=[]
        for c in text:coords.extend(self._position(cube,c))
        return ''.join(self._char(cube,coords[i],coords[i+1],coords[i+2]) for i in range(0,len(coords),3))
    def decrypt(self,text,key):
        cube=self._create_cube(key);text=self._prepare(validate_text(text));coords=[]
        for c in text:coords.extend(self._position(cube,c))
        n=len(text);return ''.join(self._char(cube,l,r,c) for l,r,c in zip(coords[:n],coords[n:2*n],coords[2*n:]))
