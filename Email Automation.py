import pandas as pd
import smtplib
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content


                           '1-SMTP'
#DATA
data = pd.read_excel('D:/shopster/RESUMES/Digital Marketing.xlsx')

#CREDENTIALS
SenderAddress = "hr@shopster.ai"
password = "shopster123!"
emails = data['EMAIL'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)

#MESSAGE
msg = '''Shopster-We are a team of passionate engineers from California, Bangkok, and India building a platform to bring the power of AI and Data-Driven Business Intelligence to every business, no matter the size. Our vision is to tech enable every step from Marketing to Operations, all the way to Customer service. Please find the attached files.
https://shopster.ai/en/
https://drive.google.com/file/d/1oDpQrM1Ph3hrbQ8hfITlO8j3QW2Y7Qi5/view?usp=sharing 
The Rolling Pinn is Bangkok’s boldest and sexiest bakery established in 2018. We have set out to make the highest quality desserts with the best ingredients for our beloved customers as we are committed to bringing cookieclimax right to your doorstep. It began when our CEO, Pinn started baking her favourite desserts which slowly became business when her passion was shared with others.
https://rollingpinn.com/ , https://www.instagram.com/therollingpinn/?hl=en
TASK :
Create a detailed digital marketing strategy for both, how will you execute it. Can see references to other similar B2B and Ecommerce Bakeries. The more rigorous, mathematical and broad it is, the better. Should not be superficial.
The task has to be done separately for two companies : Rollingpinn and Shopster
The deadline for the task is Friday 10AM.'''

#ENCODING
string_unicode = msg
string_encode = string_unicode.encode("ascii", "ignore")
string_decode = string_encode.decode()

#EMAILING
subject = "Digital Marketing Executive"
body = "Subject: {}\n\n{}".format(subject,string_decode)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()


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


                         'COURIER-CHANNEL'
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
