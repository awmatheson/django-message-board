import smtplib

# from and to info (to eventually be passed)
fromaddr = 'alyssa_message_board@gmail.com'
toaddrs  = 'warne_message_board@gmail.com'
msg = 'This is a test!'
username = 'alyssa_message_board@gmail.com'
password = 'pwd'

# open a gmail smtp object
smtpObj = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
smtpObj.starttls()
smtpObj.login(username,password)
smtpObj.sendmail(fromaddr, toaddrs, msg)
smtpObj.quit()