from markov import MarkovChain
from listogram import Listogram
from collections import defaultdict
import string
import random


# The HigherOrderMarkovChain class inherits from MarkovChain
class HigherOrderMarkovChain(MarkovChain):
    def __init__(self, order=2): 
        super().__init__() # Call the constructor of the parent class
        self.order = order # Add the order attribute

    def learn(self, word_list):
        """Learn from the given word list by building the second-order Markov chain."""
        for i in range(len(word_list) - self.order): # Loop through the word list
            current_state = tuple(word_list[i:i+self.order]) # Get the current state
            next_word = word_list[i+self.order] # Get the next word
            
            if current_state in self: # If the current state is already in the chain
                self[current_state].add_count(next_word) # Add the next word to the histogram
            else:
                self[current_state] = Listogram([next_word]) # Create a new histogram for the current state
                
            self.tokens += 1 # Increment the number of tokens

    PROPER_NOUNS = {'jo', 'beth', 'laurie', 'amy', 'meg', 'march'} # Set of proper nouns

    def random_walk(self, start_words, num_words):
        """Perform a random walk on this second-order Markov chain starting from the given word pair."""
        walk = [start_words[0], start_words[1]]  # Initialize the walk with the start words
        for _ in range(num_words - 2): # Loop until the walk is num_words long
            current_state = (walk[-2], walk[-1])  # Get the current state
            if current_state in self: # If the current state is in the chain
                next_word = self[current_state].sample() # Sample the next word
                if next_word in self.PROPER_NOUNS: # If the next word is a proper noun
                    next_word = next_word.capitalize() # Capitalize the next word
                walk.append(next_word) # Add the next word to the walk
            else:
                break # If the current state is not in the chain, break out of the loop
        walk[0] = walk[0].capitalize() # Capitalize the first word
        return walk


def generate_random_sentence(chain, start_words, num_words=10):
    """Generate and print samples using the second-order Markov chain."""
    samples = chain.random_walk(start_words, num_words) # Generate a random walk
    end_punctuation = random.choice(['.', '.', '.', '!', '!', '?', '?', '...']) # Choose a random end punctuation
    return ' '.join(samples) + end_punctuation # Return the samples joined by spaces and the end punctuation


def main():
    text_file = "little_women.txt" # Path to the text file
    with open(text_file, "r") as file: # Open the text file
        source_text = file.read() # Read the text file
    translator = str.maketrans("", "", string.punctuation + "“”‘’") # Create a translator to remove punctuation

    # Split the text into a list of words
    word_list = source_text.translate(translator).split()

    # Initialize the HigherOrderMarkovChain
    chain = HigherOrderMarkovChain()
    chain.learn(word_list)

    # Generate a random sentence
    start_index = random.randint(0, len(word_list) - chain.order)
    start_words = (word_list[start_index], word_list[start_index + 1]) # Get the start words
    # start_words = tuple(word_list[start_index:start_index + chain.order]) 

    num_words = 18
    generate_random_sentence(chain, start_words, num_words)


if __name__ == '__main__':
    main()
