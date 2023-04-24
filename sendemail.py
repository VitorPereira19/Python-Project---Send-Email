
import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['EMAIL_ADDRESS']

msg = EmailMessage()
msg['Subject'] = ''
msg['from'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('')

files = ['Random.pdf']

for file in files:
	with open(file, 'rb') as f:
		file_data = f.read()
		file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
 	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
 	smtp.send_message(msg)
