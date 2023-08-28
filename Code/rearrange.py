import sys
import random

#Recieve arguments from command-line
words = sys.argv[1:]

#Shuffle words
random.shuffle(words)

#Join words
rearranged_words = ' '.join(words)

if __name__ == '__main__':
    print(rearranged_words)