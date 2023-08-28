def reverse_words(sentence):
    """Reverse individual words in a given sentence."""
    words = sentence.split()  # Split sentence into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    return ' '.join(reversed_words)

def reverse_sentence(sentence):
    """Reverse the entire sentence."""
    return sentence[::-1]

def main():
    print("String Reversal Tool")
    print("1. Reverse individual words in a sentence.")
    print("2. Reverse the entire sentence.")

    choice = input("Please select an option (1 or 2): ")

    sentence = input("Enter the sentence to reverse: ")

    if choice == '1':
        print("Reversed words:", reverse_words(sentence))
    elif choice == '2':
        print("Reversed sentence:", reverse_sentence(sentence))
    else:
        print("Invalid choice!")

if __name__ == '__main__':
    main()