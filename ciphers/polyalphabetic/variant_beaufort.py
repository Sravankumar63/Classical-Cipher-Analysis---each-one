from core.cipher import Cipher
from core.validators import validate_text, validate_keyword


class VariantBeaufortCipher(Cipher):
    def encrypt(self, text, key):
        text = validate_text(text)
        key = validate_keyword(key, allow_spaces=True)
        result = ""; key_index = 0
        for char in text:
            if char.isalpha():
                kv = ord(key[key_index % len(key)]) - ord('A')
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char)-base+kv)%26+base)
                key_index += 1
            else: result += char
        return result
    def decrypt(self, text, key):
        text = validate_text(text); key = validate_keyword(key, allow_spaces=True)
        result = ""; key_index = 0
        for char in text:
            if char.isalpha():
                kv=ord(key[key_index%len(key)])-ord('A'); base=ord('A') if char.isupper() else ord('a')
                result += chr((ord(char)-base-kv)%26+base); key_index+=1
            else: result += char
        return result
