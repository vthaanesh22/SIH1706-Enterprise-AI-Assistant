def chatbot():
    print("Enterprise Assistant Chatbot")
    
    while True:
        user = input("Employee: ").lower()

        if "leave" in user:
            print("Bot: Employees are allowed 12 casual leaves per year.")
        
        elif "password" in user:
            print("Bot: Please reset your password through the IT portal.")
        
        elif "event" in user:
            print("Bot: The annual company meeting will be held next month.")
        
        elif "exit" in user:
            print("Bot: Goodbye!")
            break
        
        else:
            print("Bot: I will help you with HR or IT related queries.")

chatbot()
