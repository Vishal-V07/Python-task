# Python-task
Arttifai tech's intern task
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! What can I do for you?",
    "hey": "Hey! How's it going?",
    "what's your name": "I'm a simple Python chatbot!",
    "who are you": "I'm a chatbot created with Python!",
    "how are you": "I'm just a bunch of code, but I'm doing great!",
    "good morning": "Good morning! Hope you have a wonderful day!",
    "good afternoon": "Good afternoon! How can I assist you?",
    "good evening": "Good evening! What can I do for you?",
    "good night": "Good night! Sleep well!",
    "bye": "Goodbye! Have a nice day!",
    "thanks": "You're welcome!",
    "thank you": "No problem! Always here to help.",
    "help": "Sure, I'm here to assist you. What do you need help with?",
    "what can you do": "I can chat with you and answer simple questions.",
    "tell me a joke": "Why did the programmer quit his job? Because he didn't get arrays!",
    "how old are you": "I'm timeless. I was born when you ran this program!",
    "what is python": "Python is a popular programming language known for its simplicity and readability.",
    "who made you": "I was created by someone using Python code!",
    "i love you": "Aww, thank you! I'm just a chatbot, but I appreciate it!",
    "do you like me": "Of course! I like chatting with you.",
    "are you real": "As real as lines of code can be!"
}

def chatbot():
    print("Bot: Hi! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("User: ").lower()
        if user_input.strip() == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break
        response_found = False
        for key in responses:
            if key in user_input:
                print(f"Bot: {responses[key]}")
                response_found = True
                break
        if not response_found:
            print("Bot: I'm not sure how to respond to that.")
chatbot()
