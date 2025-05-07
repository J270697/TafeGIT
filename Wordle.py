import random



def target_word():
    '''
    Function: target_word()
    Purpose: Encapsulate logic for reading the target_words.txt file and picking a random word to be used in Wordle game for answer
    '''
    with open("target_words.txt", 'r') as target_words:
        unconverted_tw_list = target_words.readlines()
        target_words_list = []
        for line in unconverted_tw_list:
            target_words_list.append(line.strip())

    return random.choice(target_words_list)

# guess = "world"
# target_word = "world"


# def score_guess(guess, target_word):
#     score = [0] * len(target_word)
#     if guess == target_word:


def rules():
    print('''\nRules:
    - Test
    - Test 2\n''')

guess_count = 0
answer = target_word()


while True:
    answer_chars = list(answer)
    score = [0] * len(answer)
    print(f"Cheats: {answer}")
    print("Welcome to Wordle game")
    print("Type the word '/rules' if you need help")

    print("You have", 6 - guess_count, "guesses remaining")
    guess = input("Guess the word: ").lower().strip()

    if guess in ["/rules", "/rule", "/r"]:
        rules()
        continue

    if len(guess) < len(answer):
        print("not enough characters")
        continue

    if len(guess) > len(answer):
        print("too many characters")
        continue

    with open("all_words.txt", 'r') as valid_words:
        valid_guess = False
        line_read = valid_words.readlines()
        for line in line_read:
            if line.strip() == guess:
                valid_guess = True
                break

    if not valid_guess:
        print("Not a word in dictionary")
        continue

    if guess == answer:
        print("Congrats! The word was " + answer + ". \nYou guessed " + str(guess_count) + " times!")
        break

    # Loop through
    for num in range(len(guess)):
        if guess[num] == answer[num]:
            score[num] = 2
            answer_chars[num] = None

    for num in range(len(guess)):
        if score[num] == 0 and guess[num] in answer_chars:
            score[num] = 1
            answer_chars[answer_chars.index(guess[num])] = None
    print(*guess.upper(), sep= ' ')
    print(*score, sep= ' ')


    guess_count += 1
    if guess_count >= 6:
        print("You lost! The word was " + answer)
        break