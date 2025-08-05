class Agent:
    def __init__(self):
        self.name = "SimpleUomiAgent"
        self.version = "1.0.0"
        self.author = "fahadzaynn-droid"
        self.description = "A simple chatbot agent compliant with UOMI AI platform requirements."

    def run(self, input_text: str) -> str:
        input_text = input_text.lower()
        if "hello" in input_text or "hi" in input_text:
            return "Hello! I'm your UOMI AI assistant."
        elif "how are you" in input_text:
            return "I'm doing great, thanks for asking!"
        elif "help" in input_text:
            return "Feel free to ask me anything or request assistance."
        else:
            return "Sorry, I didn't understand that. Could you please rephrase?"

