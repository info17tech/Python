import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("priyankarmakar17@gmail.com","********")
msg = "hello"
server.sendmail("priyankarmakar17@gmail.com","poojitha202@gmail.com",msg)
print('mail is sent^.^')
server.quit()
