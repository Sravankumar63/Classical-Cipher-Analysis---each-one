from core.cipher import Cipher
from core.validators import validate_text, validate_keyword


class BeaufortCipher(Cipher):

    def encrypt(self, text, key):
        text = validate_text(text)
        key = validate_keyword(key, allow_spaces=True)

        result = ""
        key_index = 0

        for char in text:
            if char.isalpha():
                key_value = ord(key[key_index % len(key)]) - ord('A')
                if char.isupper():
                    text_value = ord(char) - ord('A')
                    result += chr((key_value - text_value) % 26 + ord('A'))
                else:
                    text_value = ord(char) - ord('a')
                    result += chr((key_value - text_value) % 26 + ord('a'))
                key_index += 1
            else:
                result += char
        return result

    def decrypt(self, text, key):
        return self.encrypt(text, key)
