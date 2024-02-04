import random
easyq = {
    0: {"eq": "Who is the main character of Garden of Sinners?\nA. Tomoe Enjou\nB. Mana Ryougi\nC. Shiki Ryougi\nD. Mikiya Kokutou", "ea": "C"},
    1: {"eq": "What movie takes place first in the series in chronological order?\nA. Movie 1\nB. Movie 2\nC. Movie 3\nD. Movie 4", "ea": "B"},
    2: {"eq": "Who is the main villain of the first movie?\nA. Kirie Fujou\nB. Lio Shirazumi\nC. Fujino Asagami\nD. Souren Araya", "ea": "A"},
    3: {"eq": "What movie takes place fourth in the series in chronological order?\nA. Movie 1\nB. Movie 2\nC. Movie 3\nD. Movie 4", "ea": "A"},
    4: {"eq": "Who's the third main character of the 5th movie?\nA. Mana Ryougi\nB. Meruka Kuramitsu\nC. Tomoe Enjou\nD. Shizune Seo", "ea": "C"},
    5: {"eq": "What did Shiki fight in Movie 4?\nA. Ghosts\nB. A zombie\nC. Multiple zombies\nD. Mages", "ea": "B"}
}

midq = {
    0: {"eq": "What got Shiki Ryougi into a coma?\nA. Mage Fight\nB. Araya's First Fight\nC. Zombie Fight\nD. Car Crash", "ea": "D"},
    1: {"eq": "Who helped create Shiki's fake arm?\nA. Mikiya Kokutou\nB. Azaka Kokutou\nC. Aoko Aozaki\nD. Touko Aozaki", "ea": "D"},
    2: {"eq": "Why did the Enjou family constantly move?\nA. Enjou's dad killed someone in a traffic accident\nB. Enjou was forced to kill his parents\nC. People keep bullying Enjou\nD. Enjou was a star sprinter", "ea": "A"},
    3: {"eq": "What flavor of ice cream is often mentioned in the series?\nA. Chocolate\nB. Strawberry\nC. Vanilla\nD. Raspberry", "ea": "B"},
    4: {"eq": "How does Touko's second body compare to her first?\nA. Second body is better\nB. Second body is worse\nC. Second body is equal\nD. None of the above", "ea": "C"},
    5: {"eq": "What do people mistake Mikiya's job to be?\nA. Swordsman\nB. Detective\nC. Accountant\nD. Poet", "ea": "B"}
}

hardq = {
    0: {"eq": "Which story order matches the 5th movie?\nA. Shiki, Mikiya, Enjou\nB. Enjou, Mikiya, Shiki\nC. Mikiya, Shiki, Enjou\nD. Enjou, Shiki, Mikiya", "ea": "A"},
    1: {"eq": "Which tie below did Shiki not cut in the series?\nA. Future Vision\nB. Ghosts\nC. Prophecies\nD. Boundary Fields", "ea": "C"},
    2: {"eq": "What is Souren Araya's origin?\nA. Nothingness\nB. Stillness\nC. Consumption\nD. Taboo", "ea": "B"},
    3: {"eq": "What part of Tomoe Enjou was key to helping Shiki defeating Souren Araya?\nA. His sprinting power\nB. His love for Shiki\nC. His love for his family\nD. Enjou's puppet status", "ea": "C"},
    4: {"eq": "What nickname does Touko Aozaki hate being called?\nA. Projection Girl\nB. Headless Witch\nC. Dirty Mage\nD. Dirty Red", "ea": "D"},
    5: {"eq": "Which character from Garden of Sinners also appeared in Fate/Zero?\nA. Cornelius Alba\nB. Touko Aozaki\nC. Shiki Ryougi\nD. Azaka Kokutou", "ea": "A"}
}

