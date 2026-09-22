from collections import Counter
from cryptanalysis.frequency import clean_text

def repeated_patterns(text, minimum=2, maximum=4):
    text = clean_text(text)
    results = {}
    for size in range(minimum, maximum + 1):
        counts = Counter(text[i:i+size] for i in range(len(text)-size+1))
        results[str(size)] = {k:v for k,v in counts.items() if v > 1}
    return results

def factor_lengths(length):
    if length < 2:
        return []
    return [n for n in range(2, min(length, 30)+1) if length % n == 0]
