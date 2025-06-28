# Simple rule-based chatbot
def chatbot():
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm doing great, thanks!",
        "bye": "Goodbye!"
    }
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            break
        print("Bot:", responses.get(user_input, "I don't understand."))

if __name__ == "__main__":
    chatbot()