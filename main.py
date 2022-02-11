import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from decouple import config
from platform import python_version

server = 'smtp.yandex.ru'
user = config('user',default='')
password = config('password',default='')


recipients = ['mrgranze@yandex.ru']
sender = 'testmypythonmail@yandex.ru'
#sender = 'komissarotkrytkin@yandex.ru'
subject = 'Вас посетил Комиссар Открыткин'
text = '<h1>Вам пришла картинка!</h1>'
html = '<html><head></head><body><p>' + text + '<table><tr><td><img src="https://i.ytimg.com/vi/1HsXR3s4KuA/maxresdefault.jpg"  height="550" width="366"></td></tr></table>' + '</p></body></html>'

#

#

filepath = "fish.png"
basename = os.path.basename(filepath)
filesize = os.path.getsize(filepath)

msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = 'Oh my <' + sender + '>'
msg['To'] = ', '.join(recipients)
msg['Reply-To'] = sender
msg['Return-Path'] = sender
#msg['X-Mailer'] = 'Python/' + (python_version())


#https://ru.stackoverflow.com/questions/1124133/Как-отправить-фото-на-почту-python
#def addImage(self, path, file_type):
# path = os.path.abspath(path)
# file_name = path.split('\\')[-1]
# with open(path, 'rb') as file:
#     file = MIMEImage(file.read(), file_type)
#     file.add_header('Content-Disposition', 'attachment', filename=file_name) # Добавляем заголовки
# self.message.attach(file)
# sending_message_email.addImage('screen.png', 'PNG')


part_text = MIMEText(text, 'plain')
part_html = MIMEText(html, 'html')
part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
part_file.set_payload(open(filepath, "rb").read())
part_file.add_header('Content-Description', basename)
part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
encoders.encode_base64(part_file)

#msg.attach(part_text)
msg.attach(part_html)
#msg.attach(part_file)

mail = smtplib.SMTP_SSL(server)
mail.login(user, password)
mail.sendmail(sender, recipients, msg.as_string())
mail.quit()
