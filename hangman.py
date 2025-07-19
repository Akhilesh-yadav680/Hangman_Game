# # while loop
# i=10
# while i>5:
#     print(i)
#     i-=1



# #  checking tghe guessed word  is present to the compueter guessed word
# import random
# my_list=["Akhilesh","Yadav","Muddam"]
# chosen_word=random.choice(my_list)
# print(chosen_word)
# user_input=(input("guess a letter ")).upper()
# print(user_input)
# for letter in chosen_word:
#     if letter==user_input:
#         print("Right")
#     else:
#         print("wrong")





# import random
# my_list=["Akhilesh","Yadav","Muddam"]
# chosen_word=random.choice(my_list)
# print(chosen_word)
# place_holder=""
# length=len(chosen_word)
# for item in range(0,length):
#     place_holder+="_"
# print(place_holder)
#
# user_input=(input("guess a letter ")).upper()
# print(user_input)
# display=" "
# for letter in chosen_word:
#     if letter==user_input:
#         display+=letter
#     else:
#         display+="_"
# print(display)


# import random
# my_list=["Akhilesh","Yadav","Muddam"]
# chosen_word=random.choice(my_list).lower()
# print(chosen_word)
# place_holder=""
# length=len(chosen_word)
# for item in range(0,length):
#     place_holder+="_"
# print(place_holder)
# game_over=False
# correct=[]
# while not game_over:
#     user_input=(input("guess a letter ")).lower()
#
#     display=""
#     for letter in chosen_word:
#         if letter==user_input:
#             display+=letter
#             correct.append(letter)
#         elif letter in correct:
#              display+=letter
#         else:
#             display+="_"
#     print(display)
#     if "_" not in display:
#         game_over=True
#         print("Game over")


# import random
# stages = [
#     # 0 lives remaining
#     '''
#       +---+
#       |   |
#       O   |
#      /|\\  |
#      / \\  |
#           |
#     =========
#     ''',
#     # 1 life remaining
#     '''
#       +---+
#       |   |
#       O   |
#      /|\\  |
#      /    |
#           |
#     =========
#     ''',
#     # 2 lives remaining
#     '''
#       +---+
#       |   |
#       O   |
#      /|\\  |
#           |
#           |
#     =========
#     ''',
#     # 3 lives remaining
#     '''
#       +---+
#       |   |
#       O   |
#      /|   |
#           |
#           |
#     =========
#     ''',
#     # 4 lives remaining
#     '''
#       +---+
#       |   |
#       O   |
#       |   |
#           |
#           |
#     =========
#     ''',
#     # 5 lives remaining
#     '''
#       +---+
#       |   |
#       O   |
#           |
#           |
#           |
#     =========
#     ''',
#     # 6 lives remaining
#     '''
#       +---+
#       |   |
#           |
#           |
#           |
#           |
#     =========
#     '''
# ]
# my_list=["Akhilesh","Yadav","Muddam"]
# lives=6
# chosen_word=random.choice(my_list).lower()
# print(chosen_word)
# place_holder=""
# length=len(chosen_word)
# for item in range(0,length):
#     place_holder+="_"
# print(place_holder)
# game_over=False
# correct=[]
# while not game_over:
#     user_input=(input("guess a letter ")).lower()
#
#     display=""
#     for letter in chosen_word:
#         if letter==user_input:
#             display+=letter
#             correct.append(letter)
#         elif letter in correct:
#              display+=letter
#         else:
#             display+="_"
#     print(display)
#     if user_input  not in chosen_word:
#         lives-=1
#         if lives==0:
#             game_over=True
#             print("Game over!run out of lives")
#     if "_" not in display:
#         game_over=True
#         print("you win")
#     print(stages[lives])



import random
from hangman_words import word_list
from hangman_words import logo
from hangman_words import stages
lives=6
print(logo)
chosen_word=random.choice(word_list).lower()
print(chosen_word)
place_holder=""
length=len(chosen_word)
for item in range(0,length):
    place_holder+="_"
print(place_holder)
game_over=False
correct=[]
while not game_over:
    print(f"**************************{lives}/6 LIVES LEFT************************ ")
    user_input=(input("Guess a letter ")).lower()
    if user_input in  correct:
        print(f"You have already guessed it before {user_input} ")
    display=""
    for letter in chosen_word:
        if letter==user_input:
            display+=letter
            correct.append(letter)
        elif letter in correct:
             display+=letter
        else:
            display+="_"
    print(display)
    if user_input  not in chosen_word:
        lives-=1
        print(f"you guessed  {user_input} that is not in the word you loose a life")
        if lives==0:
            game_over=True
            print(f"****************It was  {chosen_word.upper()}  Game over!run out of lives******************")
    if "_" not in display:
        game_over=True
        print("********************you win*************************")
    print(stages[lives])