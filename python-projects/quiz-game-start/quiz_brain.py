class Quizbrain:
    def __init__(self,question_list):
        self.question_number = 0 
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"is this TRUE OR FALSE{self.question_number}:{current_question.text}")

    def still_has_question(self):
        



