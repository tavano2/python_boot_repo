# TODO 1. asking the questions
# TODO 2. checking if the answer was correct
# TODO 3. checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer =input(f"Q.{self.q_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def check_answer(self, correct_answer, current_answer):
        if correct_answer.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"You scored: {self.score}/{self.q_number}")
        print("\n")


