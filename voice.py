import pyttsx3


def speak(question):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 145)
    engine.say(question)
    engine.runAndWait()
