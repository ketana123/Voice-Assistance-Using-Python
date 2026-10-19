# Voice Assistant in Python

A beginner-friendly voice assistant project built with Python. It listens to spoken commands, responds using text-to-speech, and can send a predefined email after asking for confirmation.

## Features

- Greets the user and asks for their name
- Recognizes speech through the microphone
- Responds using text-to-speech
- Supports a basic email-sending flow with user confirmation
- Reads email credentials from environment variables instead of hardcoding them

## Tech Stack

- Python
- SpeechRecognition
- pyttsx3
- SMTP (`smtplib`) for email delivery

## Project Structure

```text
voice-assistant/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer recommended
- A working microphone
- Internet connection for Google speech recognition and SMTP email delivery
- Gmail account with 2-Step Verification and a Google App Password (for Gmail SMTP)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/voice-assistant.git
   cd voice-assistant
   ```

2. Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If `PyAudio` fails to install, use the installation instructions for your operating system or Python version.

4. Configure email credentials as environment variables. Do not put your real password or app password in source code.

   **Windows PowerShell**
   ```powershell
   $env:SENDER_EMAIL="your_email@gmail.com"
   $env:SENDER_APP_PASSWORD="your_gmail_app_password"
   ```

   **macOS/Linux**
   ```bash
   export SENDER_EMAIL="your_email@gmail.com"
   export SENDER_APP_PASSWORD="your_gmail_app_password"
   ```

5. Run the assistant:

   ```bash
   python main.py
   ```

## How It Works

1. The assistant listens for a greeting.
2. It asks for the user's name and what they want to do.
3. If an email command is detected, it asks for a recipient email address.
4. It reads out the predefined message and asks for confirmation.
5. If the user confirms, it sends the email using Gmail SMTP.

## Current Limitations

- The email body is predefined; composing a custom message from speech is not implemented.
- WhatsApp messaging is not implemented.
- Speech recognition uses Google's online recognition service, so an internet connection is required.
- Email sending requires correctly configured Gmail credentials and an App Password.

## Security Notes

- Never commit passwords, Gmail App Passwords, API keys, or personal email credentials.
- Keep `.env` and any file containing secrets out of GitHub.
- This is a learning project. Test it with an email address you control before using it for anything important.

## Future Improvements

- Let users dictate a custom email subject and message
- Add contact selection and stronger email-address validation
- Add more voice commands and graceful retry handling
- Add a WhatsApp integration only through an approved API

## Author

Ketana Lohar
