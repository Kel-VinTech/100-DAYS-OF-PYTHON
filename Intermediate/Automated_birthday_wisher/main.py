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

now = dt.datetime.now()

print(now)