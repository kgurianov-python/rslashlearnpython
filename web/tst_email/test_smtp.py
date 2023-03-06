import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 2525
host = 'localhost'

port = 587
host = 'smtp.mailosaur.net'


def main():
    password = input("Type your password and press enter: ")

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login('BlackOroogo@gmail.com', password)


        message = MIMEMultipart("alternative")
        message["Subject"] = "test - with headers"
        message["From"] = 'BlackOroogo-test@gmail.com'
        message["To"] = 'kguryanov@gmail.com'

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)

        sender_email = "BlackOroogo@gmail.com"
        receiver_email = "kgurianov.it@gmail.com"

        # message = """Subject: test - partial_headers\n
        # To: kguryanov@gmail.com
        #
        #
        #          This is a test message.
        #          """

        server.sendmail(sender_email, receiver_email, message.as_string())
        # server.sendmail(sender_email, receiver_email, message)

        # print(message.as_string())

if __name__ == '__main__':
    main()
