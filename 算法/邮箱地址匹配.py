import re
re_email1 = re.compile('^[\w]+@[\w]+.com$')
email_address = input('Please enter your email address:')
if re_email1.match(email_address):
    print ('Yes, your email_address is valid')
    print (email_address)
else:
    print ('sorry, your email address is invalid')