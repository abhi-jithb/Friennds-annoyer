import pywhatkit as kit
import time
import random

# Your friend's phone number in international format
phone = "+91 9946712381"  # Replace with your friend's number

# List of annoying or funny messages
messages = [
    "Hello Campus Lead Perumon 😜",
    "Comon everybody get ready to clap.... ",
    "Clap your hands.. to to.. 👏",
    "👏"
    "👏👏"
    "👏👏👏",
    "👏👏👏👏",
    "👏👏👏👏👏",
    "👏👏👏👏👏👏👏👏👏",
    "Spam spam spam spam!"
]

# How many messages you want to send
count = 10

# Send messages in loop
for i in range(count):
    message = random.choice(messages)
    
    
    # This sends the message immediately
    kit.sendwhatmsg_instantly(phone_no=phone, message=message, wait_time=10, tab_close=True)
    time.sleep(2)  # WhatsApp needs at least 15 seconds before sending another

