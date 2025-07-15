import html
class QuizBrain:
    def __init__(self, q_list):
        self.current_question = None
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list) # [?] <=

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number }: {q_text}."
        # self.check_answer(u_ans, current_question.answer )

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            # print("you got it right")
            self.score += 1
            return True
        else:
            return False
        # print(f"the correct answer was {correct_answer}")
        # print(f"Your current score is {self.score}/{self.question_number}")
        # print("\n"*1)
