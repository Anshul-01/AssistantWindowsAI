import pyttsx3
import datetime
import calendar
import speech_recognition as sr
import news
import wikipedia
import webbrowser
import os
import AI
import random
import time
from time import ctime
import colourSong as cs


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current
engine.setProperty('rate', 250)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',0.9)    # setting up volume level  between 0 and 1

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Good Morning Boss!")
    
    elif hour >= 12 and hour <16:
        speak("Good Afternoon Boss!")
    
    else:
        speak("Good Evening Boss!")
    
    speak("Tell me how may I help you.")

def takeCommand():
    '''
        It takes microphone input from the user and returns string output
    '''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening....")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print("\nRecognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
 
    except Exception as e:
        #print(e)
        print("I didn't get that Boss!")
        inst_ques = "You may ask"
        instruction_questions = {'1':'Open Youtube.',
                                 '2':'Open google.',
                                 '3':'Search <-say that you want to search-> on wikipedia.',
                                 '4':'Play <-video you want to watch on youtube-> video from youtube.',
                                 '5':"What's today's date.",
                                 '6':"What's the current time. OR What's the time.",
                                 '7':'Tell me about Yourself.',
                                 '8':'For coding - Say Open Code.',
                                 '9':'Play songs. OR Plays Music.',
                                 '10':'Update me by News. OR Tell me the News.',
                                 '11':'FRIDAY are you there?',
                                 '12':'For shutdowm AI say - Goodbye.',
                                 '13':'For shutdown PC say - Shutdown. '}
        rand = str(random.randint(1,13))
        print(inst_ques + " " + instruction_questions[rand])
        return "None"
    return query

def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ['January','february','March','April','May','June','July','August','September','October','November','December']

    ordinalNumbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th',
                        '19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']

    return weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'

def youtube(query):
    song = query.replace('play','')
    pywhatkit.playonyt(song)

if __name__ == "__main__":
    wishMe()
    _red = 0
    _yellow = 0
    _green = 0
    while True:    

        query = takeCommand().lower()
        
        #Logic for Recognizing tasks based on query
        if 'wikipedia' in query:
            speak('Searching on wikipedia Sir')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('It says that...')
            print(results)
            speak(results)

        elif 'play light loop 1' in query:
            print("Playing loop 1")
            speak("Playing loop 1")
            cs.loopLed1()
            cs.loopNill()
        
        elif 'play light loop 2' in query:
            print("Playing loop 2")
            speak("Playing loop 2")
            cs.loopLed2()
            cs.loopNill()

        elif 'open google' in query:
            speak("opening Google")
            webbrowser.open("www.google.co.in")

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com/")

        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'on youtube' in query:
            _query = query.replace('play','')
            print("Playing " + _query)
            speak("Playing " + _query)
            youtube(query)

        elif 'open all lights' in query:
            _red = 1
            _yellow = 1
            _green = 1
            speak("Opening all lights")
            cs.manualGlow(_red,_yellow,_green)

        elif 'close all lights' in query:
            _red = 0
            _yellow = 0
            _green = 0
            speak("Closing all lights")
            cs.manualGlow(_red,_yellow,_green)
        
        elif 'open red' in query:
            _red = 1
            speak("Opening Red")
            cs.manualGlow(_red,_yellow,_green)

        elif 'close red' in query:
            _red = 0
            speak("Closing Red")
            cs.manualGlow(_red,_yellow,_green)

        elif 'open read' in query:
            _red = 1
            speak("Opening Red")
            cs.manualGlow(_red,_yellow,_green)

        elif 'close read' in query:
            _red = 0
            speak("Closing Red")
            cs.manualGlow(_red,_yellow,_green)
            
        elif 'open yellow' in query:
            _yellow = 1
            speak("Opening yellow")
            cs.manualGlow(_red,_yellow,_green)

        elif 'close yellow' in query:
            _yellow = 0
            speak("Closing yellow")
            cs.manualGlow(_red,_yellow,_green)
            
        elif 'open green' in query:
            _green = 1
            speak("Opening green")
            cs.manualGlow(_red,_yellow,_green)

        elif 'close green' in query:
            _green = 0
            speak("Closing green")
            cs.manualGlow(_red,_yellow,_green)

        elif 'date' in query:
            get_date = getDate()
            print(get_date)
            speak(f"Today's date is {get_date}")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")
        
        elif 'yourself' in query:
            Myself = AI.myself('FRIDAY', 'February 20', 'Anshul and Akash')
            print(Myself)
            speak(Myself)

        elif 'open code' in query:
            codePath = 'C:\\Documents\\Microsoft VS Code\\Code.exe'
            speak("opening VS code")
            os.startfile(codePath)

        elif 'open wordpad' in query:
            speak("Open Word Pad")
            codePath1 = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Wordpad'
            os.startfile(codePath1)

        elif 'open media player' in query:
            speak("Opening Media Player")
            codePath2 = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Windows Media Player'
            os.startfile(codePath2)

        elif 'play game' in query:
            codePath3 = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Riot Games\\VALORANT'
            os.startfile(codePath3)
            print("Enjoy the Game. See you Boss!")
            speak("Enjoy the Game. See you Boss!")
            exit()
        
        elif 'play song' in query:
            music_directory = 'C:\\Documents\\Songs\\English Songs'
            songs = os.listdir(music_directory)
            print("Playing " + songs)
            speak("Opening Media Player")
            songs = os.startfile(os.path.join(music_directory,random.choice(songs)))

        elif 'play music' in query:
            music_directory = 'C:\\Documents\\Songs\\English Songs'
            songs = os.listdir(music_directory)
            print("Playing " + songs)
            speak("Opening Media Player")
            songs = os.startfile(os.path.join(music_directory,random.choice(songs)))

        elif 'news' in query:
            speak("Today's News are:\n")
            newsNumbers = {'1':'First news is ',
                            '2':'Second news is ',
                            '3':'Third news is ',
                            '4':'Fourth news is ',
                            '5':'Fifth news is ',
                            }
            for i in range(0,5):
                News = news.newsHeadlines(('https://newsapi.org/v2/top-headlines?'
           'sources=bbc-sport&'
           'apiKey=439913c16a5644c7a165664f0bccdeed'),i)
                print(f'{(i+1)}: {News}')
                speak(newsNumbers[str(i+1)])
                speak(News)

        elif 'friday are you there' in query:
            speak('For you Boss, always there!')

        elif 'goodbye' in query:
            speak("Take care Boss!")
            exit()

        elif 'good bye' in query:
            speak("Take care Boss!")
            exit()


        elif 'shutdown' in query:
            speak("Shutting Down the Sytem")
            os.system('shutdown -s')