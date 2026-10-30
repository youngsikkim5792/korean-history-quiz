def main():
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
    print("테스트 성공! 1번 메뉴가 실행되었습니다.")
    print("퀴즈 풀기 기능은 준비 중입니다.")
        elif choice == "2":
            print("퀴즈 추가 기능은 준비 중입니다.")
        elif choice == "3":
            print("퀴즈 목록 기능은 준비 중입니다.")
        elif choice == "4":
            print("최고 점수 기능은 준비 중입니다.")
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