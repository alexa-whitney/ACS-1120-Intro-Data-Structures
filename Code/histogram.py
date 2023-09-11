import random
import string


def histogram(source_text):
    """Generate a histogram from a source text file."""
    with open(source_text, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        # Remove punctuation from text
        translator = str.maketrans('', '', string.punctuation + '“”‘’')
        text = text.translate(translator)
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


def random_word(hist):
    """Return a random word from the histogram, not based on frequency."""
    return random.choice(list(hist.keys()))


def weighted_random_word(hist):
    """Return a random word from the histogram based on frequency."""
    weighted_words = []
    for word in hist:
        for i in range(hist[word]):
            weighted_words.append(word)
    return random.choice(weighted_words)


if __name__ == '__main__':
    source_path = "/Users/alexawhitney/Desktop/Dominican ACS Courses/Fall 2023/andersen_fairy_tales.txt"
    hist = histogram(source_path)

    # Testing pure randomness:
    print(random_word(hist))

    # Testing weighted randomness:
    test_runs = 10000
    test_results = {}
    for _ in range(test_runs):
        word = weighted_random_word(hist)
        test_results[word] = test_results.get(word, 0) + 1

    # Display 20 random results:
    sample_20_words = random.sample(list(test_results.keys()), 20)
    for word in sample_20_words:
        print(f"{word} => {test_results[word]}")

    # Display the top 20 results:
    top_20_words = sorted(
        test_results, key=test_results.get, reverse=True)[:20]
    for word in top_20_words:
        print(f"{word} => {test_results[word]}")
