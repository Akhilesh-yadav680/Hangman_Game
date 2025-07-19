# main.py

import tkinter as tk
from tkinter import font
import random
import string
from hang import word_list

# --- Constants for Styling ---
BG_COLOR = "#2c3e50"
TEXT_COLOR = "#ecf0f1"
CORRECT_COLOR = "#2ecc71"
WRONG_COLOR = "#e74c3c"
BUTTON_COLOR = "#34495e"
BUTTON_ACTIVE_COLOR = "#4a6278"
FONT_MAIN = ("Helvetica", 18)
FONT_WORD = ("Courier", 32, "bold")
FONT_MSG = ("Helvetica", 14)

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Hangman")
        self.root.config(bg=BG_COLOR, padx=20, pady=20)
        
        self.setup_ui()
        self.start_new_game()

    def setup_ui(self):
        # --- Canvas for Hangman Drawing ---
        self.canvas = tk.Canvas(self.root, width=250, height=300, bg=BG_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, rowspan=3, padx=20)

        # --- Word Display Label ---
        self.word_label = tk.Label(self.root, text="", font=FONT_WORD, bg=BG_COLOR, fg=TEXT_COLOR)
        self.word_label.grid(row=0, column=1, pady=(20, 10))

        # --- Message Label for Status ---
        self.message_label = tk.Label(self.root, text="", font=FONT_MSG, bg=BG_COLOR, fg=WRONG_COLOR)
        self.message_label.grid(row=1, column=1)

        # --- Keyboard Frame ---
        keyboard_frame = tk.Frame(self.root, bg=BG_COLOR)
        keyboard_frame.grid(row=2, column=1, pady=10)
        self.create_keyboard(keyboard_frame)
        
        # --- Play Again Button (initially hidden) ---
        self.play_again_button = tk.Button(self.root, text="Play Again", font=FONT_MAIN,
                                           bg=CORRECT_COLOR, fg="white", command=self.start_new_game)

    def create_keyboard(self, parent_frame):
        self.keyboard_buttons = {}
        letters = string.ascii_uppercase
        for i, letter in enumerate(letters):
            row, col = divmod(i, 7)
            button = tk.Button(parent_frame, text=letter, font=FONT_MAIN, width=4,
                               bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=BUTTON_ACTIVE_COLOR,
                               command=lambda l=letter: self.guess_letter(l))
            button.grid(row=row, column=col, padx=3, pady=3)
            self.keyboard_buttons[letter] = button

    def start_new_game(self):
        # --- Reset Game State ---
        self.lives = 6
        self.chosen_word = random.choice(word_list)
        self.guessed_letters = set()
        self.display_word = ["_" for _ in self.chosen_word]
        
        # --- Reset UI ---
        self.update_display()
        self.canvas.delete("all")
        self.draw_gallows()
        for button in self.keyboard_buttons.values():
            button.config(state="normal", bg=BUTTON_COLOR)
        self.play_again_button.grid_forget()

    def guess_letter(self, letter):
        self.guessed_letters.add(letter)
        
        # Disable the guessed button
        self.keyboard_buttons[letter].config(state="disabled", bg="#1e2b38")

        if letter in self.chosen_word:
            for index, char in enumerate(self.chosen_word):
                if char == letter:
                    self.display_word[index] = letter
            self.message_label.config(text=f"Correct! '{letter}' is in the word.", fg=CORRECT_COLOR)
        else:
            self.lives -= 1
            self.message_label.config(text=f"Wrong! '{letter}' is not in the word.", fg=WRONG_COLOR)
            self.draw_hangman_part()
        
        self.update_display()
        self.check_game_over()

    def update_display(self):
        self.word_label.config(text=" ".join(self.display_word))

    def check_game_over(self):
        if "_" not in self.display_word:
            self.message_label.config(text="🎉 Congratulations, You Win!", fg=CORRECT_COLOR)
            self.end_game()
        elif self.lives == 0:
            self.message_label.config(text=f"💀 Game Over! The word was: {self.chosen_word}", fg=WRONG_COLOR)
            self.end_game()

    def end_game(self):
        for button in self.keyboard_buttons.values():
            button.config(state="disabled")
        self.play_again_button.grid(row=3, column=1, pady=20)

    def draw_gallows(self):
        self.canvas.create_line(50, 280, 200, 280, fill=TEXT_COLOR, width=3) # Base
        self.canvas.create_line(100, 280, 100, 50, fill=TEXT_COLOR, width=3) # Pole
        self.canvas.create_line(100, 50, 180, 50, fill=TEXT_COLOR, width=3)  # Beam
        self.canvas.create_line(180, 50, 180, 80, fill=TEXT_COLOR, width=3)  # Rope

    def draw_hangman_part(self):
        part = 6 - self.lives
        if part == 1: # Head
            self.canvas.create_oval(160, 80, 200, 120, outline=TEXT_COLOR, width=3)
        elif part == 2: # Body
            self.canvas.create_line(180, 120, 180, 200, fill=TEXT_COLOR, width=3)
        elif part == 3: # Left Arm
            self.canvas.create_line(180, 140, 140, 170, fill=TEXT_COLOR, width=3)
        elif part == 4: # Right Arm
            self.canvas.create_line(180, 140, 220, 170, fill=TEXT_COLOR, width=3)
        elif part == 5: # Left Leg
            self.canvas.create_line(180, 200, 140, 240, fill=TEXT_COLOR, width=3)
        elif part == 6: # Right Leg
            self.canvas.create_line(180, 200, 220, 240, fill=TEXT_COLOR, width=3)


if __name__ == "__main__":
    root = tk.Tk()
    game_app = HangmanGame(root)
    root.mainloop()
