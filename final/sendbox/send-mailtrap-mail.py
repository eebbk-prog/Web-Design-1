import smtplib

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message.

Check out http://mailtrap.io

-yuxiang
"""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("9601d23cf27838", "0a73cefe77630d")
    server.sendmail(sender, receiver, message)