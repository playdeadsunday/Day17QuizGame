class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        next_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {next_q.text} (True/False): ").capitalize()
        self.check_answer(user_answer, next_q.answer)

    def check_answer(self, user_a, correct_a):
        if user_a == correct_a:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_a}\nYour current score is: {self.score}/{self.question_number}\n")
