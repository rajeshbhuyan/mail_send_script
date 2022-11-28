#!/usr/bin/python3

import os

# Add multiple mail by using commas
to = 'user1@domain.com, user3@domain.com '
# in cc field you can also add multiple users by using comma
cc = 'user2@domain.com'
# add the user who is sending the mail
fro = 'rkb334@gmail.com'
# Subject of the mail 
subject = 'Sending mail using python3'
# This is the meesage body. YOu can add any number of lines as per your requiremnt
message = '***** MAil is composed in python script!! *****'

MAIL = open(".letter", "w")
# Email Header
MAIL.write("To : "+to+"\n")
MAIL.write("Cc: "+cc+"\n")
MAIL.write("From: "+fro+"\n")
MAIL.write("Subject: "+subject+"\n")
# Email Body
MAIL.write("\n"+ message)
MAIL.close()
os.system('/usr/sbin/sendmail -t < .letter')

# Remove the temporary file
os.system('rm -rf .letter')
print ("Mail Sent successfully")
