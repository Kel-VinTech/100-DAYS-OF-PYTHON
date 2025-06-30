""" Learning about Google SMTP Port
simple mail transfer protocol
"""

# import smtplib

# my_email = "harryrober63@gmail.com"
# password = "fsya awnu zlvu tjyt"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user = my_email, password = password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="airdrop.email00@gmail.com", 
#         msg = "Subject:Hello\n\n This is the body of my email"
#     )


import datetime as dt
import random
import pandas
import smtplib
# now = dt.datetime.now()
# year = now.year
# day = now.weekday()
# month = now.month
# print(day, year)



def generate_quotes():
    now = dt.datetime.now()
    my_email = "harryrober63@gmail.com"
    password = "fsya awnu zlvu tjyt"

    if now.weekday() == 0:
        with open("Intermediate/Automated_birthday_wisher/quotes.txt" , "r") as data_quote:
            data = data_quote.readlines()
            quote = random.choice(data)
            print(quote)

        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user = my_email, password = password)
                connection.sendmail(
                    from_addr=my_email, 
                    to_addrs="harryrober63@gmail.com", 
                    msg = f"Subject:Hello\n\n {quote}"
                )

generate_quotes()

