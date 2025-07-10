# 🕹️ Hangman - Terminal Word Guessing Game

A simple terminal-based Hangman game written in Python. Choose a difficulty, get a category hint, and try to guess the hidden word one letter at a time. You only have 6 lives — use them wisely!

---

## 🎮 Features

- ✅ Difficulty selection: `easy`, `medium`, or `hard`
- ✅ Random word + hint from selected difficulty
- ✅ Letter-by-letter guessing
- ✅ Rejects invalid inputs (e.g., numbers, symbols, multiple letters)
- ✅ Prevents repeated guesses
- ❌ No color output yet
- ❌ No emojis yet
- ❌ No "Play Again" feature yet

---

## 🧠 How to Play

1. Run the script:
   ```bash
   python hangman.py

    Select a difficulty when prompted:

    Pick easy, medium or hard:

    Guess one letter at a time:

        If the letter is in the word, it gets revealed

        If not, you lose a life

        You have 6 lives total

    The game ends when:

        You reveal the whole word (🎉 you win!)

        You run out of lives (💀 you lose)

📦 Requirements

    Python 3.x

    random module (✅ built-in, no installation needed)

📋 Example

Pick easy, medium or hard: easy
pick a letter a-z, you have 6 lives. The hint is think of a Color.
You guessed: e ✅
You guessed: x ❌
...
You Win!
The word was: green

🔧 To Do

Add color feedback (e.g., red for wrong, green for correct)

Add emoji reactions (e.g., 😃, ❌, 💀)

Add "Play Again" menu

    Show win/loss statistics at the end

👨‍💻 Author

Created by @jakub_codes as part of a hands-on Python learning journey.


---

Let me know when you add more features and I’ll keep this README growing with you.
