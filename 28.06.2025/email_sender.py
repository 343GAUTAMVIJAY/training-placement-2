import smtplib
from email.mime.text import MIMEText

sender = 'your_email@gmail.com'  # Replace with your email
password = 'your_password'  # Replace with app-specific password
receiver = input("Enter receiver email: ")
subject = input("Enter subject: ")
body = input("Enter message: ")
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
print("Email sent!")