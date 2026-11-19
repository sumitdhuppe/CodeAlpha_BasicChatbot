print("Welcome to Python Chatbot!")
print("Type 'bye' to exit.")

while True:

    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hi! How are you?")

    elif user == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user == "what is your name":
        print("Bot: I am Python Chatbot.")

    elif user == "what can you do":
        print("Bot: I can answer simple questions!")

    elif user == "who created you":
        print("Bot: I was created using Python.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand.")