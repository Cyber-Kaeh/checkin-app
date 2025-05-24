import smtplib
import sys
import os
from src.db_config import Session, User
import dotenv
dotenv.load_dotenv()
import random


CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}

messages = [
    "Someone is at the door!"<
    "An addict is dying for a meeting!",
    "Ready to be of service? Grab Anthony a coffee! And someone is at the door.."
]

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("APP_PASSWORD")

def get_recipients():
    db_session = Session()
    users = db_session.query(User).all()
    recipients = [user.check_phone(user.phone_hash) for user in users if user.available]
    db_session.close()
    return recipients

def send_message_to_all():
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    # recipients = get_recipients()
    recipients = [7042674767, 3213120722]
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


def send_message(phone_number, carrier, message):
    recipient = str(phone_number) + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)
 
 
if __name__ == "__main__":
    # if len(sys.argv) < 4:
    #     print(f"Usage: python3 {sys.argv[0]} <PHONE_NUMBER> <CARRIER> <MESSAGE>")
    #     sys.exit(0)
 
    # phone_number = sys.argv[1]
    # carrier = sys.argv[2]
    # message = sys.argv[3]
    send_message_to_all()
    # Example function call
    # send_message(phone_number, carrier, message)
    # send_message(7042674767, "tmobile", "Hello from Python!")