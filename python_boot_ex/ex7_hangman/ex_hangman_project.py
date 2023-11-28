

"""
app.diagrams.net에서 행맨 게임을 어떻게 구상할 것인지
flowchart로 먼저 만들어보자.
ex7의 다이어그램 xml_list -> ex7

순서도는 코드를 짜는 동안에도 굉장히 참고를 많이하게 되는
좋은 도구이다.
왜냐하면 순서도는 어떻게 코드를 짤지에 대해 전반적인 방향성을 제시하기 때문이다.
"""
import random
import ex_art
import ex_words

# blank_len = 0
stages = ex_art.stages
lives = len(stages) - 1
display = []

choose_word = random.choice(ex_words.word_list)
letter = list(choose_word)

print(ex_art.logo)
print(f'Pssst, the solution is {choose_word}')

for i in range(0, len(letter)):
    display.append("_")

# step 3에서 솔루션과 나의 정답이 갈린다.
"""
나의 정답
for i in range(0, len(letter)):
    display.append("_")
    blank_len += 1

while blank_len > 0:
    guess = input('Guess a letter: ').lower()
    chk = False
    for idx, item in enumerate(letter):
        if item == guess:
            display[idx] = item
            blank_len -= 1
    print(display)
"""

# 솔루션 정답.
end_of_game = False
while not end_of_game:
    guess = input('Guess a letter: ').lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for idx, item in enumerate(letter):
        if item == guess:
            display[idx] = item

    if guess not in letter:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1

    if lives == 0:
        end_of_game = True
        print("You lose.")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(display)
    print(stages[lives])

"""
step5 중간 강사 말에
모든 코드는 디버그하기 쉽게 짜도록 말한다.

"""