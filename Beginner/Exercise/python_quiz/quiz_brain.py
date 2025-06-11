class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.q_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(user_input, current_question.answer)
    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
            print(f"your current score is {self.score}/{self.question_number}")
        else:
            print(f"You got it wrong, correct answer is {correct_answer}")
            print(f"your current score is {self.score}/{self.question_number}")

    
