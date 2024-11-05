from question_model import question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for data in question_data:
    question_text = data["text"]
    question_answer = data["answer"]
    new_question = data(question_answer, question_text)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number} ")