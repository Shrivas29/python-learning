from question_model import Questions
from data import question_data
from quiz_brain import Quizbrain
questions_bank = []
for i in question_data:
    questions_text = i["text"]
    questions_answer = i["answer"]
    new_questions = Questions(text=questions_text,answer=questions_answer)
    questions_bank.append(new_questions)
    

quiz = Quizbrain(questions_bank) 
quiz.next_question()