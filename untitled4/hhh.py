import math
import random
import _File



class hhh:
    def demo(self):
        if __name__ == '__main__':
            print("Welcome to hangman!!")
            word = "EVAPORATE"
            guessed = "_" * len(word)
            word = list(word)
            guessed = list(guessed)
            lstGuessed = []
            letter = raw_input("guess letter: ")
            while True:
                if letter.upper() in lstGuessed:
                    letter = ''
                    print("Already guessed!!")
                elif letter.upper() in word:
                    index = word.index(letter.upper())
                    guessed[index] = letter.upper()
                    word[index] = '_'
                else:
                    print(''.join(guessed))
                    if letter is not '':
                        lstGuessed.append(letter.upper())
                    letter = raw_input("guess letter: ")

                if '_' not in guessed:
                    print("You won!!")
                    break






hhh().demo()