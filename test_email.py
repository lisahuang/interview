# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

'''Google blocks sign-in attempts from apps which do not use modern security standards (mentioned on their support page). You can however, turn on/off this safety feature by going to the link below:

Go to this link and select Turn On
https://www.google.com/settings/security/lesssecureapps'''

# Create a text/plain message
msg = MIMEText('this is a test email')


me = 'my email address'
you = 'your email address'
msg['Subject'] = 'test email'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
#s = smtplib.SMTP('https://alphaur.e2k.ad.ge.com/ews/exchange.asmx', port=443)
s = smtplib.SMTP('smtp.gmail.com', port=587)
s.starttls()
s.login(me, "password")
s.sendmail(me, [you], msg.as_string())
s.quit()