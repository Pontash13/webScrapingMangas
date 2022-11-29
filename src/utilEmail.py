#enviar email com anexo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


def enviar_email(assunto, anexo):
    msg = MIMEMultipart()
    msg['From'] = 'alyssoncosta50@gmail.com'
    msg['To'] = 'ALYSSONCOSTA50_HF2FAF@kindle.com'
    msg['Subject'] = 'Convert'

    msg.attach(MIMEText('Enviando pelo gerador', 'plain'))

    # anexo
    filename = anexo
    attachment = open(anexo, "rb")

    part = MIMEApplication(attachment.read(), Name=filename)
    part['Content-Disposition'] = 'attachment; filename="%s"' % 'doc.epub'
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('alyssoncosta50@gmail.com', 'jujaykuhmpbhahpr')
    text = msg.as_string()
    server.sendmail('alyssoncosta50@gmail.com', 'ALYSSONCOSTA50_HF2FAF@kindle.com', text)
    server.quit()

enviar_email('teste', 'C:\\Users\\alyss\\PycharmProjects\\pythonProject\\Chainsaw Man_capCap. 112.epub')
print('email enviado')