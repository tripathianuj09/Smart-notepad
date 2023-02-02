import speech_recognition as s

def take_query():
    sr=s.Recognizer()
    print("Say something:")
    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            sr.adjust_for_ambient_noise(m,duration=5)
            text=sr.recognize_google(audio,language='en-IN')
            return text
        except:
            print("Exception occured")

print("You said:",take_query())
