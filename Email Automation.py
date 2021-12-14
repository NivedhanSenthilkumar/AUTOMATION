
                                'LIBRARIES'
import pandas as pd
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

                           '1-SMTP(Sendmail Task Protocol)'
                           '1.1 - Mail without attachment'
#DATA
data = pd.read_excel('D:/shopster/RESUMES/UX Engineer/GL/UI.xlsx')

#CREDENTIALS
SenderAddress = "hr@shopster.ai"
password = "shopster123!"
emails = data['Email'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)

#MESSAGE
msg = """Hello,There are tasks we would like you to do. All 3 tasks are mandatory. The deadline is by  Saturday at 6 p.m.
Task 1 - Frontend
https://github.com/shrihari1999/rock-paper-scissor
No need to focus on the backend for this.

Task 2 - SaaS Enterprise Visitor Management System
We use Django primarily, and we would like to give you a sample project to see how quickly you might be able to build this project.

Imagine our Customer is an enterprise with multiple office locations and  employees. They want to install this at the front desk, reception of different locations. They will use this to log their visitors.

Screens to build:
1. Employee Directory: view, add, edit, update, delete list of employees, with their name, email address, office location, and department.
2. Visitor Log : view, add, edit, update, delete visitor logs to one of the several office locations of a company. Also collect visitor's personal info, and which employee he is visiting. Able to change Visitor status: ‘Waiting for Check in’, ‘Inside Building’, ‘Checked Out’.
3. Add REST API for the above using Django Rest Framework with both Token and Session Authentication.

Reference :  https://photos.app.goo.gl/fh6JLNyidnmxDP8j9
The product : https://envoy.com/visitor-registration/#

You can just use Bootstrap components for the interface and not spend much time on the look of the website. We focus only on the functionality.

Here is a tutorial on Django:  https://youtu.be/e1IyzVyrLSU

Task 3 - Scraping
Scrape Company Name, Company Website, all Founders Name, and their Email, Industries fields of all companies in Bangkok from crunchbase.com
You might need to start the free 1-week trial  for some of the above columns to be visible to complete this task.

Please confirm when you see this and start these tasks.

ABOUT US :

We are a team of passionate engineers from California, Bangkok, and India building a platform to bring the power of AI and Data-Driven Business Intelligence to every business, no matter the size. Our vision is to tech enable every step: from Marketing to Operations, all the way to Customer Service. We are looking for passionate and ambitious candidates for full-time and internship opportunities with firm understanding of web frameworks, APIs, databases, and back-end systems.

Job Reference Link: https://www.linkedin.com/jobs/view/2736053918/?refId=DyaNLovg89MIRxGpxp%2F2SQ%3D%3D&trackingId=%2FhoBGUWNgxQ%2Fxw%2FmsY%2BaGg%3D%3D

Website :   https://shopster.ai/en/
Apple App Store : https://apps.apple.com/in/app/shopster-ai/id1572993701
Google Play Store : https://play.google.com/store/apps/details?id=com.shopster"""

#ENCODING
string_unicode = msg
string_encode = string_unicode.encode("ascii", "ignore")
string_decode = string_encode.decode()

#EMAILING
subject = "Full Stack Engineer"
body = "Subject: {}\n\n{}".format(subject,string_decode)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()

                               '1.2 - Mail with Attachment'
#LOGIN
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("hr@shopster.ai", "shopster123!")
fromaddr='hr@shopster.ai'

#MESSAGE
body = ("""Hi There Please refer attachment Thanks & Regards""")

#MAIL BLAST
for index, row in e.iterrows():
    msg = MIMEMultipart()
msg['From'] = fromaddr
msg['Subject'] = 'TEST'
msg.attach(MIMEText(body, 'plain'))
filename = 'D:/Rollingpinn/Product photos/carrot2.jpg'
toaddr = data['EMAILS']
attach_file_name = 'D:/Rollingpinn/Product photos/carrot2.jpg'
attach_file = open(attach_file_name, 'rb')
part = MIMEBase('application', 'octate-stream',filename='test.jpg')
part.set_payload((attach_file).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print("Emails sent successfully")
server.quit()

                             '1.3 -  EMAIL with multiple attachments'
#Set up crap for the attachments
files = 'D:/Rollingpinn/Product photos/'
filenames = [os.path.join(files, f) for f in os.listdir(files)]

#Set up users for email
gmail_user = "hr@shopster.ai"
gmail_pwd = "shopster123!"
recipients = data['EMAILS']

#Create Module
def mail(to, subject, text, attach):
   msg = MIMEMultipart()
   msg['From'] = gmail_user
   msg['To'] = data['EMAILS']
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   #get all the attachments
   for file in filenames:
      part = MIMEBase('application', 'octet-stream')
      part.set_payload(open(file, 'rb').read())
      encoders.encode_base64(part)
      part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
      msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

#send it
mail(recipients,
   "Its XMAS SEASON!!!!",
   """

https://rollingpinn.com/product/xmas-0.75lb/

สำหรับปีนี้ The Rolling Pinn ได้นำ ‘Xmas Special’ 
Tree Cake
โฉมใหม่ไฉไลกว่าเดิมกลับมาเพื่อให้คุณได้สนุกสนานและเพลิดเพลินในเทศกาลแห่งการให้แสนอบอุ่นด้วยเค้กสุดอลัง. 
เปิดให้จองแล้วในราคาพิเศษสำหรับ Early Bird Pre-Order ถึงวันที่ 20 ธันวาคมนี้เท่านั้น!  
มีให้เลือกถึง 3 สี 3 ขนาด สายหวานที่กำลังมองหาเค้กสุดน่ารักอยู่อย่ารอช้า
""",
filenames)


                              '2-SENDGRID'
my_sg = sendgrid.SendGridAPIClient(api_key = os.environ.get('SENDGRID_API_KEY'))
my_sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

# Change to your verified sender
from_email = Email("your_email@example.com")
# Change to your recipient
to_email = To("destination@example.com")

subject = "Lorem ipsum dolor sit amet"
content = Content("text/plain", "consectetur adipiscing elit")

mail = Mail(from_email, to_email, subject, content)
# Get a JSON-ready representation of the Mail object
mail_json = mail.get()
# Send an HTTP POST request to /mail/send
response = my_sg.client.mail.send.post(request_body=mail_json)


                         '3-COURIER-CHANNEL'
from trycourier import Courier
client = Courier(auth_token="pk_prod_ZN043V85VAM138K22DMK8G8Y2F8Y")
resp = client.send(
  event="courier-quickstart",
  recipient="aman@courier.com",
  data={
    "favoriteAdjective": "awesomeness"
  },
  profile={
    "email": "aman@courier.com"
  }
)
