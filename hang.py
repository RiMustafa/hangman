import random
import requests
#Requests is a package that has random words so the game can essentially be endless with words

def get_random_word():
  try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        response.raise_for_status()
        word = response.json()[0].upper()
        return word
  except requests.RequestException as e:
        print(f"Error fetching word: {e}")
        # Fallback to a predefined list in case of an error, just incase of error in the pull req
        fallback_words = [
            "PYTHON", "DEVELOPER", "HANGMAN", "COMPUTER", "PROGRAMMING"
        ]
        return random.choice(fallback_words).upper()
  
  def display_hangman(tries):
       stages = [
            """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
  return stages[tries]

def play(word):
     word_completion -"_" * len(word)
     guessed = False
     