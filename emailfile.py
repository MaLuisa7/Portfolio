import smtplib
from email.mime.text import  MIMEText

body = 'This text email was sent from my pycharm local computer. El norte rifa mijo'

msg = MIMEText(body)

msg['From'] = 'mluisa.args@gmail.com'
msg['To'] = 'juliozeck@gmail.com'
msg['Subject'] = 'Hello-test'

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login('mluisa.args@gmail.com','bmrnclrsqpmmwjha')

server.send_message(msg)

print('Mail sent')

server.quit()