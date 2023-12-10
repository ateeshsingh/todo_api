# # import smtplib
# #
# # smtp_server = 'smtp.gmail.com'
# # smtp_port = 587
# # smtp_username = 'ateeshchauhan4023@gmail.com'
# # smtp_password = 'hdao kbqx oqay jxkk'
# #
# # from_email = 'ateeshchauhan4023@gmail.com'
# # to_email = 'ateesh.chauhan@flynava.ai'
# # subject = 'Hello, world!'
# # body = 'This is a test email.'
# #
# # message = f'Subject: {subject}\n\n{body}'
# #
# # with smtplib.SMTP(smtp_server, smtp_port) as smtp:
# #     smtp.starttls()
# #     smtp.login(smtp_username, smtp_password)
# #     smtp.sendmail(from_email, to_email, message)
# #
# #
# import time
#
# import schedule
# from schedule import every, repeat
# from pymongo import MongoClient
#
# client =MongoClient()
#
# @repeat(every(1).second)
# def reminder_email(planet):
#     pass
#
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
