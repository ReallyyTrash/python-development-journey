import os
import smtplib

import requests
from dotenv import load_dotenv
from pyexpat.errors import messages
from twilio.rest import Client
load_dotenv()
sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
virtual_num = os.getenv("TWILIO_VIRTUAL_NUMBER")
my_num = os.getenv("TWILIO_VERIFIED_NUMBER")
whatsapp_num = os.getenv("TWILIO_WHATSAPP_NUMBER")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(sid, auth_token )
        self.email = os.getenv("my_email")
        self.email_pass = os.getenv("email_pass")
        self.smtp_add = os.getenv("smtp_address")
        self.connection = smtplib.SMTP(self.smtp_add)
    def send_sms(self, body):
        message = self.client.messages.create(from_=virtual_num, to=my_num, body=body)
        print(message.sid)
    def send_whatsapp(self, body):
        message = self.client.messages.create(
            from_=f'whatsapp:{whatsapp_num}',
            body=body,
            to=f'whatsapp: {my_num}')
    def send_email(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_pass)
            for email in email_list:
                self.connection.sendmail(
                    self.email, email, f"Subject: New Low Price Flight! \n\n{email_body}"
                )