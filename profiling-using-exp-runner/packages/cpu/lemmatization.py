#AI generated for explorative purposes

from functools import cache, lru_cache, wraps
import spacy
from time import perf_counter

def timer(func, *args, **kwargs):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        print(f'Starting {func.__name__} at {start}')   # 1
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f'Finished {func.__name__} at {end}')     # 3
        print(f"Elapsed time: {end - start}")           # 4
        return result                                   # 5                
    return wrapper

@timer
def measure_time(func: callable, *args, **kwargs):
    print(f"Calling {func.__name__} with args: {args}")  # 2
    return func(*args, **kwargs)

nlp = spacy.load("en_core_web_sm")

# Basic Implementation
def lemmatization_basic(nlp: spacy.language.Language, sentence: str) -> str:
    doc = nlp(sentence)
    lemmatized_sentence = ' '.join([token.lemma_ for token in doc])
    return lemmatized_sentence

# Using functools.cache (Python 3.9+)
@cache
def lemmatization_cache(nlp: spacy.language.Language, sentence: str) -> str:    
    doc = nlp(sentence)
    lemmatized_sentence = ' '.join([token.lemma_ for token in doc])
    return lemmatized_sentence

# Using functools.lru_cache
@lru_cache(maxsize=None)
def lemmatization_lru_cache(nlp: spacy.language.Language, sentence: str) -> str:
    doc = nlp(sentence)
    lemmatized_sentence = ' '.join([token.lemma_ for token in doc])
    return lemmatized_sentence

if __name__ == '__main__':
    # Example usage
    sentence = "The quick brown foxes are jumping over the lazy dogs"

    print(lemmatization(nlp, sentence))
    print(measure_time(lemmatization, nlp, sentence))
    
    print(measure_time(lemmatization_cache, nlp, sentence))
    print(measure_time(lemmatization_cache, nlp, sentence))

    print(measure_time(lemmatization_lru_cache, nlp, sentence))
    print(measure_time(lemmatization_lru_cache, nlp, sentence))

    assert lemmatization(nlp, sentence) == lemmatization_cache(nlp, sentence) == lemmatization_lru_cache(nlp, sentence)