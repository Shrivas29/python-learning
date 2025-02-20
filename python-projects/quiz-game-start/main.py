from question_model import Questions
from data import question_data
questions_bank = []
for i in question_data:
    questions_text = i["text"]
    questions_answer = i["answer"]
    new_questions = Questions(text=questions_text,answer=questions_answer)
    questions_bank.append(new_questions)