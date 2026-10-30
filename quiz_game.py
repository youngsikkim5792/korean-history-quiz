
import json
from pathlib import Path

from quiz import Quiz
from questions import get_default_questions


STATE_FILE = Path(__file__).with_name("state.json")


class QuizGame:
    def __init__(self):
        self.quizzes = get_default_questions()
        self.score = 0
        self.best_score = 0
        self.load_state()

    def load_state(self):
        if not STATE_FILE.exists():
            return

        try:
            with STATE_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("저장 데이터 형식이 잘못되었습니다.")

            saved_quizzes = data.get("custom_quizzes", [])
            best_score = data.get("best_score", 0)

            if not isinstance(saved_quizzes, list):
                raise ValueError("퀴즈 목록 형식이 잘못되었습니다.")

            if type(best_score) is not int or best_score < 0:
                raise ValueError("최고 점수 형식이 잘못되었습니다.")

            loaded_quizzes = []

            for item in saved_quizzes:
                question = item["question"]
                options = item["options"]
                answer = item["answer"]

                if (
                    not isinstance(question, str)
                    or not question.strip()
                    or not isinstance(options, list)
                    or len(options) != 4
                    or not all(
                        isinstance(option, str) and option.strip()
                        for option in options
                    )
                    or type(answer) is not int
                    or answer not in (1, 2, 3, 4)
                ):
                    raise ValueError("저장된 문제 내용이 잘못되었습니다.")

                loaded_quizzes.append(Quiz(question, options, answer))

            self.quizzes.extend(loaded_quizzes)
            self.best_score = best_score

        except (OSError, ValueError, KeyError, TypeError) as error:
            print(f"저장 데이터를 불러오지 못했습니다: {error}")
            print("기본 문제로 게임을 시작합니다.")

    def save_state(self):
        default_count = len(get_default_questions())

        data = {
            "best_score": self.best_score,
            "custom_quizzes": [
                {
                    "question": quiz.question,
                    "options": quiz.options,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes[default_count:]
            ],
        }

        try:
            with STATE_FILE.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            return True

        except OSError as error:
            print(f"저장에 실패했습니다: {error}")
            return False

    def play(self):
        self.score = 0
        total_score = len(self.quizzes) * 20

        print("\n===== 한국 역사 퀴즈 시작 =====")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[문제 {index}/{len(self.quizzes)}]")
            quiz.display()

            while True:
                answer = input("\n정답 번호 (1~4): ").strip()

                if answer not in ("1", "2", "3", "4"):
                    print("숫자 1~4 중에서 입력해 주세요.")
                    continue

                answer = int(answer)
                break

            if quiz.check_answer(answer):
                print("정답입니다! +20점")
                self.score += 20
            else:
                correct = quiz.options[quiz.answer - 1]
                print(f"오답입니다. 정답은 {quiz.answer}번 ({correct})입니다.")

        print("\n===== 퀴즈 종료 =====")
        print(f"최종 점수: {self.score}점 / {total_score}점")

        if self.score > self.best_score:
            self.best_score = self.score
            print("새로운 최고 점수를 달성했습니다!")
            self.save_state()

    def show_best_score(self):
        print(f"\n최고 점수: {self.best_score}점")
