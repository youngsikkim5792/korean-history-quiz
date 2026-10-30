
class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display(self):
        print("\n" + self.question)

        for number, option in enumerate(self.options, start=1):
            print(f"{number}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.answer
