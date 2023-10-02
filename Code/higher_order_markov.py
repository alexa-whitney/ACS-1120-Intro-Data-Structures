from markov import MarkovChain
from listogram import Listogram
import string
import random

class HigherOrderMarkovChain(MarkovChain): # The HigherOrderMarkovChain class inherits from MarkovChain
    
    def learn(self, word_list):
        """Learn from the given word list by building the second-order Markov chain."""
        for i in range(len(word_list) - 2):  
            current_state = (word_list[i], word_list[i + 1])
            next_word = word_list[i + 2]
            
            if current_state in self:
                self[current_state].add_count(next_word)
            else:
                self[current_state] = Listogram([next_word])
                self.types += 1
            self.tokens += 1

    def random_walk(self, start_words, num_words):
        """Perform a random walk on this second-order Markov chain starting from the given word pair."""
        walk = list(start_words)  # Convert tuple to list
        for _ in range(num_words - 2):  
            current_state = (walk[-2], walk[-1])  # Last two words
            if current_state in self:
                next_word = self[current_state].sample()
                walk.append(next_word)
            else:
                break
        walk[0] = walk[0].capitalize()
        return walk

def generate_random_sentence(chain, start_words, num_words=10):
    """Generate and print samples using the second-order Markov chain."""
    samples = chain.random_walk(start_words, num_words)
    print('Random walk ({} words) beginning with the words "{} {}":'.format(num_words, start_words[0], start_words[1]))
    print(' '.join(samples) + '.')

def main():
    # Test the HigherOrderMarkovChain on words from "Little Women"
    text_file = "little_women.txt"
    source_text = open(text_file, "r").read()
    translator = str.maketrans("", "", string.punctuation + "“”‘’")

    # remove punctuations and split into words
    word_list = source_text.translate(translator).split()

    # Initialize the HigherOrderMarkovChain
    chain = HigherOrderMarkovChain()
    chain.learn(word_list)

    # Choose two consecutive words from the word list as the starting state
    start_index = random.randint(0, len(word_list) - 2)
    start_words = (word_list[start_index], word_list[start_index + 1])

    num_words = 18
    generate_random_sentence(chain, start_words, num_words)

if __name__ == '__main__':
    main()
