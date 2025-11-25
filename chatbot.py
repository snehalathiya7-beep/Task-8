
"""
Rule-Based Chatbot
------------------
A simple chatbot using if-elif-else statements.
Objective: Understand basic NLP structure.
Author: Sneha Lathiya
"""

print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("🤖 Chatbot: Goodbye! Have a nice day!")
        break

    elif "hello" in user or "hi" in user or "hey" in user:
        print("🤖 Chatbot: Hello! How can I help you?")

    elif "how are you" in user:
        print("🤖 Chatbot: I'm doing great! Thanks for asking.")

    elif "your name" in user:
        print("🤖 Chatbot: I'm a simple rule-based chatbot created using Python.")

    elif "help" in user:
        print("🤖 Chatbot: I can respond to greetings and simple questions.")

    else:
        print("🤖 Chatbot: Sorry, I don't understand that yet. I'm still learning!")
