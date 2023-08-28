import sys
import random

# Get random words using the words.txt file
def get_random_words(word_count):
    """Select and return a list of random words from the dictionary."""
    # Open the file
    with open('/usr/share/dict/words', 'r') as f:
        # Read the file and split into a list of words
        words = f.read().split()
        # Select a random set of words from the file and store in a data type (list)
        random_words = random.sample(words, min(word_count, len(words)))
        # Return the data type
        return random_words

def generate_random_sentence():
    num_words = int(sys.argv[1])
    random_words = get_random_words(num_words)
    
    # Capitalize the first word
    random_words[0] = random_words[0].capitalize()

    # Create a sentence from the list of random words
    random_sentence = ' '.join(random_words) + '.'
    print(random_sentence)

if __name__ == '__main__':
    generate_random_sentence()
