## dependencies include IMAPclient and pyzmail
import imapclient
import pyzmail
from datetime import date

# connect to gmail
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('a.w.matheson@gmail.com', '2002Cliffwood')
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search([u'SINCE', date(2005, 4, 3)])
firstMessage = imapObj.fetch([UIDs[0]], ['BODY[]', 'FLAGS'])
lastMessage = imapObj.fetch([UIDs[-1]], ['BODY[]', 'FLAGS'])
back = False
if back:
	previousMessage = imapObj.fetch([UIDs[-1]], ['BODY[]', 'FLAGS'])
	#show previous message

delete = False
if delete:
	#delete message
	print("message deleted")

reply = False
if reply:
	# send canned response
	print("sending heart, smiley ...")

forward = False
if forward:
	# go to next message
	print("forward")