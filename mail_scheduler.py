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
    to_email = receiver_mail
    subject = 'Task Reminder !!'
    body = f'This is a reminder email. for completing the {task_name}'
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(from_email, to_email, message)
    print("mail_sent")


@repeat(every(15).minutes)
def email_schedule():
    records = todo_app.db.get_collection("Todos").find({})
    for rec in records:
        mail_sender(receiver_mail=rec.get("email"), task_name=rec.get("name"))


while True:
    schedule.run_pending()
    time.sleep(secs=120)
