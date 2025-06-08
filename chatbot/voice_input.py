import speech_recognition as sr

def recognize_with_fallbacks(recognizer, audio):
    languages = ["en-IN", "hi-IN", "bn-IN"]
    for lang in languages:
        try:
            print(f"🌐 Trying language: {lang}")
            location = recognizer.recognize_google(audio, language=lang)
            print(f"✅ Recognized with {lang}: {location}")
            return location
        except sr.UnknownValueError:
            print(f"🤔 Didn't understand in {lang}")
        except sr.RequestError as e:
            print(f"⚠️ API error for {lang}: {e}")
    return None

def listen_for_location():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎙️ Listening... Please say your location.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
    except sr.WaitTimeoutError:
        print("⏰ No speech detected. Please try again.")
        return None
    except OSError:
        print("❌ Microphone not found or is in use.")
        return None

    try:
        print("🔎 Recognizing speech...")
        location = recognize_with_fallbacks(recognizer, audio)
        if location:
            print(f"📍 You said: {location}")
        return location
    except sr.UnknownValueError:
        print("😕 Sorry, I couldn't understand your voice.")
        return None
    except sr.RequestError as e:
        print(f"⚠️ Could not request results from API; {e}")
        return None
