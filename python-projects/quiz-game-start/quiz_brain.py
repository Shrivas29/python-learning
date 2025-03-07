class Quizbrain:
    def __init__(self,question_list,score):
        self.question_number = 0 
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"is this TRUE OR FALSE{self.question_number}:{current_question.text}")
        self.check_score(self,answer,current_question)
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True 
        else:
            False
      
    def check_score(self,answer,correct_answer):
        if answer.lower() == correct_answer.lower():
            print("you are right")
            self.score += 1
        else:
            print("you are wrong") 
        print(self.score,"this is your current score")
        print("\n")
        




