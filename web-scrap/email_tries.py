import smtplib
conn = smtplib.SMTP('smtp-mail.outlook.com', 587)
type(conn)
conn
conn.ehlo()
conn.starttls()
conn.login('email@hotmail.com', 'password')
conn.sendmail('email@hotmail.com', 'email@hotmail.com', 'Subject: Testing123.\n\nHello,\n\n')