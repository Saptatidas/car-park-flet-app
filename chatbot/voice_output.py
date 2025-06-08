import pythoncom
import pyttsx3
import threading

def speak(text):
    # This ensures that the text-to-speech engine runs in the main thread
    def run_speech():
        pythoncom.CoInitialize()
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Adjust speed as needed
        engine.say(text)
        engine.runAndWait()
    
    # Run the speech in a separate thread
    if threading.current_thread() is threading.main_thread():
        run_speech()
    else:
        speech_thread = threading.Thread(target=run_speech)
        speech_thread.start()
