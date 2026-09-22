from dataclasses import dataclass
from typing import Optional
@dataclass
class CipherResult:
    success: bool
    result: str=""
    key: Optional[str]=None
    message: str=""
