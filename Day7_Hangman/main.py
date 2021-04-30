import random
from Art import stages, logo
from Word import word_list

print(logo)
comp_selected_word = random.choice(word_list)
game_status = True
guess = ""
hang_count = 0
comp_guess = []

for i in range(0,len(comp_selected_word)):
    guess += '-'
    comp_guess += '-'
print(guess)

while game_status is True:
    print(stages[6-hang_count])
    user_guess = input('Guess a letter: ')
    if user_guess in comp_selected_word:
        for word in range(len(comp_selected_word)):
            if comp_selected_word[word] == user_guess:
                comp_guess[word] = user_guess
                print('Correct guess')
    else:
        print("You loose a life!")
        hang_count += 1
    print(f"{' '.join(comp_guess)}")

    if '-' not in comp_guess:
        game_status = False
        print('You Win!')
        break
    elif hang_count == 6:
        game_status = False
        print('You loose!')
        break