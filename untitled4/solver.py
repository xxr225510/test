import math
import random



class solver:
    def demo(self):
        with open('/Users/huijia/Desktop/sowpods.txt','r')as open_file:
            t=open_file.readlines()

        word =random.choice(t)
        word = list(word)
        guessed=[]
        print word


        def game():
            board = "_" * len(word)
            board=list(board)

            guess=0
            while True:

                    letter=raw_input("guess a letter:")
                    letter=letter.upper()


                    if letter in word:
                        index = word.index(letter)
                        board[index] = letter
                        word[index] = '_'
                        print (" ".join(board))
                        guess +=1

                    elif "_" not in board:
                        print ("game over.")
                        break
                    elif letter in guessed:
                        print ("you have guessed this letter")
                        print board
                        guess += 1
                    elif letter not in word:
                        print("letter is wrong")
                        print " ".join(board)
                        guess += 1
                        guessed.append(letter)
                    elif guess==6:
                        print "game over."
                    break
            return game()
        game()





solver().demo()