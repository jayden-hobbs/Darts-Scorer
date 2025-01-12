#!/usr/bin/env python3

import sys
import random
import time

def setStartingScore():
    beginning_score = int(input("Enter the starting score: "))
    return beginning_score

def getNames():
    player1 = input("Enter the name of player 1: ").capitalize()
    player2 = input("Enter the name of player 2: ").capitalize()
    print("I will now choose at random who goes first.")
    time.sleep(2)
    starterNum = random.randint(1, 2)
    if starterNum == 1:
        print(f"{player1} goes first.")
    else:
        print(f"{player2} goes first.")
    return player1, player2, starterNum

def loadFinishes():
    finishes = {}
    with open("finishes.txt", "r") as f:
        for line in f:
            score, finish = line.strip().split(" ", 1)
            finishes[int(score)] = finish
    return finishes


def playGame(player1, player2, beginning_score, starterNum, finishes):
    p1score = beginning_score
    p2score = beginning_score
    currentPlayer = player1 if starterNum == 1 else player2

    while p1score > 0 and p2score > 0:
        print("\n" + "=" * 40)
        print(f"{currentPlayer}'s Turn".center(40))
        print("=" * 40)
        
        current_score = p1score if currentPlayer == player1 else p2score
        print(f"Score Remaining: {current_score}".center(40))

        if current_score <= 180 and current_score in finishes:
            print(f"Common Finish: {finishes[current_score]}".center(40))

        try:
            score = int(input(f"\n{currentPlayer}, enter your score: "))
            if score < 0 or score > 180:
                print("\nInvalid input. Please enter a number between 0 and 180.")
                continue

            new_score = current_score - score

            if new_score < 0:
                print("\nInvalid input. Your score cannot go below zero.")
                continue

            if currentPlayer == player1:
                p1score = new_score
                if p1score == 0:
                    print(f"\n{player1} wins!".center(40))
                    return
                currentPlayer = player2
            else:
                p2score = new_score
                if p2score == 0:
                    print(f"\n{player2} wins!".center(40))
                    return
                currentPlayer = player1

        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            continue

        print("=" * 40)



if __name__ == '__main__':
    print("Welcome to the dart scorer!".center(40))
    player1, player2, starterNum = getNames()
    beginning_score = setStartingScore()
    finishes = loadFinishes() 
    playGame(player1, player2, beginning_score, starterNum, finishes)







