"""Simple voice assistant that can greet users and send a predefined email."""

import os
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage


def speak(text: str) -> None:
    """Speak text aloud and print it for visibility."""
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def listen() -> str:
    """Listen through the microphone and return recognized speech."""
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=10)
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower().strip()
    except (sr.UnknownValueError, sr.RequestError, OSError, sr.WaitTimeoutError) as error:
        print("Speech recognition error:", error)
        speak("Sorry, I couldn't understand. Please try again.")
        return ""


def send_mail(recipient: str, subject: str, content: str) -> bool:
    """Send an email using SMTP credentials stored in environment variables."""
    sender = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("SENDER_APP_PASSWORD")

    if not sender or not app_password:
        print("Set SENDER_EMAIL and SENDER_APP_PASSWORD environment variables first.")
        return False

    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(content)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as server:
            server.starttls()
            server.login(sender, app_password)
            server.send_message(message)
        return True
    except (smtplib.SMTPException, OSError) as error:
        print("Email could not be sent:", error)
        return False


def main() -> None:
    speak("Hi! Say hello to start.")
    greeting = listen()

    if not any(word in greeting for word in ("hi", "hello", "hey")):
        speak("Please say hi or hello to start.")
        return

    speak("What is your name?")
    name = listen() or "there"
    speak(f"How can I help you, {name}?")

    command = listen()
    if "send message" not in command and "mail" not in command and "email" not in command:
        speak("I can currently help with sending a predefined email.")
        return

    speak("I can send an email. Please say the recipient email address.")
    recipient = listen().replace(" ", "")
    if "@" not in recipient or "." not in recipient:
        speak("That doesn't sound like a valid email address. Cancelling.")
        return

    email_content = "This is a test email sent by my voice assistant project."
    speak("The email content is: " + email_content)
    speak("Should I send it? Please say yes or no.")
    confirmation = listen()

    if confirmation == "yes" or confirmation.startswith("yes "):
        if send_mail(recipient, "Test email from Voice Assistant", email_content):
            speak("Email sent successfully.")
        else:
            speak("I couldn't send the email. Check the setup and terminal message.")
    else:
        speak("Email cancelled.")


if __name__ == "__main__":
    main()
