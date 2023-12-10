from src.settings.app import todo_app
import smtplib
import time
import schedule
from schedule import every, repeat


def mail_sender(receiver_mail, task_name):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'ateeshchauhan4023@gmail.com'
    smtp_password = 'hdao kbqx oqay jxkk'
    from_email = 'ateeshchauhan4023@gmail.com'
    to_email = receiver_mail  # 'ateesh.chauhan@flynava.ai'
    subject = 'Hello, world!'
    body = 'This is a test email.'
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(from_email, to_email, message)
    print("mail_sent")


@repeat(every(10).seconds)
def email_schedule():
    todo_app.db.get_collection("Todos").find({})
    mail_sender(receiver_mail="ateesh.chauhan@flynava.ai", task_name="")


while True:
    schedule.run_pending()
    time.sleep(1)
