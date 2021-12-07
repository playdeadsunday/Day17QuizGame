from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data)):
    new_q = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(new_q)

new_ob = QuizBrain(question_bank)

new_ob.next_question()
