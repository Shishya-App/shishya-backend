from email import message
from twilio.rest import Client
from decouple import config

account_sid = config("account_sid")
auth_token = config("auth_token")
twilio_phone = config("twilio_phone")


class MessageHandler:
    
    phone_number = None
    otp = None
    
    def __init__(self,phone_number,otp):
        self.phone_number= phone_number
        self.otp = otp
        
    def send_otp_on_phone(self):
        client = Client(account_sid, auth_token)
        
        message=   client.messages.create(
                     body=f'Your verification code is "+{self.otp}',
                     from_=twilio_phone,
                     to=self.phone_number
                 )
        print(message.sid)