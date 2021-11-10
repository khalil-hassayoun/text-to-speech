import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
while True:
    text = input("Enter text: ")
    engine.say(text)
    engine.runAndWait() 
