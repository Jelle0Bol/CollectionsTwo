
import random

def show_rolls(dice):
    print("De dobbelstenen zijn :\n", end = '')
    for d in dice:
        print(str(d) + ' ', end='') 

score = 0
score_list = []

game_over = False
while not game_over:
    dice = []
    for d in range(5):
        dice.append(random.randint(1,6))

    show_rolls(dice)

    for x in range(2):
        reroll = input("\nWelke dobbelsteen wil je opnieuw gooien? : ")
        reroll = reroll.split() # Maakt een list
        for index, ch in enumerate(reroll):
            reroll[index] = int(ch) - 1

        for index in reroll:
            dice[index] = random.randint(1,6)

        show_rolls(dice)

    number_valid = False
    while not number_valid:
        number_to_score = int(input("Op welke nummer wil je scoren? : "))

        if number_to_score not in score_list:
            number_valid = True
        else:
            print("Je hebt al gescoord met dat nummer")
            print("Jouw gescoorde nummers zijn : ", end='')
            for num in score_list:
                print(str(num) + ' ', end='')
            print()

    score_list.append(number_to_score)

    for d in dice:
        if d == number_to_score:
            score += d

    print("Jouw score is " + str(score))

    if len(score_list) == 6:
        game_over = True