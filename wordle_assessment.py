
#Travis Byrne, J270697, 03MAY25
import random



def target_word():
    """
    Function: target_word()
    Purpose: Reads the target_words.txt file and picks a random word to be used in Wordle game for answer
    """
    with open("target_words.txt", 'r') as target_words:
        unconverted_tw_list = target_words.readlines()
        target_words_list = []
        for line in unconverted_tw_list:
            target_words_list.append(line.strip())
        # for i in range(5):
        #     print(target_words_list[i])
        # for i in range((len(target_words_list) - 5), len(target_words_list)):
        #     print(target_words_list[i])

    return random.choice(target_words_list)

def all_words():
    with open("all_words.txt", 'r') as valid_words:
        unconverted_all_words = valid_words.readlines()
        all_words_list = []
        for line in unconverted_all_words:
            all_words_list.append(line.strip())
        # for i in range(5):
        #     print(all_words_list[i])
        # for i in range((len(all_words_list) - 5), len(all_words_list)):
        #     print(all_words_list[i])
    return all_words_list

def score_guess(guess, target_words):
    """
        Function: score_guess()
        Purpose: Calculates how each character scores, ranging from 0-2
        Description:
        1. 2 parameters
            1.a. guess = users guess
            1.b. target_word = answer user needs to guess
        2. Loops through each letter of guess and assigns score value
            2.a. Score values: 2 = correct letter and correct position, 1 = correct letter, incorrect position, 0 = incorrect letter
            2.b. Loop 1: sets 2 value for correct letter + position, and None in target_word_chars position when checked
            2.c. Loop 2: sets 1 value for correct letter + incorrect position, and None in target_word_chars for first found position checked
        3. Returns score of guess after comparing characters of guess and target_word
    """
    score = [0] * len(target_words)
    target_word_chars = list(target_words)

    for num in range(len(guess)):
        if guess[num] == target_words[num]:
            score[num] = 2
            target_word_chars[num] = None

    for num in range(len(guess)):
        if score[num] == 0 and guess[num] in target_word_chars:
            score[num] = 1
            target_word_chars[target_word_chars.index(guess[num])] = None


    return score

def audit_log(guess, answer, score):
    with open("log_date.log", 'a') as logfile:
        logfile.write("\n" + guess + " " + answer + " " + " " + score)

def rules():
    print("\nRules:")
    print("- Guess must be 5 letters")
    print("- Guess must be a word")
    print("\nScoring")
    print("0: Incorrect Letter")
    print("1: Letter in word, incorrect position")
    print("2: Letter in word, correct position\n")
    print("\n Example:")
    print("Answer: world")
    print("Guess: hello")
    print("H E L L O")
    print("0 0 0 2 1")



def game_loop():
    guess_count = 0
    answer = target_word()
    total_guess = 6


    cheats = True
    if cheats:
        print(f"Cheats: {answer}")

    #Intro
    print("Welcome to Wordle game")

    difficulty = int(input("What level? Easy, normal or hard? [1 = easy, 2 = normal, 3 = hard").strip())
    if difficulty == 1:
        total_guess += 1
    elif difficulty == 3:
        total_guess -= 1

    # Game Loop
    while True:

        print("\nType the word '/rules' if you need help")
        print("You have", total_guess - guess_count, "guesses remaining")

        #User Guess
        guess = input("Guess the word: ").lower().strip()

        #Input conditions for valid guess, if invalid, continues in order to not increment guess count by +1
        if guess in ["/rules", "/rule", "/r"]:
            rules()
            continue

        if len(guess) < len(answer):
            print("not enough characters (<5), try again")
            continue

        if len(guess) > len(answer):
            print("too many characters (>5), try again")
            continue

        if guess not in all_words():
            print("Not a word in dictionary, try again")
            continue

        #When all criteria met, score answer and display score
        score = score_guess(guess, answer)
        print(*guess.upper(), sep=' ')
        print(*score, sep=' ')


        guess_count += 1

        audit_log(guess, answer, str(score))

        #Win or lose criteria
        if score == [2,2,2,2,2]:
            print("\nCongrats! The word was " + answer + ". \nYou guessed " + str(guess_count) + " times!")
            break

        if guess_count >= total_guess:
            print("You lost! The word was " + answer)
            break

#Unit Tests
def test_word_in_dict():
    guess = "axbet"
    test_flag = True

    if guess not in all_words():
        test_flag = False

    try:
        assert test_flag == False
        print("Axbet test : Success!")
    except AssertionError:
        print("Axbet test : Failed")

    guess = "apple"
    test_flag = True

    if guess not in all_words():
        test_flag = False

    try:
        assert test_flag == True
        print("Apple test : Success!")
    except AssertionError:
        print("Apple test : Failed")


def test_score_guess():
    score = score_guess("hello", "world")
    try:
        assert score == [0,0,0,2,1]
        print("Score test : Success!")
    except AssertionError:
        print("Score test : Failed")

def run_tests():
    test_word_in_dict()
    test_score_guess()

# run_tests()
game_loop()
# target_word()
# all_words()





# #
# target_word()
# print(target_word())

#Test 1
#Arrange
# guess = "world"
# target_word = "hello"
#
# #Act
# act = score_guess(guess, target_word)
#
# #Assert
# assert act == [0,1,0,2,0]
#
# #Test 2
# #Arrange
# guess = "world"
# target_word = "world"
#
# #Act
# act = score_guess(guess, target_word)
#
# #Assert
# assert act == [2,2,2,2,2]
#
#
# #Returns [0,0,0,0,0]
# # print(score_guess("guess", "world"))