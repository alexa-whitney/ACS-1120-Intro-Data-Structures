def madlibs():
    # Get words from the user
    noun = input(f"Please provide a noun: ")
    verb = input(f"Please provide a verb: ")
    adjective = input(f"Please provide an adjective: ")
    adverb = input(f"Please provide an adverb: ")

    # Construct the mad lib story
    story = (f"On a sunny day, a {adjective} {noun} decided to {verb} "
             f"{adverb} at the zoo.")

    # Display the story
    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == '__main__':
    madlibs()