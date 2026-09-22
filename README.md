# Classical Cipher Lab

An interactive Python and Streamlit application for studying classical cryptography and cryptanalysis.

## Features

- 15 classical cipher algorithms
- Substitution, polyalphabetic, transposition, and polygraphic cipher families
- Encrypt and decrypt operations
- Analyze / Break workflow
- Frequency analysis
- Index of Coincidence (IoC)
- N-gram scoring
- Key-length analysis
- Candidate key and plaintext generation
- Step-by-step cipher explanations
- Interactive charts and results

## Ciphers

### Substitution
- Caesar
- Atbash
- Affine
- Monoalphabetic Substitution
- Homophonic Substitution

### Polyalphabetic
- Vigenère
- Beaufort
- Variant Beaufort

### Transposition
- Rail Fence
- Columnar Transposition
- Route Cipher

### Polygraphic
- Playfair
- Hill
- Bifid
- Trifid

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure

The project is organized into separate modules for cipher implementations, cryptanalysis, analysis, UI components, language data, and tests.

## Purpose

This project is intended as an educational cybersecurity and cryptography lab for understanding how classical ciphers work and why statistical cryptanalysis can break many of them.
