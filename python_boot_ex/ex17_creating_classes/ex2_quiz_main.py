from ex2_quiz_data import question_data
from ex2_quiz_question_model import Question
from ex2_quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

print("You've completed the quiz")
print(f"Your final score {brain.score}/{brain.q_number}")

"""
이와 같이 객체 지향 프로그래밍에 큰 장점은
데이터를 갈아 끼울 때 main.py, quiz_data를 제외한 나머지 모듈 코드를 전혀 건들지 않아도 된다.
이것이 모듈 방식의 가장 좋은 점이다.
"""