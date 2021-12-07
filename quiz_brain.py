class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        next_q = self.question_list[self.question_number]
        next_a = input(f"Q.{self.question_number}: {next_q.text} (True/False): ")
