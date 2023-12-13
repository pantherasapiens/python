import pyttsx3

def speak(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # text_to_speak = input("Enter the text to speak: ")
    # speak(text_to_speak)
    print("Welcome to Robo Speaker \nCreated by Anand")
    while True:
        x = input("Enter Command: ")
        if x == "exit":
            speak("Sayonara")
            break
        else:
            command = f"{x}"
            speak(command)