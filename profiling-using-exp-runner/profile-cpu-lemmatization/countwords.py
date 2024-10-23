
input_size_options = [
    "Running quickly, the children played happily in the sunny park, unaware of the approaching storm.",

    """In the midst of the bustling city, there lies a forgotten garden. Overgrown with wildflowers and vines, 
    it stands as a remnant of a bygone era. The air is filled with the scent of blooming roses, and the sound of 
    chirping birds creates a symphony that contrasts sharply with the distant hum of traffic. This hidden oasis 
    provides a sanctuary for those seeking peace and a respite from the relentless pace of modern life.""",

    """In the vast expanse of the digital universe, information flows like an endless river, touching every 
    corner of the globe. The advent of the internet has revolutionized the way we communicate, learn, and conduct 
    business. With just a few clicks, we can access a wealth of knowledge that was unimaginable just a few 
    decades ago. However, this immense connectivity also brings challenges. The sheer volume of data generated 
    every second requires sophisticated algorithms and technologies to process and make sense of it. Artificial 
    intelligence and machine learning have become integral in managing this data deluge, enabling us to extract 
    insights and make informed decisions.Moreover, the rise of social media platforms has transformed how we 
    interact with one another."""
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
