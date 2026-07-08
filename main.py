print("ChatGPT Mini: System Booted. Welcome to Day 2!")
user_name = input("ChatGPT Mini:What is your name,user?\n you:")
print("ChatGPT Mini: Hello" + user_name +"! Initializing chat mode. (Type 'exit' or 'bye' to close)\n "+ "_" *50)
while True:
    user_input = input(user_name + ":").lower().strip()
    if user_input == "exit" or user_input == "bye":

        print("ChatGPT Mini: Session ended. Goodbye " + user_name + "! Keep innovating!")
        break
    elif "how" in user_input or "kaise" in user_input:
        print("ChatGPT Mini: As an AI, I am functioning at peak performance! How are you doing today?")

    elif "good" in user_input or "fine" in user_input or "theek" in user_input:
        print("ChatGPT Mini: That's wonderful to hear! What project or coding task are we working on next?")

    elif "bad" in user_input or "sad" in user_input or "boring" in user_input:
        print("ChatGPT Mini: I detect lower energy levels. Maybe a quick break, a fresh coding logic, or a plate of Biryani will help?")
    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("ChatGPT Mini: Hello " + user_name + "! I am online. How can I assist you right now?")
    elif "biryani" in user_input:
        print("ChatGPT Mini: Biryani detected! Highly recommended for boosting developer productivity. Extra points for spicy aloo!")
    else:
        print("ChatGPT Mini: Interesting perspective, " + user_name + ". Tell me more about that, or ask me another question!")
    


