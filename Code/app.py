"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
import string
import random
from higher_order_markov import HigherOrderMarkovChain, generate_random_sentence

app = Flask(__name__)

# Initialize HigherOrderMarkovChain.
source_path = 'little_women.txt'
with open(source_path, 'r') as file:
    source_text = file.read()
    translator = str.maketrans("", "", string.punctuation + "“”‘’")
    word_list = source_text.translate(translator).split()

chain = HigherOrderMarkovChain()
chain.learn(word_list)


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    start_index = random.randint(0, len(word_list) - 2)
    start_words = (word_list[start_index], word_list[start_index + 1])
    sentence = ' '.join(chain.random_walk(start_words, 18))
    return render_template("littlewomen.html", sentence=sentence)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
