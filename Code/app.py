"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from histogram import histogram, weighted_random_sentence  # Importing functions from histogram.py


app = Flask(__name__)

# Initialize histogram.
source_path = '/Users/alexawhitney/Desktop/Dominican ACS Courses/Fall 2023/little_women.txt'
hist = histogram(source_path)  # Use the histogram function from histogram.py


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = weighted_random_sentence(hist)
    return render_template("littlewomen.html", sentence=sentence)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
