# Classical Cipher Lab

Educational Python/Streamlit implementation of 15 classical cipher algorithms with encryption, decryption, frequency analysis and heuristic cryptanalysis.

## Cipher Families
- Substitution: Caesar, Atbash, Affine, Monoalphabetic, Homophonic
- Polyalphabetic: Vigenere, Beaufort, Variant Beaufort
- Transposition: Rail Fence, Columnar, Route
- Polygraphic: Playfair, Hill, Bifid, Trifid

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

Cryptanalysis outputs are statistical/heuristic and are not guaranteed to recover the original key.