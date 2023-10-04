from markov import MarkovChain
from listogram import Listogram
from collections import defaultdict
import string
import random


# The HigherOrderMarkovChain class inherits from MarkovChain
class HigherOrderMarkovChain(MarkovChain):
    def __init__(self, order=2):
        super().__init__()
        self.order = order

    def learn(self, word_list):
        """Learn from the given word list by building the second-order Markov chain."""
        for i in range(len(word_list) - self.order):
            current_state = tuple(word_list[i:i+self.order])
            next_word = word_list[i+self.order]
            
            if current_state in self:
                self[current_state].add_count(next_word)
            else:
                self[current_state] = Listogram([next_word])
                
            self.tokens += 1

    PROPER_NOUNS = {'jo', 'beth', 'laurie', 'amy', 'meg', 'march'}

    def random_walk(self, start_words, num_words):
        """Perform a random walk on this second-order Markov chain starting from the given word pair."""
        walk = [start_words[0], start_words[1]]  # Convert tuple to list
        for _ in range(num_words - 2):
            current_state = (walk[-2], walk[-1])  # Last two words
            if current_state in self:
                next_word = self[current_state].sample()
                if next_word in self.PROPER_NOUNS:
                    next_word = next_word.capitalize()
                walk.append(next_word)
            else:
                break
        walk[0] = walk[0].capitalize()
        return walk


def generate_random_sentence(chain, start_words, num_words=10):
    """Generate and print samples using the second-order Markov chain."""
    samples = chain.random_walk(start_words, num_words)
    end_punctuation = random.choice(['.', '.', '.', '!', '!', '?', '?', '...'])
    print('Random walk ({} words) beginning with the words "{} {}":'.format(
        num_words, start_words[0], start_words[1]))
    return ' '.join(samples) + end_punctuation


def main():
    text_file = "little_women.txt"
    with open(text_file, "r") as file:
        source_text = file.read()
    translator = str.maketrans("", "", string.punctuation + "“”‘’")

    # remove punctuations and split into words
    word_list = source_text.translate(translator).split()

    # Initialize the HigherOrderMarkovChain
    chain = HigherOrderMarkovChain()
    chain.learn(word_list)

    # Choose `order` consecutive words from the word list as the starting state
    start_index = random.randint(0, len(word_list) - chain.order)
    start_words = tuple(word_list[start_index:start_index + chain.order])

    num_words = 18
    generate_random_sentence(chain, start_words, num_words)


if __name__ == '__main__':
    main()
