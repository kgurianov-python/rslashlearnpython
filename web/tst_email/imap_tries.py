import email
import imaplib

FROM_EMAIL = "@gmail.com"

SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

mail = imaplib.IMAP4_SSL(SMTP_SERVER)

pwd = input("Password:")

mail.login(FROM_EMAIL, pwd)
mail.select('inbox')

data = mail.search(None, '(FROM "Google")')
mail_ids = data[1]
id_list = mail_ids[0].split()
for num in id_list:
    data = mail.fetch(num, '(RFC822)' )
    for response_part in data:
        arr = response_part[0]
        if isinstance(arr, tuple):
            msg = email.message_from_bytes(arr[1])
            _, rec_date = msg['Received'].split(';')
            print(f"Subject: {msg['Subject']}\n\tSent: {msg['date']};\n\tReceived: {rec_date.strip()}")
            # print(msg['Received'][1])
            # print(f"Date: {msg['X-Received']}, {type(msg['date'])}")

    # tmp, date_ = mail.fetch(num, '(BODY[HEADER.FIELDS (DATE)])')
    # print (date_)
