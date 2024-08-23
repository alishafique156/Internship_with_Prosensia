#Quizgame
def get_questions():
  return {
      "What is the capital of Pakistan?": "Islamabad",
      "What is 2 + 1 ?": "3",
      "What is the color of the sky?": "Yellow"
  }

def ask_question(question, correct_answer):
  user_answer = input(question + " ").strip().capitalize()
  if user_answer == correct_answer.capitalize():
      return True
  else:
      print(f"Incorrect. The correct answer is {correct_answer}.")
      return False

def main():
  questions = get_questions()
  score = 0
  for question, answer in questions.items():
      if ask_question(question, answer):
          score += 1
  print(f"Your final score is {score}/{len(questions)}.")

main()

