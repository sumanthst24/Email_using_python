# Import the email modules and smtplib
import smtplib
# import imghdr to find the types of our image
import imghdr
from email.message import EmailMessage

sender_email="sender-email-address" #assigning sender email address
sender_password="sender-email-password" #assigning the password to a sender_password variable

receiver_email="receiver-email-address" #assigning receiver email address
subject="Test" #assigning subject of the email
body="Image testing worked" #assigning body of the email

# Create the email message object
msg = EmailMessage()

# Creation of the message and email structure
msg['From']=sender_email
msg['To']=receiver_email
msg['Subject']=subject
msg.set_content(body)

# Open the files in byte mode.
with open('scenary.jpeg', 'rb') as f:
        file_data = f.read()#reading the data of the input image
        file_type = imghdr.what(f.name)#imghdr to figure out the type of the image
        file_name = f.name

#adding thr attchment to the EmailMessage object
msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#login wih the credentials
smtp.login(sender_email,sender_password)
#send the message along with attachment
smtp.send_message(msg)
#quit the connection established
smtp.close()
