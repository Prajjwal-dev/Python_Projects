import random
import datetime


# A simple rule-based chatbot for Pro Chat

class ProChat:
    def __init__(self, name):
        self.name = name
        self.responses = {
            "hello": ["Hello!", "Hi!", "Greetings!", "Hey there!"],
            "how are you": ["I'm good, thanks for asking!", "Doing well, how about you?",
                            "I'm just a program, but I'm feeling great!"],
            "what's your name": [f"My name is {self.name}.", "You can call me Pro Chat!",
                                 "I'm your AI chatbot friend."],
            "date": ["Today is " + str(datetime.date.today()), "It's " + str(datetime.date.today())],
            "time": ["The current time is " + datetime.datetime.now().strftime("%H:%M:%S"),
                     "Right now, it's " + datetime.datetime.now().strftime("%H:%M:%S")],
            "goodbye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
        }

    def get_response(self, user_input):
        # Lowercase the user input to make the chatbot case-insensitive
        user_input = user_input.lower()

        # Search for a keyword in the user input
        for keyword in self.responses:
            if keyword in user_input:
                return random.choice(self.responses[keyword])

        # Default response if no keyword matches
        return "I'm not sure how to respond to that. Can you ask something else?"


# Main program to run the ProChat bot
def main():
    print("Welcome to Pro Chat!")
    bot_name = "Pro Chat"
    chatbot = ProChat(bot_name)

    user_name = input("What's your name? ")
    print(f"Hello, {user_name}! Ask me anything or type 'goodbye' to exit.")

    while True:
        user_input = input(f"{user_name}: ")

        if "goodbye" in user_input.lower():
            print(chatbot.get_response("goodbye"))
            break
        else:
            response = chatbot.get_response(user_input)
            print(f"{bot_name}: {response}")


if __name__ == "__main__":
    main()
