"""
A simple text based User Interface (UI) for the Adventure World game.
"""


class TextUI:

    def __init__(self):
        # Nothing to do...
        pass

    def get_command(self):
        """
            Fetches a command from the console.
        :return: a single string
        """
        word = None
        print('> ', end='')
        input_line = input()
        if input_line != "":
            all_words = input_line.split()
            word = all_words[0]

            # Just ignore any other words
        return (word)

    def print_to_textUI(self, text):
        """
            Displays text to the console.
        :param text: Text to be displayed
        :return: None
        """
        print(text)
