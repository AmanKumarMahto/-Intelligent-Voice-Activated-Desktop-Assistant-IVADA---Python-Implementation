import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import mysql.connector



engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("I m sam Please tell me how may i help you")

def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
    # print(e)

        print("say that again please...")
        return ("None")
    return query
if __name__ == '__main__':
    wishme()
    while True:
    #if 1:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open chrome' in query:
            webbrowser.open("chrome.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")\

        elif'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'shutdown' in query:
            os.system('shutdown -s')
            speak("shutting down...")
        elif'the time' in query:
            strTime = datetime.datetime.now().strftime("%H Hour:%M Minutes:%S Seconds")
            speak(f"sir,The Time is{strTime}")
        elif 'open code' in query:
            pycharmPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains"
            os.startfile(pycharmPath)

        elif 'open snapchat image' in query:
            imagesPath = "D:\\Snapchat"
            os.startfile(imagesPath)

        elif 'open farewell image' in query:
            farewellPath = "D:\\Farewell"
            os.startfile(farewellPath)



        elif 'open result' in query:
            mydb = mysql.connector.connect(host="localhost",user="raj",passwd="raj1234",database="results",auth_plugin="mysql_native_password")
            mycursor = mydb.cursor()

            mycursor.execute("select * from students")

            for i in mycursor:
                print(i)

        elif'of' in query:
            quit()