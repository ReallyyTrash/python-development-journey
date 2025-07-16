import html
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list) # [?] <=

    def next_question(self):
        current_question = self.question_list[self.question_number]

        self.question_number += 1
        q_text = html.unescape(current_question.text)
        u_ans =input(f"Q.{self.question_number }: {q_text}. (True/False): ")
        self.check_answer(u_ans, current_question.answer )

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("you got it right")
            self.score += 1
        else:
            print("thats wrong")
        print(f"the correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n"*1)