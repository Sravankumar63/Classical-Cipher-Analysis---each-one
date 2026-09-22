from core.cipher import Cipher
from core.validators import validate_text
class HomophonicCipher(Cipher):
    DEFAULT_MAPPING={"A":["10","11","12"],"B":["13","14"],"C":["15","16"],"D":["17","18","19"],"E":["20","21","22","23"],"F":["24","25"],"G":["26","27"],"H":["28","29"],"I":["30","31","32"],"J":["33"],"K":["34"],"L":["35","36"],"M":["37","38"],"N":["39","40","41"],"O":["42","43","44","45"],"P":["46","47"],"Q":["48"],"R":["49","50","51"],"S":["52","53","54"],"T":["55","56","57","58"],"U":["59","60"],"V":["61"],"W":["62"],"X":["63"],"Y":["64"],"Z":["65"]}
    def __init__(self,mapping=None):
        self.mapping=mapping or self.DEFAULT_MAPPING;self.reverse_mapping={s:l for l,ss in self.mapping.items() for s in ss}
    def encrypt(self,text,key=None):
        text=validate_text(text);return ' '.join(self.mapping.get(c.upper(),[c])[0] if c.isalpha() else c for c in text)
    def decrypt(self,text,key=None):return ''.join(self.reverse_mapping.get(t,t) for t in validate_text(text).split())
