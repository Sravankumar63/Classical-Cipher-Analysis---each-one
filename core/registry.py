class CipherRegistry:
    def __init__(self):self._ciphers={}
    def register(self,name,cipher):self._ciphers[name]=cipher
    def get(self,name):return self._ciphers.get(name)
    def available(self):return list(self._ciphers.keys())
