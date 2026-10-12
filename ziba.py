import pyttsx3 
import speech_recognition as sr
import datetime

#ziba ki awaz set krna 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 1 matlab larki ki awaz 
engine.setProperty('rate',160)

def bolo(text):
    print(f"Ziba: {text}")
    engine.say(text)
    engine.runAndWait()

def suno():
    query = input("Aap bolen (type karen): ")
    return query.lower
        print("sun rahi hun...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='ur-PK')
            print(f"Tum ne kaha: {query}")
            return query.lower()
        except:
            return ""
# jab file chalegi to ziba bolegi
bolo("Assalamualaikum! Main ziba tayyar hun. Batao main kya karo")

while True:
    baat = suno()
    if "asslamualaikum" in baat:
        bolo("walaikum assalam! kaisi ho aap?")
    elif "kya haal he" in baat:
        bolo("Main theek hun, aap sunao!")
    elif "time" in baat or "tareekh" in baat:
        time = datetime.datetime.now().strftime("%I:%M %p")
        bolo(f"Abhi time ho raha hai {time}")
    elif "bye" in baat or "allah hafiz" in baat:
        bolo("Allah Hafiz! phir milenge")
        break
    elif baat!="":
        bolo(f"Aap ne kaha {baat}, is par main abhi seekh rahi hun")    

        



    