input_size_options = [
    """In the midst of the bustling city, there lies a forgotten garden.""",

    """The sheer volume of data generated every second requires sophisticated algorithms and technologies to process and make sense of it.""",

    """The advent of the internet has revolutionized the way we communicate, learn, and conduct business. With just a few clicks, we can access a wealth of knowledge that was unimaginable just a few decades ago."""
]

def count_words(text):
    words = text.split()
    return len(words)

def main():
    for index, text in enumerate(input_size_options, start=1):
        word_count = count_words(text)
        print(f"sentence {index} : {word_count} words")

if __name__ == "__main__":
    main()
