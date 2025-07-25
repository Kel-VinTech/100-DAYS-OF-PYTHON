from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["text"]
    answer = question["answer"]
    new_question = Question(question_text,answer)    
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

    if quiz.still_has_questions() == False:
        print("You have completed this quiz")
        print(f"Your final score is {quiz.score}/{quiz.question_number}")

