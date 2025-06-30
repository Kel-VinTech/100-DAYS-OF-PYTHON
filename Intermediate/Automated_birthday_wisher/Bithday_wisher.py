##################### Normal Starting Project ######################
import pandas
import random
import smtplib
import datetime as dt
from email_credentials import MY_EMAIL, MY_PASSWORD
from email.message import EmailMessage

# use MY_EMAIL and MY_PASSWORD in your SMTP code



now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month,today_day)

with open("Intermediate/Automated_birthday_wisher/birthdays.csv", "r") as data:
    data_file = pandas.read_csv(data)


birthdays_dict = {(row['month'], row['day']): row for (index, row) in data_file.iterrows()}


letters = f"Intermediate/Automated_birthday_wisher/letter_templates/letter_{random.randint(1,5)}.txt"

if today in birthdays_dict:
    
    birthday_today = birthdays_dict[today]
    name = birthday_today['name']
    to_user = birthday_today['email']
    

    # random_letter = random.choice(letters)

    with open(letters) as letter:
        content = letter.read()
        birthday_letter = content.replace('[NAME]',name)


        msg = EmailMessage()
        msg["Subject"] = "🎉 Happy Birthday!"
        msg["From"] = MY_EMAIL
        msg["To"] = to_user
        msg.set_content(birthday_letter)  # birthday_letter can contain emojis and special chars

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(MY_EMAIL, MY_PASSWORD)
            smtp.send_message(msg)  # use send_message, not sendmail

        




