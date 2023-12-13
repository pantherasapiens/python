from gtts import gTTS
import pygame

# Initialize pygame with minimal video settings
pygame.init()
pygame.mixer.init()

def speak(text):
    # Create a gTTS object with the text
    tts = gTTS(text)

    # Save the speech to an audio file
    tts.write_to_fp("temp.mp3")

    # Load the saved audio file using pygame
    pygame.mixer.music.load("temp.mp3")

    # Play the loaded audio file
    pygame.mixer.music.play()

    # Wait for the audio to finish
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.event.wait()

if __name__ == "__main__":
    print("Welcome to Robo Speaker \nCreated by Anand")
    while True:
        x = input("Enter Command: ")
        if x == "exit":
            speak("Sayonara")
            break
        else:
            command = f"{x}"
            speak(command)

    # Clean up pygame
    pygame.mixer.quit()
    pygame.quit()
