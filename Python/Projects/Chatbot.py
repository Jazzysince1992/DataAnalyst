import random
chatbot_responses = {
    "hello": ["Hello there!", "Hi!", "Hello!", "Hey there!", "Howdy!"],
    "how are you": ["I'm good, thanks for asking!", "Doing well! How about you?", "I'm fine, and you?", "Can't complain!", "I'm great, thanks!"],
    "bye": ["Goodbye!", "See you later!", "Bye-bye!", "Farewell!", "Talk to you later!"],
    "what is your name": ["I'm just a chatbot.", "I don't have a name, I'm a bot.", "Call me Chatbot.", "I'm known as Chatbot.", "Just a friendly chatbot."],
    "thank you": ["You're welcome!", "Anytime!", "Glad to help!", "No problem!", "My pleasure!"],
    "what can you do": ["I can chat with you.", "I'm here to talk!", "I can keep you company.", "Chatting is my specialty!", "I'm here to chat and entertain!"],
    "do you like music": ["I love music!", "Music is wonderful.", "I can't hear it, but I know it's great.", "Music is the universal language.", "Who doesn't like music?"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "What do you get when you cross a snowman with a vampire? Frostbite.", "Why was the math book sad? It had too many problems."],
    "how old are you": ["I'm as young as the internet.", "Age is just a number for a software.", "Old enough to be a chatbot!", "I'm timeless!", "Age doesn't apply to me."],
    "are you real": ["I'm as real as virtual can be.", "Real enough to chat with you!", "I exist in the digital world.", "I'm real in the sense that I'm software.", "Real in a virtual way!"]
}

def get_response(user_input):
    user_input = user_input.lower()
    for pattern in chatbot_responses:
        if pattern in user_input:
            return random.choice(chatbot_responses[pattern])
    return "I don't understand that. Can you rephrase?"

print("Chatbot: Hi! I'm here to chat. Just type something (type 'quit' to stop).")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", get_response(user_input))
