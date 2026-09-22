from .exceptions import InvalidKeyError,InvalidInputError
def validate_text(text):
    if text is None or not str(text).strip():raise InvalidInputError("Input text cannot be empty.")
    return str(text)
def validate_caesar_key(key):
    try:return int(key)%26
    except:raise InvalidKeyError("Caesar key must be an integer.")
def validate_keyword(key,allow_spaces=False):
    if key is None or not str(key).strip():raise InvalidKeyError("Keyword cannot be empty.")
    k=''.join(str(key).split()).upper() if allow_spaces else str(key).upper()
    if not k.isalpha():raise InvalidKeyError("Keyword must contain alphabetic characters only.")
    return k
