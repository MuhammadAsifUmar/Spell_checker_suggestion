#Muhammad Asif Umar Uet Mardan 

import enchant
from textblob import TextBlob

# Enchant for spell checking
d = enchant.Dict("en_US")

def spell_check_and_grammar(user_input):
    """Checks spelling and offers suggestions for grammar and misspelled words.

    Args:
        user_input (str): The sentence or text entered by the user.

    Returns:
        str: The original sentence with suggestions for spelling and grammar (if available).
    """

    corrected_text = ""
    words = user_input.lower().split()  # Split into lowercase words

    for word in words:
        if not d.check(word):  # Check spelling
            suggestions = d.suggest(word)
            if suggestions:
                corrected_text += f"{word} ({', '.join(suggestions)}) "
            else:
                corrected_text += word + " "  # Keep word as is if no suggestions
        else:
            corrected_text += word + " "  # Add correctly spelled word

    # Grammar correction suggestions using TextBlob (improved error handling)
    corrected_blob = TextBlob(corrected_text)
    try:
        grammar_suggestions = str(corrected_blob.corrections)  # Get suggestions (if available)
    except AttributeError:  # Handle potential 'corrections' attribute not existing
        grammar_suggestions = "Grammar correction unavailable."

    return f"Original sentence: {user_input}\n" \
           f"Spell check suggestions: {corrected_text.strip()}\n" \
           f"Grammar correction suggestions: {grammar_suggestions}\n" \
           f"Please review and make necessary corrections."

# User input with error handling
while True:
    try:
        user_sentence = input("Enter a sentence or text (or 'q' to quit): ")
        if user_sentence.lower() == 'q':
            break  # Exit loop on 'q' input
        corrected_output = spell_check_and_grammar(user_sentence)
        print(corrected_output)
    except (KeyboardInterrupt, SystemExit):  # Handle keyboard interrupt or system exit
        print("\nExiting program...")
        break