extraq = {
    0: {"eq": "What is the ending song name of Paradox Spiral?\nA. Oblivious\nB. Aria\nC. Sprinter\nD. Fairytale", "ea": "C"},
    1: {"eq": "Who doesn't have future vision?\nA. Touko Aozaki\nB. Shizune Seo\nC. Mother of Mifune\nD. Mitsuru Kamekura", "ea": "A"},
    2: {"eq": "Who's the main antagonist of the 3rd movie?\nA. Kirie Fujou\nB. Lio Shirazumi\nC. Fujino Asagami\nD. Souren Araya", "ea": "C"},
    3: {"eq": "What's the name of Shiki's special eyes?\nA. Mystic Eyes of Precognition\nB. Mystic Eyes of Flame\nC. Mystic Eyes of Charm\nD. Mystic Eyes of Death Perception", "ea": "D"},
    4: {"eq": "Which of the ending songs is the most popular?\nA. Oblivious\nB. Sprinter\nC. Seventh Heaven\nD. Kizuato", "ea": "A"}
}

def main():
    diff = input("Welcome to the Garden of Sinners Trivia Game!\nThis game will contain at least 6 questions.\nWhat difficulty do you want to play on?\n(Respond with (e) for easy, (m) for medium, and (h) for hard.)\n")
    while not valid_diff(diff):
        print("\n----Invalid Input----\n")
        diff = input("Welcome to the Garden of Sinners Trivia Game!\nThis game will contain at least 6 questions.\nWhat difficulty do you want to play on?\n(Respond with (e) for easy, (m) for medium, and (h) for hard.)\n")
    #easy mode
    print()
    score = 0
    if diff == 'e':
        for i in range(6):
            print(easyq[i]["eq"])
            ans = input("Answer: ").strip().upper()
            if ans == easyq[i]["ea"]:
                score += nscore(diff, i)
                print(f"That is correct! You currently have {score} points! :D\n")
            else:
                print(f"Sorry, that's wrong. The correct answer is {easyq[i]["ea"]}. You currently have {score} points.\n")
        print(f"You scored {score} points!")

    #medium mode
    elif diff == 'm':
        for i in range(6):
            print(midq[i]["eq"])
            ans = input("Answer: ").strip().upper()
            if ans == midq[i]["ea"]:
                score += nscore(diff, i)
                print(f"That is correct! You currently have {score} points! :D\n")
            else:
                print(f"Sorry, that's wrong. The correct answer is {midq[i]["ea"]}. You currently have {score} points.\n")
        print(f"You scored {score} points!")

    #Hard mode
    else:
        for i in range(6):
            print(hardq[i]["eq"])
            ans = input("Answer: ").strip().upper()
            if ans == hardq[i]["ea"]:
                score += nscore(diff, i)
                print(f"That is correct! You currently have {score} points! :D\n")
            else:
                print(f"Sorry, that's wrong. The correct answer is {hardq[i]["ea"]}. You currently have {score} points.\n")
        print(f"You scored {score} points!")
    feel = int(input("On a score from 1 to 10, how do you feel about the game so far? "))
    want = input("Do you want to spend 4 points for a bonus question? (87% Success Rate) ").lower().strip()
    if want == 'yes' or want == 'y':
        score -= 4
        funny = int(input("Pick a number from 1 to 8: "))
        while funny < 1 or funny > 8:
            print("Number is outside range.")
            funny = int(input("Pick a number from 1 to 8: "))
        funny = order(funny)
        score2 = funalg(funny, feel)
        quest = random.randint(0, 4)
        print(extraq[quest]["eq"])
        ans = input("Answer: ").strip().upper()
        if ans == extraq[quest]["ea"]:
            score += score2
            print(f"That is correct! You currently have {score} points! Good game!\n")
            if funny < 0:
                print("Sorry about the point drop. It's unfortunate Movie 6 is very different from the source material. :/")
        else:
            print(f"Sorry, that's wrong. The correct answer is {midq[i]["ea"]}. You currently have {score} points.\n")
    else:
        print(f"Your score: {score}")

def valid_diff(diff):
    return diff in ["e", "m", "h"]

def nscore(diff, q):
    if q < 0 or q > 5:
        return 0
    if diff == 'e':
        return q + 1
    elif diff == 'm':
        return 3*q+2
    elif diff == 'h':
        return 5*q+3

def order(num):
    if num == 1:
        return 4
    if num == 2:
        return 1
    if num == 3:
        return 3
    if num == 4:
        return 2
    if num == 6:
        return -5
    else:
        return order(num - 4) + 4

def funalg(funny, feel):
    if feel < 0 or feel > 10:
        return -10
    else:
        return funny * feel

if __name__ == "__main__":
    main()
