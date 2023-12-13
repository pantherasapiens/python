# Randomnumbers in Numpy
from numpy import random
import pygame

x = random.randint(100)
y = random.rand()
x1 = random.randint(100,size = (5))
x2 = random.randint(100, size = (3,5))
y1 = random.rand(5)
y2 = random.rand(3,5)
a = random.choice([3,5,7,9])
a1 = random.choice([3,5,7,9], size = (3,5))

Start = input("Welcome\nPress Anythng to Continue: ")
pygame.time.delay(10)
difficulty = input("Choose the difficulty level: ")
def game():
    if difficulty == 'a':
        info = input("Guess: ")
        if info == x:
            print("You won")
            return
        else:
            print("Try again!")
            game()
    elif difficulty == 'b':
        info = input("Guess: ")
        if info == x1:
            print("You won")
            return
        else:
            print("Try again!")
            game()
    elif difficulty == 'c':
        info = input("Guess: ")
        if info == x2:
            print("You won")
            return
        else:
            print("Try again!")
            game()
    elif difficulty == 'd':
        info = input("Guess: ")
        if info == y:
            print("You won")
            return
        else:
            print("Try again!")
            game()
    elif difficulty == 'e':
        info = input("Guess: ")
        if info == y1:
            print("You won")
            return
        else:
            print("Try again!")
            game()
    elif difficulty == 'f':
        info = input("Guess: ")
        if info == y2:
            print("You won")
            return
        else:
            print("Try again!")
            game()
    elif difficulty == 'g':
        info = input("Guess: ")
        if info == a:
            print("You won")
            return
        else:
            print("Try again!")
            game()
    elif difficulty == 'h':
        info = input("Guess: ")
        if info == a1:
            print("You won")
            return
        else:
            print("Try again!")
            game()

game()
