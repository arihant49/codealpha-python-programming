def simple_chatbot():
    print("--- CodeAlpha Rule-Based Chatbot ---")
    print("Type 'bye' to exit the conversation.\n")
    
    while True:
        # Standardize user input to lowercase and strip whitespace
        user_input = input("You: ").lower().strip()
        
        # Rule-based conditions
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi! How can I help you today?")
            
        elif "how are you" in user_input:
            print("Chatbot: I'm fine, thanks! Just here to help you code.")
            
        elif "your name" in user_input:
            print("Chatbot: I'm the CodeAlpha Basic Assistant Bot.")
            
        elif "bye" in user_input or "goodbye" in user_input:
            print("Chatbot: Goodbye! Have a wonderful day!")
            break  # Exit the loop
            
        else:
            print("Chatbot: I'm sorry, I don't quite understand that. Try saying 'hello' or 'how are you'.")

if __name__ == "__main__":
    simple_chatbot()