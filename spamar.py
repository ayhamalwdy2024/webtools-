import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = 'smtp.example.com'
smtp_port = 587
sender_email = 'your-email@example.com'
sender_password = 'your-password'
receiver_email = 'recipient-email@example.com'

subject = 'Test Email'
body = 'This is a test email.'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print('Email sent successfully!')
except Exception as e:
    print(f'Failed to send email: {e}')
