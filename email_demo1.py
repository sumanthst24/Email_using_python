import smtplib

sender_email="your-email-here" #assigning sender email address
sender_password="your-password" #assigning the password to a variable

receiver_email="receiver-email-address" #assigning receiver email address
subject="Test"
body="testing worked"

smtp = smtplib.SMTP('smtp.gmail.com', 587)

smtp.ehlo()
smtp.starttls()
smtp.ehlo()

smtp.login(sender_email,sender_password)

msg=subject+'\n\n'+body


smtp.sendmail(sender_email,receiver_email,msg)

smtp.close()
