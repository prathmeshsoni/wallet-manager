# email_notifier.py

import os
import smtplib
import sys
import traceback
from email.message import EmailMessage

# email_list = {'analpatel': 'analpatel.crawlmagic@gmail.com',
#               'anitagohil': 'anitagohil.crawlmagic@gmail.com',
#               'jaymak': 'jaymak.crawlmagic@gmail.com',
#               'karan': 'karan.crawlmagic@gmail.com',
#               'krupesh': 'krupesh.crawlmagic@gmail.com',
#               'parth': 'parth.crawlmagic@gmail.com',
#               'parth6353': 'parth6353.crawlmagic@gmail.com',
#               'prathmesh': 'prathmesh.crawlmagic@gmail.com',
#               'vrushabh': 'vrushabh.crawlmagic@gmail.com',
#               'yash': 'yash.crawlmagic@gmail.com',
#               'yashvyas': 'yashvyas.crawlmagic@gmail.com'}


def send_email():
    subject = f"Script Execution: "
    body = f"Your script  located in folder  has started running."

    # Replace the following details with your email server settings
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    # cc_email = 'status.crawlmagic@gmail.com'
    sender_email = 'prathmesh.soni112@gmail.com'
    password = 'cobykuwsrpnjbzqw'

    # Logic to get the email address associated with folder_name (you should implement this logic)
    receiver_email = 'prathmesh.soni51@gmail.com'

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    # msg['Cc'] = cc_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
    except Exception as e:
        print(f"Error sending email: {e}")


if __name__ == '__main__':
    send_email()