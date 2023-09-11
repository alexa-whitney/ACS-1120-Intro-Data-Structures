def histogram(source_text):
    """Generate a histogram from a source text file."""
    with open(source_text, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        words = text.split()

    hist = {}


    for word in words:
        if word in hist:
            hist[word] += 1
        else:
            hist[word] = 1

    return hist


def unique_words(hist):
    """Return the total count of unique words in the histogram."""
    return len(hist)


def frequency(word, hist):
    """Return the frequency of a word in the histogram."""
    return hist.get(word, 0)


if __name__ == '__main__':
    source_path = "/Users/alexawhitney/Desktop/Dominican ACS Courses/Fall 2023/andersen_fairy_tales.txt"
    hist = histogram(source_path)

    print("Total unique words:", unique_words(hist))
    word_to_check = "prince"  # Change this to whatever word you want to check
    print(f"Frequency of '{word_to_check}':", frequency(word_to_check, hist))
