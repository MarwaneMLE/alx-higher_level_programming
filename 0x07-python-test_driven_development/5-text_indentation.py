#!/usr/bin/python3

def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of these character
    Args:
    text: is string
    """

    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty string to store the formatted text
    formatted_text = ""

    # Initialize a flag to prevent adding extra new lines
    new_line_flag = True

    # Iterate through the characters in the input text
    for char in text:
        if char in ('.', '?', ':'):
            # Add the punctuation character to the formatted text
            formatted_text += char

            # Add two new lines
            formatted_text += "\n\n"

            # Reset the new line flag to prevent extra new lines
            new_line_flag = True
        elif char != ' ':
            # If the character is not a space, add it to the formatted text
            formatted_text += char

            # Reset the new line flag
            new_line_flag = False
        elif not new_line_flag:
            # If the character is a space and the new line flag is not set, add it
            formatted_text += char

    print(formatted_text)

