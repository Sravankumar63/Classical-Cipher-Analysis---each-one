from cryptanalysis.chi_square import chi_square_score
from cryptanalysis.ioc import index_of_coincidence
from cryptanalysis.ngram import ngram_score

def statistical_summary(text):
    return {
        "chi_square": chi_square_score(text),
        "ioc": index_of_coincidence(text),
        "ngram_score": ngram_score(text),
    }
