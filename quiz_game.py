
from questions import get_default_questions


class QuizGame:
    def __init__(self):
        self.quizzes = get_default_questions()
        self.score = 0

    def play(self):
        self.score = 0

        print("\n===== 한국 역사 퀴즈 시작 =====")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[문제 {index}/{len(self.quizzes)}]")
            quiz.display()

            while True:
                answer = input("\n정답 번호 (1~4): ").strip()

                if not answer.isdigit():
                    print("숫자 1~4 중에서 입력해 주세요.")
                    continue

                answer = int(answer)

                if answer < 1 or answer > len(quiz.options):
                    print("보기 번호 중에서 선택해 주세요.")
                    continue

                break

            if quiz.check_answer(answer):
                print("정답입니다! +20점")
                self.score += 20
            else:
                correct = quiz.options[quiz.answer - 1]
                print(f"오답입니다. 정답은 {quiz.answer}번 ({correct})입니다.")

        print("\n===== 퀴즈 종료 =====")
        print(f"최종 점수: {self.score}점 / 100점")
