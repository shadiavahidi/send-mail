from datetime import datetime
import smtplib
import random

# enter sender email and password
my_email = "enter email address"
password = "enter password"

# enter your friend's birthday
birthday = datetime(2024, 7, 29).strftime("%Y,%m,%d")

now = datetime.now().strftime("%Y,%m,%d")

if now == birthday:
    with open("message") as message_file:
        all_text = message_file.readlines()
        quote = random.choice(all_text)
        # print(quote)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="enter the recipient's email",
                        msg=f"Subject:Happy birthday \n\n {quote}"
                        )
