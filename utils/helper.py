import random
import smtplib
from Config.Config import Config
import zipfile
from io import BytesIO


def generate_code(length):
    code = ''
    for i in range(length):
        code += str(random.randint(0, 9))
    return code


def send_email(input_message, email_to=Config.gmail_user):
    gmail_user = Config.gmail_user
    gmail_pwd = Config.gmail_password
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + email_to + '\n' + 'From: ' + gmail_user + '\n'
    msg = header + input_message
    smtpserver.sendmail(gmail_user, email_to, msg)
    smtpserver.close()


def generate_zip(files):
    mem_zip = BytesIO()

    with zipfile.ZipFile(mem_zip, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.writestr(f[0], f[1])

    return mem_zip.getvalue()
