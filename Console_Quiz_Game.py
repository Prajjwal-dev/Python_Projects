import requests
import random
import os
import html


class QuizGameAPI:

    def __init__(self):
        self.api_url = "https://opentdb.com/api.php?amount=5&type=multiple"
        self.questions = []
        self.score = 0
        self.high_score = self.load_high_score()

    def fetch_questions(self):
        """Fetch questions from the API."""
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json()
            self.questions = data["results"]
        else:
            print("Error fetching questions from the API.")
            exit()

    @staticmethod
    def format_question(question_data):
        """Format the question and options for display."""
        question = html.unescape(question_data['question'])
        correct_answer = html.unescape(question_data['correct_answer'])
        incorrect_answers = [html.unescape(ans) for ans in question_data['incorrect_answers']]
        options = incorrect_answers + [correct_answer]
        random.shuffle(options)

        return {
            "question": question,
            "options": options,
            "answer": correct_answer
        }

    def load_high_score(self):
        """Load the high score from a file."""
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as file:
                try:
                    return int(file.read().strip())
                except ValueError:
                    return 0
        return 0

    def save_high_score(self):
        """Save the high score to a file."""
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def start(self):
        """Start the quiz game."""
        print("\nWelcome to the Console Quiz Game (API Edition)!")
        while True:
            self.fetch_questions()
            self.score = 0  # Reset score for new game

            for i, question_data in enumerate(self.questions):
                formatted = self.format_question(question_data)
                print(f"\nQuestion {i + 1}: {formatted['question']}")
                for j, option in enumerate(formatted['options'], start=1):
                    print(f"{chr(64 + j)}. {option}")

                answer = input("Your answer (A/B/C/D) or type 'exit' to quit: ").upper()
                if answer == 'EXIT':
                    print(f"Exiting the game. Your final score: {self.score}")
                    break

                if answer not in ['A', 'B', 'C', 'D']:
                    print("Invalid choice. Please select A, B, C, or D.")
                    continue

                if formatted['options'][ord(answer) - 65] == formatted['answer']:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer was {formatted['answer']}.")

                print(f"Current Score: {self.score}")

            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
                print(f"Congratulations! New High Score: {self.high_score}")

            print(f"\nQuiz Over! You scored {self.score}/{len(self.questions)}.")
            print(f"Current High Score: {self.high_score}")

            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thank you for playing!")
                break


if __name__ == "__main__":
    game = QuizGameAPI()
    game.start()
