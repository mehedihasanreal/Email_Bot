import smtplib  # simple mail transfer protocol
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass


def send_email(reciever, subject, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # transport layer security
    server.login("sender@gmail.com", "password")
    email = EmailMessage()
    email["From"] = "sender"
    email["To"] = reciever
    email["Subject"] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    "nasim": "hasantareq@gmail.com",
    "tushar": "tusherkhan@gmail.com",
    "zubaer": "zubaer.almahamud@gmail.com",
}


def get_email_info():
    talk("To whom you want to send email:")
    name = get_info()
    reciever = email_list[name]
    print(reciever)
    talk("what is the subject of your email?")
    subject = get_info()
    talk("Tell me the text of the email")
    message = get_info()
    send_email(reciever, subject, message)
    talk("boss your mail is sent")
    talk("do you want to send more mail?")
    send_more = get_info()
    if "yes" in send_more:
        get_email_info()


get_email_info()
