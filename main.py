
from quiz_game import QuizGame
from quiz import Quiz


def add_quiz(game):
    print("\n===== 새로운 퀴즈 추가 =====")

    question = input("문제를 입력하세요: ").strip()

    if not question:
        print("문제는 비워둘 수 없습니다.")
        return

    options = []

    for number in range(1, 5):
        option = input(f"{number}번 보기를 입력하세요: ").strip()

        if not option:
            print("보기는 비워둘 수 없습니다.")
            return

        options.append(option)

    while True:
        answer = input("정답 번호 (1~4): ").strip()

        if answer in ("1", "2", "3", "4"):
            break

        print("1~4 중에서 입력해 주세요.")

    game.quizzes.append(Quiz(question, options, int(answer)))

    if game.save_state():
        print("\n새로운 퀴즈가 저장되었습니다!")
    else:
        print("\n문제는 추가되었지만 저장에 실패했습니다.")

    print(f"총 {len(game.quizzes)}개의 문제가 등록되어 있습니다.")


def main():
    game = QuizGame()

    while True:
        print("\n================================")
        print("       한국 역사 퀴즈 게임")
        print("================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가하기")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("5. 종료")

        choice = input("\n메뉴 번호를 입력하세요 (1~5): ").strip()

        if choice == "1":
            game.play()

        elif choice == "2":
            add_quiz(game)

        elif choice == "3":
            print("\n===== 한국 역사 퀴즈 목록 =====")

            for index, quiz in enumerate(game.quizzes, start=1):
                print(f"{index}. {quiz.question}")

            print(f"\n총 {len(game.quizzes)}개의 문제가 등록되어 있습니다.")

        elif choice == "4":
            game.show_best_score()

        elif choice == "5":
            print("게임을 종료합니다. 감사합니다!")
            break

        else:
            print("잘못된 입력입니다. 1~5 중에서 선택하세요.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n게임을 종료합니다.")
