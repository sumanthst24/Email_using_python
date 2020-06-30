# Import the email modules and smtplib
import smtplib
from email.message import EmailMessage

sender_email="your-email-here" #assigning sender email address
sender_password="your-password" #assigning the password to a variable

receiver_email="receiver-email-address" #assigning receiver email address
subject="Test" #assigning subject of the email
body="testing worked" #assigning body of the email

# Create the email message object
msg = EmailMessage()

# Creation of the message and email structure
msg['From']=sender_email
msg['To']=receiver_email
msg['Subject']=subject
msg.set_content(body)

# Send the email through smtp.gmail.com server and 465 port number.
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

#login wih the credentials
smtp.login(sender_email,sender_password)

#send the message
smtp.send_message(msg)

#quit the connection established
smtp.close()
