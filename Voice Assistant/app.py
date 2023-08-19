import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime
import pyjokes

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing..")
            text=recognizer.recognize_google(audio,language='en-in')
            print(text)
            return text
        except sr.UnknownValueError:
            return ("Could not Understand..")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    
    while True:
        data1 = sptext().lower()
        if data1 == "hey peter":
            speechtx("Hi there! How are you?")
        elif "your name" in data1:
            name = "My name is Peter"
            speechtx(name)
        elif "old are you" in data1:
            birthdate = datetime.date(1985, 5, 5)
            current_date = datetime.date.today()
            age_in_days = (current_date - birthdate).days
            age_in_years = age_in_days // 365
            speechtx(f"I am {age_in_years} years old")
        elif "time" in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")
        elif 'joke' in data1:
            joke = pyjokes.get_joke(language="en", category='neutral')
            print(joke)
            speechtx(joke)
        elif "exit" in data1:
            speechtx("Ok Bye, Fuck Off")
            break
        else:
            speechtx("Could Not Understand")
        
        time.sleep(5)