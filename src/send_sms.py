import smtplib
import os
from src.db_config import Session, User
import dotenv
dotenv.load_dotenv()
import random


CARRIERS = {
    "att": "@text.att.net",
    "att-old": "@mmode.com",
    "att-cingular": "@cingularme.com",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com",
    "boost": "@myboostmobile.com",
    "cricket": "@sms.mycricket.com",
    "uscellular": "@email.uscc.net",
    "metropcs": "@mymetropcs.com",
    "sprint": "@messaging.sprintpcs.com",
    "sprint2": "@pm.sprint.com",
    "straighttalk": "@vtext.com",
}

messages = [
    "Someone is at the door!",
    "An addict is dying for a meeting!",
    "Will you go let someone in?",
    "Ready to be of service? Grab Anthony a coffee! Oh, and someone is at the door.."
]

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("APP_PASSWORD")

def get_recipients():
    db_session = Session()
    users = db_session.query(User).all()
    recipients = [user.phone for user in users if user.available]
    db_session.close()
    return recipients


def send_messages():
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    recipients = get_recipients()
    if not recipients:
        print("No available members at this time.")
        return
    for carrier in CARRIERS:
        for recipient in recipients:
            message = random.choice(messages)
            recipient_email = str(recipient) + CARRIERS[carrier]
            server.sendmail(auth[0], recipient_email, message)
        print(f"Message sent to {recipient_email} via {carrier}.")
    print("All messages sent successfully.")


if __name__ == "__main__":
    send_messages()