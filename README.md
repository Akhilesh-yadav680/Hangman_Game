# Hangman Game 🎮

A modern and interactive Hangman game built with Python and Tkinter.

## Features

- GUI-based Hangman game using Tkinter
- Interactive keyboard with alphabetical buttons
- Dynamic canvas drawing for each hangman part
- Randomized word selection from a custom list
- Status messages and restart option

## Project Structure

```bash
.
├── app.py   # Main GUI game file
├── hangman.py                  # Console version for CLI play
├── hangman_words.py            # Word list, ASCII art, stages
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
Requirements
Install dependencies using:
pip install -r requirements.txt
Note: Tkinter is pre-installed with most Python versions. If not, use pip install tk or install it via your OS package manager.

How to Run
python "Hangman Game interface.py"
Optional
You can also run the CLI version:
python hangman.py
