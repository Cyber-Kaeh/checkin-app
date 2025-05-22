from flask import Flask, render_template, request, session, jsonify
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from dotenv import load_dotenv
from flask_session import Session
import random
import time
import os
load_dotenv()

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)

def generate_otp():
    return ''.join(random.choice('0123456789') for _ in range(6))


def send_otp(phone_number, otp):
    message = twilio_client.messages.create(
        body=f'Your OTP is {otp}',
        from_='+14155238886',  # Twilio number
        to=phone_number
    )
    return message.sid