from cryptanalysis.frequency import clean_text, frequency_count

def analyze_input(text):
    cleaned = clean_text(text)
    return {
        "raw_length": len(text or ""),
        "clean_length": len(cleaned),
        "alphabetic_ratio": (len(cleaned) / len(text)) if text else 0.0,
        "unique_letters": len(set(cleaned)),
        "frequency": frequency_count(cleaned),
    }
