
from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("my_email")
MY_PASSWORD = os.environ.get("my_password")


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# Successfully done!

# 2. Check if today matches a birthday in the birthdays.csv
bday_df = pandas.read_csv("birthdays.csv")
# print(bday_df)
# print(bday_df.columns)
bday_month = bday_df["month"]
dayy = bday_df["day"]

today= dt.datetime.today()

for index, row in bday_df.iterrows():
    if row["month"] == today.month and row["day"] == today.day:
        # print(f"Today is {row['name']}'s birthday!")
        bday_person= row['name']
        # print (bday_person)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
with open("scheduled-tasks/letter_templates/letter_3.txt", "r") as letter_file:
    letter_contents = letter_file.read()
    new_letter= letter_contents.replace("[NAME]", bday_person)

with open(f"scheduled-tasks/letter_templates/letter_for_{bday_person}.txt", mode= 'w') as completed_letter:
    completed_letter.write(new_letter)


# 4. Send the letter generated in step 3 to that person's email address.
my_email= os.environ.get("my_email")
my_password= os.environ.get("my_password")
connection= smtplib.SMTP('smtp.gmail.com', 587)
connection.set_debuglevel(1)
connection.starttls()
connection.login(user= my_email, password= my_password )
connection.sendmail(from_addr=my_email, to_addrs="oghenerunogbemre2026@gmail.com",
						msg= f"Subject: Happy Birthday \n\n {new_letter}")
connection.close()



