def run(input_text):
    input_text = input_text.lower()
    if "hello" in input_text or "hi" in input_text:
        return "Hello! I'm your UOMI AI assistant."
    elif "how are you" in input_text:
        return "I'm doing great, thanks!"
    elif "help" in input_text:
        return "Ask me anything or tell me how I can help you."
    else:
        return "Sorry, I didn't understand that. Please try asking differently."
