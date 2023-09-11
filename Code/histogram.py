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

def weighted_random_sentence(hist):
    """Generate a sentence with a random number of words based on their occurrence probabilities."""

    # Create a list where words appear multiple times based on their frequency
    weighted_words_list = []
    for word, frequency in hist.items():
        weighted_words_list.extend([word] * frequency)
    
    # Randomly determine the length of the sentence
    sentence_length = random.randint(5, 20)
    sentence = []

    # Randomly select words based on their weight for the determined length
    for _ in range(sentence_length):
        selected_word = random.choice(weighted_words_list)
        sentence.append(selected_word)

    return ' '.join(sentence)


if __name__ == '__main__':
    source_path = "/Users/alexawhitney/Desktop/Dominican ACS Courses/Fall 2023/little_women.txt"
    hist = histogram(source_path)

    # # Testing pure randomness:
    # print(random_word(hist))

    # # Testing weighted randomness:
    # test_runs = 10000
    # test_results = {}
    # for _ in range(test_runs):
    #     word = weighted_random_word(hist)
    #     test_results[word] = test_results.get(word, 0) + 1

    # # Display 20 random results:
    # sample_20_words = random.sample(list(test_results.keys()), 20)
    # for word in sample_20_words:
    #     print(f"{word} => {test_results[word]}")

    # # Display the top 20 results:
    # top_20_words = sorted(
    #     test_results, key=test_results.get, reverse=True)[:20]
    # for word in top_20_words:
    #     print(f"{word} => {test_results[word]}")

    # Test new functions
    print(f"Random word: {random_word(hist)}")
    print(f"Weighted random word: {weighted_random_word(hist)}")
    print(f"Weighted random sentence: {weighted_random_sentence(hist)}")
