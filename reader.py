import csv
import json
import smtplib

# open the JSON file containing the sender's email and password, and the email subject and body
with open("email_info.json", "r") as f:
    # load the JSON data
    data = json.load(f)
    # get the sender's email address and password
    sender_email = data["sender"]["email"]
    password = data["sender"]["password"]
    # get the subject and body of the email
    subject = data["email"]["subject"]
    body = data["email"]["body"]

# connect to the email server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)

# open the CSV file containing the recipients email addresses
with open("recipients.csv", "r") as f:
    # read the CSV file
    reader = csv.reader(f)
    # send the email to each recipient
    for row in reader:
        recipient = row[0]
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, recipient, message)

# disconnect from the email server
server.quit()
