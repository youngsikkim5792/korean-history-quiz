import unittest

from quiz import Quiz
from quiz_game import QuizGame


class TestQuiz(unittest.TestCase):
    def test_correct_answer(self):
        quiz = Quiz("테스트 문제", ["A", "B", "C", "D"], 2)
        self.assertTrue(quiz.check_answer(2))

    def test_wrong_answer(self):
        quiz = Quiz("테스트 문제", ["A", "B", "C", "D"], 2)
        self.assertFalse(quiz.check_answer(1))

    def test_default_questions(self):
        game = QuizGame()
        self.assertGreaterEqual(len(game.quizzes), 5)


if __name__ == "__main__":
    unittest.main()
