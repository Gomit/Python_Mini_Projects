
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC065409470d8ccbdf983738257e6f0927"
auth_token  = "581df18f25c12b56b5f3abc4e0906aa8"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="TEXTMESSAGE TO MERON!",
    to="+46762575515",    # Replace with your phone number
    from_="+46769438567") # Replace with your Twilio number
print message.sid